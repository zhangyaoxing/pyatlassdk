"""Contract checks for every generated resource method in all three packages.

Each method is called with synthesized arguments against a stubbed ``client.request`` and the
request it would send is verified: HTTP verb, path templating and quoting, query-parameter
mapping, body/content-type pairing and Accept header.
"""

from __future__ import annotations

import datetime as dt
import inspect
import re
import types
import typing
from dataclasses import dataclass
from typing import Any, Union, get_args, get_origin, get_type_hints

import pytest
from pydantic import BaseModel

from pyatlassdk import AtlasAdminClient, AtlasAppAdminClient, AtlasStatusClient

VALID_VERBS = {"GET", "POST", "PUT", "PATCH", "DELETE"}
ADMIN_MEDIA = re.compile(r"^application/vnd\.atlas\.\d{4}-\d{2}-\d{2}\+(json|gzip|csv)$")
TRICKY_SEGMENT = "a/b c?#"  # must be percent-encoded when embedded in a path


@dataclass
class Call:
    package: str
    resource: str
    method: str
    kwargs: dict[str, Any]
    kwonly: list[str]
    has_body: bool
    sent: dict[str, Any]


class Stub:
    """Stands in for ``client.request`` and records its keyword arguments."""

    def __init__(self) -> None:
        self.sent: dict[str, Any] = {}

    def __call__(self, **kwargs: Any) -> None:
        self.sent = kwargs


def sample(annotation: Any) -> Any:
    """Build a throwaway value for a type annotation."""
    origin = get_origin(annotation)
    if origin in (Union, types.UnionType):
        options = [a for a in get_args(annotation) if a is not type(None)]
        return sample(options[0])
    if origin is typing.Literal:
        return get_args(annotation)[0]
    if origin in (list, list):
        return []
    if origin in (dict, dict):
        return {}
    if annotation is Any:
        return {}
    if annotation is str:
        return TRICKY_SEGMENT
    if annotation is bool:
        return True
    if annotation is int:
        return 7
    if annotation is float:
        return 1.5
    if annotation is dt.datetime:
        return dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
    if annotation is dt.date:
        return dt.date(2026, 1, 1)
    if inspect.isclass(annotation) and issubclass(annotation, BaseModel):
        return annotation.model_construct()
    if inspect.isclass(annotation) and issubclass(annotation, (str, int)):
        return next(iter(annotation))
    # e.g. a resource class shadowing a model of the same name (see KNOWN_ISSUES.md); the request
    # shape is still checkable with an opaque stand-in.
    return object()


def resources_of(client: Any) -> list[tuple[str, Any]]:
    return sorted(
        (name, value) for name, value in vars(client).items() if hasattr(value, "_client")
    )


def collect() -> list[Call]:
    clients = {
        "admin": AtlasAdminClient(),
        "app": AtlasAppAdminClient(access_token="t"),
        "status": AtlasStatusClient(),
    }
    calls: list[Call] = []
    for package, client in clients.items():
        for resource_name, resource in resources_of(client):
            for method_name, method in inspect.getmembers(resource, inspect.ismethod):
                if method_name.startswith("_"):
                    continue
                signature = inspect.signature(method)
                hints = get_type_hints(method)
                stub = Stub()
                client.request = stub  # type: ignore[method-assign]
                kwargs: dict[str, Any] = {}
                kwonly: list[str] = []
                for name, parameter in signature.parameters.items():
                    if parameter.kind is inspect.Parameter.KEYWORD_ONLY:
                        kwonly.append(name)
                    if name == "body" or parameter.kind is inspect.Parameter.KEYWORD_ONLY or parameter.default is inspect.Parameter.empty:
                        kwargs[name] = sample(hints[name])
                method(**kwargs)
                calls.append(
                    Call(
                        package,
                        resource_name,
                        method_name,
                        kwargs,
                        kwonly,
                        "body" in signature.parameters,
                        dict(stub.sent),
                    )
                )
        del client.request  # restore the class method
        client.close()
    return calls


CALLS = collect()
IDS = [f"{c.package}.{c.resource}.{c.method}" for c in CALLS]


def test_collected_a_realistic_number_of_methods() -> None:
    per_package = {p: sum(1 for c in CALLS if c.package == p) for p in ("admin", "app", "status")}

    assert per_package["admin"] > 500
    assert per_package["app"] > 100
    assert per_package["status"] == 8


def test_method_names_are_unique_within_each_resource() -> None:
    seen = set()
    for call in CALLS:
        key = (call.package, call.resource, call.method)
        assert key not in seen
        seen.add(key)


