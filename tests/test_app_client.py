"""AtlasAppAdminClient construction, bearer auth and API-key login."""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest

from conftest import Recorder, app_client
from pyatlassdk import AtlasAppAdminClient, AtlasAppApiError
from pyatlassdk.app import client as app_module

RESOURCE_DIR = Path(app_module.__file__).parent / "resources"


def test_constructor_sets_bearer_header_and_defaults() -> None:
    with AtlasAppAdminClient(access_token="abc") as client:
        assert client.auth_mode == "bearer"
        assert client._http.headers["authorization"] == "Bearer abc"
        assert str(client._http.base_url).rstrip("/") == app_module.DEFAULT_BASE_URL
        assert client._http.timeout == httpx.Timeout(30.0)


def test_access_token_is_required() -> None:
    with pytest.raises(TypeError):
        AtlasAppAdminClient()  # type: ignore[call-arg]


def test_custom_base_url_and_timeout() -> None:
    with AtlasAppAdminClient(access_token="t", base_url="https://eu.example/v3", timeout=2.5) as c:
        assert str(c._http.base_url).startswith("https://eu.example/v3")
        assert c._http.timeout == httpx.Timeout(2.5)


def test_every_resource_is_attached_to_the_client() -> None:
    with AtlasAppAdminClient(access_token="t") as client:
        resources = [v for v in vars(client).values() if hasattr(v, "_client")]

    modules = {p.stem for p in RESOURCE_DIR.glob("*.py") if p.stem != "__init__"}
    assert {type(r).__module__.rsplit(".", 1)[-1] for r in resources} == modules
    assert all(resource._client is client for resource in resources)


def test_requests_send_the_bearer_token(recorder: Recorder) -> None:
    app_client(recorder, token="xyz").request("GET", "/groups")

    assert recorder.last.headers["authorization"] == "Bearer xyz"


# --------------------------------------------------------------------------- login


class LoginServer:
    def __init__(self, response: httpx.Response) -> None:
        self.response = response
        self.requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.response


@pytest.fixture
def patch_http(monkeypatch: pytest.MonkeyPatch):
    """Route the throwaway client created inside ``login`` through a mock transport."""
    real_client = httpx.Client

    def install(server: LoginServer) -> None:
        def factory(*args, **kwargs):
            kwargs["transport"] = httpx.MockTransport(server)
            return real_client(*args, **kwargs)

        monkeypatch.setattr(app_module.httpx, "Client", factory)

    return install


def test_login_exchanges_api_key_for_a_client(patch_http) -> None:
    server = LoginServer(httpx.Response(200, json={"access_token": "jwt-1", "refresh_token": "r"}))
    patch_http(server)

    client = AtlasAppAdminClient.login(username="user", api_key="key")

    sent = server.requests[0]
    assert sent.method == "POST"
    assert str(sent.url) == f"{app_module.DEFAULT_BASE_URL}/auth/providers/mongodb-cloud/login"
    assert json.loads(sent.content) == {"username": "user", "apiKey": "key"}
    assert sent.headers["accept"] == "application/json"
    assert sent.headers["content-type"] == "application/json"
    assert isinstance(client, AtlasAppAdminClient)
    assert client._http.headers["authorization"] == "Bearer jwt-1"


def test_login_honours_base_url_and_timeout(patch_http) -> None:
    server = LoginServer(httpx.Response(200, json={"access_token": "t"}))
    patch_http(server)

    client = AtlasAppAdminClient.login("u", "k", base_url="https://eu.example/v3", timeout=4.0)

    assert str(server.requests[0].url) == "https://eu.example/v3/auth/providers/mongodb-cloud/login"
    assert str(client._http.base_url).startswith("https://eu.example/v3")
    assert client._http.timeout == httpx.Timeout(4.0)


def test_login_http_error_is_wrapped(patch_http) -> None:
    patch_http(LoginServer(httpx.Response(401, json={"error": "invalid creds"})))

    with pytest.raises(AtlasAppApiError) as excinfo:
        AtlasAppAdminClient.login("u", "bad")

    assert excinfo.value.status_code == 401
    assert excinfo.value.payload == {"error": "invalid creds"}


@pytest.mark.parametrize(
    "body", [{}, {"access_token": ""}, {"access_token": None}, {"access_token": 1}]
)
def test_login_without_a_usable_token_is_wrapped(patch_http, body) -> None:
    patch_http(LoginServer(httpx.Response(200, json=body)))

    with pytest.raises(AtlasAppApiError) as excinfo:
        AtlasAppAdminClient.login("u", "k")

    assert excinfo.value.status_code == 500
    assert excinfo.value.payload == body


def test_login_closes_its_temporary_http_client(
    patch_http, monkeypatch: pytest.MonkeyPatch
) -> None:
    created: list[httpx.Client] = []
    real_client = httpx.Client

    def factory(*args, **kwargs):
        kwargs["transport"] = httpx.MockTransport(
            LoginServer(httpx.Response(200, json={"access_token": "t"}))
        )
        created.append(real_client(*args, **kwargs))
        return created[-1]

    monkeypatch.setattr(app_module.httpx, "Client", factory)

    AtlasAppAdminClient.login("u", "k")

    assert created[0].is_closed
