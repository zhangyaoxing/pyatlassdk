from __future__ import annotations

import json
from datetime import datetime, timezone

import httpx
import pytest

from pyatlassdk import AtlasAdminClient, AtlasAppAdminClient
from pyatlassdk.admin.models.bi_connector import BiConnector
from pyatlassdk.admin.models.cluster_description20240805 import ClusterDescription20240805
from pyatlassdk.app.models.anonymous_auth_provider import AnonymousAuthProvider


def test_model_serializes_with_aliases() -> None:
    cluster = ClusterDescription20240805(name="demo", cluster_type="SHARDED")

    assert cluster.model_dump(by_alias=True, exclude_none=True) == {
        "clusterType": "SHARDED",
        "name": "demo",
    }


def test_client_exposes_resources() -> None:
    with AtlasAdminClient(public_key="public", private_key="private") as client:
        assert client.clusters is not None
        assert client.alerts is not None


def test_client_supports_digest_credentials() -> None:
    with AtlasAdminClient(public_key="public", private_key="private") as client:
        assert client.auth_mode == "digest"


def test_client_supports_oauth2_credentials() -> None:
    with AtlasAdminClient(client_id="client-id", client_secret="client-secret") as client:
        assert client.auth_mode == "oauth2"


def test_client_rejects_partial_credentials() -> None:
    with pytest.raises(ValueError):
        AtlasAdminClient(client_id="client-id")


def test_uppercase_enums_accept_any_casing() -> None:
    connector = BiConnector(read_preference="secondary")

    assert connector.read_preference == "SECONDARY"
    assert connector.model_dump(by_alias=True, exclude_none=True) == {"readPreference": "SECONDARY"}


def test_datetime_values_are_json_encoded() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    client = AtlasAdminClient(public_key="public", private_key="private")
    client._http.close()
    client._http = httpx.Client(
        base_url="https://example.test/api/atlas/v2",
        transport=httpx.MockTransport(handler),
    )
    client.clusters.create_group_cluster(
        group_id="g1",
        body=ClusterDescription20240805(
            name="demo",
            create_date=datetime(2026, 1, 1, tzinfo=timezone.utc),
        ),
    )

    payload = json.loads(requests[0].content)
    assert payload["createDate"].startswith("2026-01-01T00:00:00")


def test_app_client_uses_bearer_auth() -> None:
    with AtlasAppAdminClient(access_token="token") as client:
        assert client.auth_mode == "bearer"
        assert client.admin is not None
        assert client._http.headers["authorization"] == "Bearer token"


def test_app_models_are_importable() -> None:
    provider = AnonymousAuthProvider(**_anonymous_provider_payload())

    assert provider.type == "anon-user"


def _anonymous_provider_payload() -> dict[str, object]:
    return {"name": "anon-user", "type": "anon-user", "disabled": False}


def test_app_client_uses_relative_paths() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json=[])

    client = AtlasAppAdminClient(access_token="token")
    client._http.close()
    client._http = httpx.Client(
        base_url="https://services.example/api/admin/v3.0",
        headers={"Authorization": "Bearer token"},
        transport=httpx.MockTransport(handler),
    )
    result = client.apps.admin_list_applications(group_id="g1")

    assert result == []
    assert str(requests[0].url) == "https://services.example/api/admin/v3.0/groups/g1/apps"
    assert requests[0].headers["accept"] == "application/json"