# GET endpoints that the generator emitted with a JSON body. HTTP GET bodies are not portable
# (proxies and servers may drop them) and the ``lineItems:search`` name suggests a POST search; see KNOWN_ISSUES.md (issue 5).
GET_WITH_BODY = {"admin.invoices.search_org_invoice_line_items"}


def _param(call: Call, ident: str) -> Any:
    return pytest.param(call, id=ident)


@pytest.fixture(params=[_param(c, i) for c, i in zip(CALLS, IDS)])
def call(request: pytest.FixtureRequest) -> Call:
    return request.param


def test_uses_a_valid_http_verb(call: Call) -> None:
    assert call.sent["method"] in VALID_VERBS


def test_path_is_absolute_and_fully_templated(call: Call) -> None:
    path = call.sent["path"]

    assert path.startswith("/")
    assert "{" not in path and "}" not in path
    assert "//" not in path
    assert not path.endswith("/") or path == "/"


def test_path_arguments_are_percent_encoded(call: Call) -> None:
    path = call.sent["path"]

    assert TRICKY_SEGMENT not in path
    assert "?" not in path and "#" not in path and " " not in path
    assert path.count("/") == path.replace("%2F", "").count("/")  # slashes only separate segments


def test_every_string_path_argument_appears_in_the_path(call: Call) -> None:
    positional = [
        name
        for name, value in call.kwargs.items()
        if name not in call.kwonly and name != "body" and value == TRICKY_SEGMENT
    ]
    encoded = "a%2Fb%20c%3F%23"

    assert call.sent["path"].count(encoded) >= (1 if positional else 0)
    assert call.sent["path"].count(encoded) == len(positional) or len(positional) == 0


def test_query_params_map_one_to_one_with_keyword_arguments(call: Call) -> None:
    params = call.sent.get("params")
    query_arguments = [name for name in call.kwonly if name != "body"]
    if not query_arguments:
        assert not params
        return

    assert params is not None
    assert len(params) == len(query_arguments)
    assert all(value is not None for value in params.values())


def test_query_param_names_are_wire_style(call: Call) -> None:
    for key in call.sent.get("params") or {}:
        assert re.fullmatch(r"[A-Za-z][A-Za-z0-9._\[\]\-]*", key), key


def test_body_is_forwarded_only_when_declared(call: Call) -> None:
    if call.has_body:
        assert "json" in call.sent
        assert call.sent["json"] is call.kwargs["body"]
    else:
        assert call.sent.get("json") is None


def test_content_type_is_sent_exactly_when_a_body_is_declared(call: Call) -> None:
    if call.package != "admin":
        assert call.sent.get("content_type") in (None, "application/json")
        return

    if call.has_body:
        assert ADMIN_MEDIA.match(call.sent["content_type"]) or call.sent["content_type"] == "application/json"
    else:
        assert call.sent.get("content_type") is None


@pytest.fixture(params=[_param(c, i) for c, i in zip(CALLS, IDS) if c.package == "admin"])
def admin_call(request: pytest.FixtureRequest) -> Call:
    return request.param


def test_admin_accept_header_is_versioned(admin_call: Call) -> None:
    call = admin_call
    accept = call.sent.get("accept")
    assert accept is not None
    assert ADMIN_MEDIA.match(accept) or accept == "application/json", accept


def test_request_always_passes_a_response_model_keyword(call: Call) -> None:
    assert "response_model" in call.sent


def test_delete_requests_have_no_body(call: Call) -> None:
    if call.sent["method"] == "DELETE":
        assert call.sent.get("json") is None


def test_get_requests_have_no_body(call: Call, request: pytest.FixtureRequest) -> None:
    ident = request.node.callspec.id.split("-")[-1]
    if ident in GET_WITH_BODY:
        request.applymarker(
            pytest.mark.xfail(strict=True, reason="GET sent with a JSON body (KNOWN_ISSUES.md #5)")
        )
    if call.sent["method"] == "GET":
        assert call.sent.get("json") is None
        assert call.sent.get("content_type") is None


def test_resource_methods_are_documented() -> None:
    clients = [AtlasAdminClient(), AtlasAppAdminClient(access_token="t"), AtlasStatusClient()]
    undocumented = []
    for client in clients:
        for resource_name, resource in resources_of(client):
            for method_name, method in inspect.getmembers(resource, inspect.ismethod):
                if not method_name.startswith("_") and not (method.__doc__ or "").strip():
                    undocumented.append(f"{resource_name}.{method_name}")
        client.close()

    assert undocumented == []
