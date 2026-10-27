"""AtlasAdminClient construction, Digest auth and OAuth 2.0 token handling."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import parse_qs

import httpx
import pytest

from conftest import Recorder, admin_client, attach_transport, oauth_client
from pyatlassdk import AtlasAdminApiError, AtlasAdminClient
from pyatlassdk.admin import client as admin_module

RESOURCE_DIR = Path(admin_module.__file__).parent / "resources"


# --------------------------------------------------------------------------- construction


@pytest.mark.parametrize(
    "kwargs",
    [
        {"public_key": "pub"},
        {"private_key": "priv"},
        {"public_key": "", "private_key": ""},
        {"public_key": "pub", "private_key": ""},
        {"public_key": "", "private_key": "priv"},
    ],
)
def test_incomplete_api_keys_are_rejected(kwargs) -> None:
    with pytest.raises(ValueError, match="public_key and private_key"):
        AtlasAdminClient(**kwargs)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"client_id": "id"},
        {"client_secret": "secret"},
        {"client_id": "", "client_secret": ""},
        {"client_id": "id", "client_secret": ""},
    ],
)
def test_incomplete_service_account_credentials_are_rejected(kwargs) -> None:
    with pytest.raises(ValueError, match="client_id and client_secret"):
        AtlasAdminClient(**kwargs)


def test_mixing_api_keys_and_service_account_is_rejected() -> None:
    with pytest.raises(ValueError, match="not both"):
        AtlasAdminClient(
            public_key="pub", private_key="priv", client_id="id", client_secret="secret"
        )
    with pytest.raises(ValueError, match="not both"):
        AtlasAdminClient(public_key="pub", client_id="id")


def test_auth_modes() -> None:
    with AtlasAdminClient() as anonymous:
        assert anonymous.auth_mode == "anonymous"
    with AtlasAdminClient(public_key="p", private_key="k") as digest:
        assert digest.auth_mode == "digest"
        assert isinstance(digest._http.auth, httpx.DigestAuth)
    with AtlasAdminClient(client_id="i", client_secret="s") as oauth:
        assert oauth.auth_mode == "oauth2"
        assert oauth._http.auth is None or not isinstance(oauth._http.auth, httpx.DigestAuth)


def test_defaults() -> None:
    with AtlasAdminClient() as client:
        assert str(client._http.base_url).rstrip("/") == admin_module.DEFAULT_BASE_URL
        assert client._http.timeout == httpx.Timeout(30.0)
        assert client._oauth_token_url == admin_module.DEFAULT_OAUTH_TOKEN_URL


def test_custom_base_url_timeout_and_token_url() -> None:
    with AtlasAdminClient(
        base_url="https://gov.example/api/atlas/v2",
        oauth_token_url="https://gov.example/oauth/token",
        timeout=5.0,
    ) as client:
        assert str(client._http.base_url).startswith("https://gov.example/api/atlas/v2")
        assert client._http.timeout == httpx.Timeout(5.0)
        assert client._oauth_token_url == "https://gov.example/oauth/token"


def test_every_resource_is_attached_to_the_client() -> None:
    with AtlasAdminClient() as client:
        resources = [v for v in vars(client).values() if hasattr(v, "_client")]

    modules = {p.stem for p in RESOURCE_DIR.glob("*.py") if p.stem != "__init__"}
    assert {type(r).__module__.rsplit(".", 1)[-1] for r in resources} == modules
    assert all(resource._client is client for resource in resources)


# --------------------------------------------------------------------------- anonymous / digest


def test_digest_client_sends_no_authorization_until_challenged(recorder: Recorder) -> None:
    admin_client(recorder).request("GET", "/ping")

    assert "authorization" not in recorder.last.headers


def test_anonymous_client_sends_no_authorization(recorder: Recorder) -> None:
    client = attach_transport(AtlasAdminClient(), recorder)
    client.request("GET", "/ping")

    assert "authorization" not in recorder.last.headers


def test_digest_auth_answers_a_challenge(recorder: Recorder) -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        if "authorization" not in request.headers:
            return httpx.Response(
                401,
                headers={
                    "www-authenticate": 'Digest realm="atlas", nonce="abc", qop="auth", '
                    'algorithm=MD5, opaque="xyz"'
                },
            )
        return httpx.Response(200, json={})

    recorder.response = respond
    admin_client(recorder).request("GET", "/ping")

    assert len(recorder.requests) == 2
    answer = recorder.requests[1].headers["authorization"]
    assert answer.startswith("Digest ")
    assert 'username="public"' in answer
    assert 'realm="atlas"' in answer


def test_digest_client_never_calls_the_oauth_endpoint(recorder: Recorder) -> None:
    admin_client(recorder).request("GET", "/ping")

    assert all("oauth" not in str(r.url) for r in recorder.requests)


def test_persistent_401_with_digest_raises(recorder: Recorder) -> None:
    recorder.response = lambda request: httpx.Response(401, json={"detail": "bad keys"})

    with pytest.raises(AtlasAdminApiError) as excinfo:
        admin_client(recorder).request("GET", "/ping")

    assert excinfo.value.status_code == 401
    assert len(recorder.requests) == 1


# --------------------------------------------------------------------------- OAuth 2.0


def token_response(token: str = "tok-1", expires_in: object = 3600) -> httpx.Response:
    body: dict[str, object] = {"access_token": token, "token_type": "Bearer"}
    if expires_in is not None:
        body["expires_in"] = expires_in
    return httpx.Response(200, json=body)


class OAuthServer:
    """Fake Atlas that issues numbered tokens and records API calls."""

    def __init__(self, *, reject_tokens: set[str] | None = None) -> None:
        self.token_calls = 0
        self.api_calls: list[httpx.Request] = []
        self.token_requests: list[httpx.Request] = []
        self.reject = reject_tokens or set()

    def __call__(self, request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/oauth/token"):
            self.token_calls += 1
            self.token_requests.append(request)
            return token_response(f"tok-{self.token_calls}")
        self.api_calls.append(request)
        token = request.headers.get("authorization", "").removeprefix("Bearer ")
        if token in self.reject:
            return httpx.Response(401, json={"detail": "expired"})
        return httpx.Response(200, json={})


def test_oauth_token_request_shape() -> None:
    server = OAuthServer()
    client = oauth_client(server)

    client.request("GET", "/ping")

    sent = server.token_requests[0]
    assert sent.method == "POST"
    assert str(sent.url) == admin_module.DEFAULT_OAUTH_TOKEN_URL
    assert sent.headers["content-type"] == "application/x-www-form-urlencoded"
    assert parse_qs(sent.content.decode()) == {
        "grant_type": ["client_credentials"],
        "client_id": ["id"],
        "client_secret": ["secret"],
    }


def test_oauth_api_requests_carry_bearer_token() -> None:
    server = OAuthServer()
    oauth_client(server).request("GET", "/ping")

    assert server.api_calls[0].headers["authorization"] == "Bearer tok-1"


def test_oauth_token_is_cached_across_requests() -> None:
    server = OAuthServer()
    client = oauth_client(server)

    for _ in range(3):
        client.request("GET", "/ping")

    assert server.token_calls == 1
    assert len(server.api_calls) == 3


def test_oauth_token_is_refreshed_after_expiry(monkeypatch: pytest.MonkeyPatch) -> None:
    now = [1000.0]
    monkeypatch.setattr(admin_module.time, "monotonic", lambda: now[0])
    server = OAuthServer()
    client = oauth_client(server)

    client.request("GET", "/ping")
    now[0] += 3600 - 61  # still inside the 60s safety margin
    client.request("GET", "/ping")
    assert server.token_calls == 1

    now[0] += 2  # past lifetime - 60s
    client.request("GET", "/ping")
    assert server.token_calls == 2
    assert server.api_calls[-1].headers["authorization"] == "Bearer tok-2"


def test_oauth_short_lifetimes_are_floored_at_one_second(monkeypatch: pytest.MonkeyPatch) -> None:
    now = [0.0]
    monkeypatch.setattr(admin_module.time, "monotonic", lambda: now[0])
    client = oauth_client(lambda request: token_response(expires_in=10))

    client._access_token()

    assert client._oauth_expires_at == pytest.approx(1.0)


@pytest.mark.parametrize("expires_in", [None, "abc", [], {}])
def test_oauth_invalid_expires_in_falls_back_to_an_hour(
    monkeypatch: pytest.MonkeyPatch, expires_in
) -> None:
    now = [0.0]
    monkeypatch.setattr(admin_module.time, "monotonic", lambda: now[0])
    client = oauth_client(lambda request: token_response(expires_in=expires_in))

    client._access_token()

    assert client._oauth_expires_at == pytest.approx(3540.0)


def test_oauth_numeric_string_expires_in_is_accepted(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(admin_module.time, "monotonic", lambda: 0.0)
    client = oauth_client(lambda request: token_response(expires_in="600"))

    client._access_token()

    assert client._oauth_expires_at == pytest.approx(540.0)


def test_oauth_401_triggers_one_refresh_and_retry() -> None:
    server = OAuthServer(reject_tokens={"tok-1"})
    client = oauth_client(server)

    client.request("GET", "/ping")

    assert server.token_calls == 2
    assert [r.headers["authorization"] for r in server.api_calls] == [
        "Bearer tok-1",
        "Bearer tok-2",
    ]


def test_oauth_retry_resends_the_body() -> None:
    server = OAuthServer(reject_tokens={"tok-1"})
    client = oauth_client(server)

    client.request("POST", "/things", json={"a": 1})

    assert server.api_calls[0].content == server.api_calls[1].content
    assert json.loads(server.api_calls[1].content) == {"a": 1}


def test_oauth_second_401_is_raised_without_a_third_attempt() -> None:
    server = OAuthServer(reject_tokens={"tok-1", "tok-2", "tok-3"})
    client = oauth_client(server)

    with pytest.raises(AtlasAdminApiError) as excinfo:
        client.request("GET", "/ping")

    assert excinfo.value.status_code == 401
    assert len(server.api_calls) == 2
    assert server.token_calls == 2


def test_oauth_non_401_errors_do_not_refresh() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/oauth/token"):
            return token_response()
        return httpx.Response(403, json={"detail": "forbidden"})

    client = oauth_client(handler)
    with pytest.raises(AtlasAdminApiError) as excinfo:
        client.request("GET", "/ping")

    assert excinfo.value.status_code == 403


def test_oauth_token_endpoint_error_is_wrapped() -> None:
    client = oauth_client(lambda request: httpx.Response(401, json={"error": "invalid_client"}))

    with pytest.raises(AtlasAdminApiError) as excinfo:
        client.request("GET", "/ping")

    assert excinfo.value.status_code == 401
    assert "access token" in str(excinfo.value)
    assert excinfo.value.payload == {"error": "invalid_client"}


@pytest.mark.parametrize(
    "body", [{}, {"access_token": ""}, {"access_token": None}, {"access_token": 5}]
)
def test_oauth_missing_or_invalid_token_is_wrapped(body) -> None:
    client = oauth_client(lambda request: httpx.Response(200, json=body))

    with pytest.raises(AtlasAdminApiError) as excinfo:
        client.request("GET", "/ping")

    assert excinfo.value.status_code == 500
    assert "access_token" in str(excinfo.value)
    assert excinfo.value.payload == body


def test_oauth_failed_token_fetch_does_not_cache_anything() -> None:
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/oauth/token"):
            calls["n"] += 1
            return httpx.Response(500, text="down") if calls["n"] == 1 else token_response()
        return httpx.Response(200, json={})

    client = oauth_client(handler)
    with pytest.raises(AtlasAdminApiError):
        client.request("GET", "/ping")

    client.request("GET", "/ping")

    assert client._oauth_token == "tok-1"


def test_access_token_without_credentials_is_a_401() -> None:
    with AtlasAdminClient() as client, pytest.raises(AtlasAdminApiError) as excinfo:
        client._access_token()

    assert excinfo.value.status_code == 401


def test_explicit_refresh_bypasses_the_cache() -> None:
    server = OAuthServer()
    client = oauth_client(server)

    first = client._access_token()
    second = client._access_token(refresh=True)

    assert (first, second) == ("tok-1", "tok-2")


def test_custom_oauth_token_url_is_used() -> None:
    server = OAuthServer()
    client = oauth_client(
        server,
        client_id="id",
        client_secret="secret",
        oauth_token_url="https://other.test/oauth/token",
    )
    client.request("GET", "/ping")

    assert str(server.token_requests[0].url) == "https://other.test/oauth/token"


def test_basic_authorization_header_is_not_sent_to_token_endpoint() -> None:
    server = OAuthServer()
    oauth_client(server).request("GET", "/ping")

    sent = server.token_requests[0]
    assert "authorization" not in sent.headers  # credentials travel in the form body
