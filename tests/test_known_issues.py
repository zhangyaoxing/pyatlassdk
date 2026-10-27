"""Executable record of the defects documented in ``KNOWN_ISSUES.md``.

Every test here asserts the *correct* behavior and is marked ``xfail(strict=True)``: the suite
stays green while the bug exists, and turns red the moment a fix lands so the marker (and the
matching entry in KNOWN_ISSUES.md) gets removed. Nothing under ``src/`` was changed to make these
pass or fail.
"""

from __future__ import annotations

import gzip
import json
from typing import Any

import httpx
import pytest
from pydantic import BaseModel

from conftest import CLIENT_FACTORIES, Recorder, admin_client, oauth_client
from pyatlassdk import AtlasAdminApiError, AtlasAppAdminClient, AtlasAppApiError
from pyatlassdk.app import client as app_module


def known_issue(number: int, summary: str, raises: type[BaseException] = Exception):
    """Strict xfail; ``raises`` keeps an unrelated crash (e.g. a typo) from hiding as expected."""
    return pytest.mark.xfail(
        strict=True, reason=f"KNOWN_ISSUES.md #{number}: {summary}", raises=raises
    )


# --------------------------------------------------------------------------- 1. Literal[true]


@known_issue(1, "models annotated Literal[true]/Literal[false] can never be built")
@pytest.mark.parametrize(
    "module, name",
    [
        ("email_password_auth_provider", "EmailPasswordAuthProvider"),
        *[
            (f"email_password_auth_provider_config_variant{i}", f"EmailPasswordAuthProviderConfigVariant{i}")
            for i in range(1, 7)
        ],
        ("push_pull_app_config", "PushPullAppConfig"),
    ],
)
def test_model_with_literal_true_is_usable(module: str, name: str) -> None:
    import importlib

    cls = getattr(importlib.import_module(f"pyatlassdk.app.models.{module}"), name)

    assert cls.__pydantic_complete__
    cls.model_json_schema()


@known_issue(1, "pushing an app configuration needs PushPullAppConfig")
def test_push_app_configuration_body_can_be_constructed() -> None:
    from pyatlassdk.app.models.push_pull_app_config import PushPullAppConfig

    PushPullAppConfig(name="demo", provider_region="aws-us-east-1")


# --------------------------------------------------------------------------- 2. shadowed model


