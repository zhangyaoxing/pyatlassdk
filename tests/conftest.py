"""Shared fixtures and helpers for the pyatlassdk test suites."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import httpx
import pytest

from pyatlassdk import AtlasAdminClient, AtlasAppAdminClient, AtlasStatusClient

Handler = Callable[[httpx.Request], httpx.Response]

BASE_URL = "https://example.test/api"


@dataclass
class Recorder:
    """Captures every request seen by a mocked transport and replies with a canned response."""

    requests: list[httpx.Request] = field(default_factory=list)
    response: Callable[[httpx.Request], httpx.Response] = lambda request: httpx.Response(
        200, json={}
    )

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        return self.response(request)

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]


def attach_transport(client: Any, handler: Handler, base_url: str = BASE_URL) -> Any:
    """Swap the client's HTTP transport for a mock while keeping its default headers/auth."""
    old = client._http
    headers = dict(old.headers)
    auth = old.auth
    old.close()
    client._http = httpx.Client(
        base_url=base_url,
        headers=headers,
        auth=auth,
        transport=httpx.MockTransport(handler),
    )
    return client


def admin_client(handler: Handler, **kwargs: Any) -> AtlasAdminClient:
    kwargs = kwargs or {"public_key": "public", "private_key": "private"}
    return attach_transport(AtlasAdminClient(**kwargs), handler)


def oauth_client(handler: Handler, **kwargs: Any) -> AtlasAdminClient:
    kwargs = kwargs or {"client_id": "id", "client_secret": "secret"}
    return attach_transport(AtlasAdminClient(**kwargs), handler)


def app_client(handler: Handler, token: str = "token") -> AtlasAppAdminClient:
    return attach_transport(AtlasAppAdminClient(access_token=token), handler)


def status_client(handler: Handler) -> AtlasStatusClient:
    return attach_transport(AtlasStatusClient(), handler)


CLIENT_FACTORIES = {
    "admin": admin_client,
    "app": app_client,
    "status": status_client,
}


@pytest.fixture(params=sorted(CLIENT_FACTORIES))
def package(request: pytest.FixtureRequest) -> str:
    """Name of each generated package; used to run shared behavior against all three clients."""
    return request.param


@pytest.fixture
def recorder() -> Recorder:
    return Recorder()


@pytest.fixture
def make_client(package: str, recorder: Recorder) -> Callable[[], Any]:
    """Build a client for the current ``package`` parameter wired to ``recorder``."""
    return lambda: CLIENT_FACTORIES[package](recorder)


_ATLAS_ENV_VARS = (
    "MONGO_ATLAS_PUBLIC_KEY",
    "MONGO_ATLAS_PRIVATE_KEY",
    "MONGO_ATLAS_CLIENT_ID",
    "MONGO_ATLAS_CLIENT_SECRET",
    "MONGO_ATLAS_ACCESS_TOKEN",
    "MONGO_ATLAS_BASE_URL",
    "MONGO_ATLAS_OAUTH_TOKEN_URL",
    "MONGO_ATLAS_APP_BASE_URL",
    "MONGO_ATLAS_STATUS_BASE_URL",
)


@pytest.fixture(autouse=True)
def _clear_atlas_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep a developer's local .env from changing test behavior."""
    for name in _ATLAS_ENV_VARS:
        monkeypatch.delenv(name, raising=False)
