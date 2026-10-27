"""``client.request`` behavior shared by the admin, app and status clients."""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest
from pydantic import BaseModel, ConfigDict, Field

from conftest import Recorder
from pyatlassdk import AtlasAdminApiError, AtlasAppApiError, AtlasStatusApiError

ERRORS = {"admin": AtlasAdminApiError, "app": AtlasAppApiError, "status": AtlasStatusApiError}
DEFAULT_ACCEPT = {
    "admin": "application/vnd.atlas.2025-03-12+json",
    "app": "application/json",
    "status": "application/json",
}


class Widget(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    widget_id: str = Field(alias="widgetId")


def test_default_accept_header(package, make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things")

    assert recorder.last.headers["accept"] == DEFAULT_ACCEPT[package]


def test_accept_override(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things", accept="application/x-test")

    assert recorder.last.headers["accept"] == "application/x-test"


def test_no_content_type_without_body(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things")

    assert "content-type" not in recorder.last.headers
    assert recorder.last.content == b""


def test_content_type_defaults_to_accept_family_when_body_present(
    package, make_client, recorder: Recorder
) -> None:
    make_client().request("POST", "/things", json={"a": 1})

    assert recorder.last.headers["content-type"] == DEFAULT_ACCEPT[package]
    assert json.loads(recorder.last.content) == {"a": 1}


def test_content_type_override(make_client, recorder: Recorder) -> None:
    make_client().request("POST", "/things", json={"a": 1}, content_type="application/x-test")

    assert recorder.last.headers["content-type"] == "application/x-test"


@pytest.mark.parametrize("body", [[], {}, 0, False, ""])
def test_falsy_but_not_none_bodies_are_still_sent(make_client, recorder: Recorder, body) -> None:
    make_client().request("POST", "/things", json=body)

    assert "content-type" in recorder.last.headers
    assert json.loads(recorder.last.content) == body


def test_models_in_body_are_serialized_with_aliases(make_client, recorder: Recorder) -> None:
    make_client().request("POST", "/things", json=Widget(widget_id="w1"))

    assert json.loads(recorder.last.content) == {"widgetId": "w1"}


def test_none_params_are_dropped(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things", params={"a": 1, "b": None, "c": "x"})

    assert dict(recorder.last.url.params) == {"a": "1", "c": "x"}


def test_falsy_params_are_kept(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things", params={"zero": 0, "off": False, "empty": ""})

    assert dict(recorder.last.url.params) == {"zero": "0", "off": "false", "empty": ""}


def test_list_params_repeat_the_key(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things", params={"id": ["a", "b"]})

    assert recorder.last.url.params.get_list("id") == ["a", "b"]


def test_no_params_means_no_query_string(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things")

    assert recorder.last.url.query == b""


def test_path_is_joined_to_base_url(make_client, recorder: Recorder) -> None:
    make_client().request("GET", "/things/1")

    assert str(recorder.last.url) == "https://example.test/api/things/1"


def test_response_model_none_returns_none(make_client, recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(200, json={"ignored": True})

    assert make_client().request("GET", "/things") is None


def test_response_is_validated_into_model(make_client, recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(200, json={"widgetId": "w1"})

    result = make_client().request("GET", "/things", response_model=Widget)

    assert isinstance(result, Widget)
    assert result.widget_id == "w1"


def test_response_is_validated_into_list_of_models(make_client, recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(
        200, json=[{"widgetId": "a"}, {"widgetId": "b"}]
    )

    result = make_client().request("GET", "/things", response_model=list[Widget])

    assert [w.widget_id for w in result] == ["a", "b"]


def test_response_model_any_returns_raw_json(make_client, recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(200, json={"k": [1, 2]})

    assert make_client().request("GET", "/things", response_model=Any) == {"k": [1, 2]}


def test_invalid_response_raises_validation_error(make_client, recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(200, json={"wrong": 1})

    with pytest.raises(Exception) as excinfo:
        make_client().request("GET", "/things", response_model=Widget)

    assert type(excinfo.value).__name__ == "ValidationError"


@pytest.mark.parametrize("status", [400, 403, 404, 409, 429, 500, 503])
def test_error_status_raises_atlas_api_error(
    package, make_client, recorder: Recorder, status: int
) -> None:
    recorder.response = lambda request: httpx.Response(status, json={"detail": "nope"})

    with pytest.raises(ERRORS[package]) as excinfo:
        make_client().request("GET", "/things")

    assert excinfo.value.status_code == status
    assert excinfo.value.payload == {"detail": "nope"}
    assert str(excinfo.value).startswith(f"HTTP {status}:")


def test_error_with_plain_text_body_keeps_text_payload(
    package, make_client, recorder: Recorder
) -> None:
    recorder.response = lambda request: httpx.Response(502, text="bad gateway")

    with pytest.raises(ERRORS[package]) as excinfo:
        make_client().request("GET", "/things")

    assert excinfo.value.payload == "bad gateway"
    assert "bad gateway" in str(excinfo.value)


def test_error_is_raised_before_model_validation(package, make_client, recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(404, json={"detail": "x"})

    with pytest.raises(ERRORS[package]):
        make_client().request("GET", "/things", response_model=Widget)


@pytest.mark.parametrize("method", ["GET", "POST", "PUT", "PATCH", "DELETE"])
def test_http_method_is_forwarded(make_client, recorder: Recorder, method: str) -> None:
    make_client().request(method, "/things")

    assert recorder.last.method == method


def test_transport_errors_propagate(make_client, recorder: Recorder) -> None:
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("down")

    recorder.response = boom

    with pytest.raises(httpx.ConnectError):
        make_client().request("GET", "/things")


def test_client_is_a_context_manager_that_closes(package) -> None:
    from conftest import CLIENT_FACTORIES

    client = CLIENT_FACTORIES[package](lambda request: httpx.Response(200, json={}))
    with client as entered:
        assert entered is client
        assert not client._http.is_closed

    assert client._http.is_closed


def test_close_is_idempotent(make_client) -> None:
    client = make_client()
    client.close()
    client.close()

    assert client._http.is_closed


def test_401_raises_for_clients_without_challenge_auth(recorder: Recorder) -> None:
    from conftest import app_client, status_client

    recorder.response = lambda request: httpx.Response(401, json={"detail": "nope"})

    for factory, error in ((app_client, AtlasAppApiError), (status_client, AtlasStatusApiError)):
        with pytest.raises(error) as excinfo:
            factory(recorder).request("GET", "/things")
        assert excinfo.value.status_code == 401