@known_issue(2, "resource class shadows the model it returns")
def test_cluster_outage_simulation_resource_returns_the_model(recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(
        200, json={"clusterName": "c", "state": "SIMULATING"}
    )

    result = admin_client(recorder).cluster_outage_simulation.get_group_cluster_outage_simulation(
        "g", "c"
    )

    assert isinstance(result, BaseModel)
    assert result.state == "SIMULATING"


@known_issue(2, "resource class shadows the model it returns")
@pytest.mark.parametrize(
    "method", ["get_group_cluster_outage_simulation", "end_group_cluster_outage_simulation"]
)
def test_cluster_outage_simulation_response_model_is_a_pydantic_model(method: str) -> None:
    sent: dict[str, Any] = {}
    client = admin_client(Recorder())
    client.request = lambda **kwargs: sent.update(kwargs)  # type: ignore[method-assign]

    getattr(client.cluster_outage_simulation, method)("g", "c")

    assert isinstance(sent["response_model"], type) and issubclass(sent["response_model"], BaseModel)


# --------------------------------------------------------------------------- 3. empty bodies


@known_issue(3, "successful empty responses crash when a response_model is declared")
@pytest.mark.parametrize("package", sorted(CLIENT_FACTORIES))
@pytest.mark.parametrize("status", [200, 202, 204])
def test_empty_success_body_with_any_model_returns_none(package: str, status: int) -> None:
    client = CLIENT_FACTORIES[package](lambda request: httpx.Response(status))

    assert client.request("DELETE", "/things/1", response_model=Any) is None


@known_issue(3, "DELETE endpoints (73 methods declare response_model=Any) cannot succeed")
def test_remove_team_from_project_handles_no_content(recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(204)

    assert admin_client(recorder).teams.remove_group_team("g", "t") is None


# --------------------------------------------------------------------------- 4. non-JSON downloads


@known_issue(4, "gzip endpoints parse the body as JSON")
def test_log_download_returns_the_raw_payload(recorder: Recorder) -> None:
    raw = gzip.compress(b"2026-01-01T00:00:00 I NETWORK listening\n")
    recorder.response = lambda request: httpx.Response(
        200, content=raw, headers={"content-type": "application/gzip"}
    )

    result = admin_client(recorder).monitoring_and_logs.download_group_cluster_log(
        "g", "host", "mongodb"
    )

    assert result == raw or gzip.decompress(result.encode("latin-1")) == gzip.decompress(raw)


@known_issue(4, "CSV endpoint parses the body as JSON")
def test_csv_invoice_download_returns_text(recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(
        200, text="id,amount\n1,10\n", headers={"content-type": "text/csv"}
    )

    result = admin_client(recorder).invoices.get_org_invoice_csv("o", "i")

    assert "id,amount" in result


@known_issue(4, "a plain-text body cannot be returned for response_model=str")
def test_request_returns_text_for_str_model(recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(200, text="hello")

    assert admin_client(recorder).request("GET", "/x", response_model=str) == "hello"


# --------------------------------------------------------------------------- 6. token payloads


@known_issue(6, "non-JSON OAuth token response escapes as JSONDecodeError")
def test_oauth_token_endpoint_with_html_body_raises_atlas_error() -> None:
    client = oauth_client(lambda request: httpx.Response(200, text="<html>maintenance</html>"))

    with pytest.raises(AtlasAdminApiError):
        client.request("GET", "/ping")


@known_issue(6, "non-object OAuth token response escapes as AttributeError")
def test_oauth_token_endpoint_with_array_body_raises_atlas_error() -> None:
    client = oauth_client(lambda request: httpx.Response(200, json=["not", "an", "object"]))

    with pytest.raises(AtlasAdminApiError):
        client.request("GET", "/ping")


@known_issue(6, "non-JSON login response escapes as JSONDecodeError")
def test_app_login_with_html_body_raises_atlas_error(monkeypatch: pytest.MonkeyPatch) -> None:
    real_client = httpx.Client

    def factory(*args: Any, **kwargs: Any) -> httpx.Client:
        kwargs["transport"] = httpx.MockTransport(lambda r: httpx.Response(200, text="<html>"))
        return real_client(*args, **kwargs)

    monkeypatch.setattr(app_module.httpx, "Client", factory)

    with pytest.raises(AtlasAppApiError):
        AtlasAppAdminClient.login("u", "k")


# --------------------------------------------------------------------------- 7. redirects


@known_issue(7, "3xx responses are neither followed nor reported as AtlasApiError")
@pytest.mark.parametrize("package", sorted(CLIENT_FACTORIES))
def test_redirect_response_raises_atlas_error(package: str) -> None:
    from pyatlassdk import AtlasStatusApiError

    client = CLIENT_FACTORIES[package](
        lambda request: httpx.Response(302, headers={"location": "https://elsewhere.test/"})
    )

    with pytest.raises((AtlasAdminApiError, AtlasAppApiError, AtlasStatusApiError)):
        client.request("GET", "/things", response_model=Any)


# --------------------------------------------------------------------------- 8. empty token


@known_issue(8, "AtlasAppAdminClient accepts an empty access token", raises=pytest.fail.Exception)
def test_app_client_rejects_empty_access_token() -> None:
    with pytest.raises(ValueError):
        AtlasAppAdminClient(access_token="")


# --------------------------------------------------------------------------- 9. characterization


def test_explicit_none_cannot_be_sent_to_clear_a_field(recorder: Recorder) -> None:
    """Characterization of KNOWN_ISSUES.md #9 (design limitation, not marked xfail).

    Request bodies are dumped with ``exclude_none=True``, so a model field set to ``None`` is
    indistinguishable from an unset one and is never transmitted as JSON ``null``.
    """
    from pyatlassdk.admin.models.team_response import TeamResponse

    admin_client(recorder).request("PATCH", "/teams/1", json=TeamResponse(id=None, name=None))

    assert json.loads(recorder.last.content) == {}
