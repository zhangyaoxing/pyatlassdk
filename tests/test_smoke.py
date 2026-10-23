from __future__ import annotations

import json
from datetime import datetime, timezone

import httpx
import pytest

from pyatlassdk import AtlasClient
from pyatlassdk.models.bi_connector import BiConnector
from pyatlassdk.models.cluster_description20240805 import ClusterDescription20240805


def test_model_serializes_with_aliases() -> None:
    cluster = ClusterDescription20240805(name="demo", cluster_type="SHARDED")

    assert cluster.model_dump(by_alias=True, exclude_none=True) == {
        "clusterType": "SHARDED",
        "name": "demo",
    }


def test_client_exposes_resources() -> None:
    with AtlasClient(public_key="public", private_key="private") as client:
        assert client.clusters is not None
        assert client.alerts is not None


def test_client_supports_digest_credentials() -> None:
    with AtlasClient(public_key="public", private_key="private") as client:
        assert client.auth_mode == "digest"


def test_client_supports_oauth2_credentials() -> None:
    with AtlasClient(client_id="client-id", client_secret="client-secret") as client:
        assert client.auth_mode == "oauth2"


def test_client_rejects_partial_credentials() -> None:
    with pytest.raises(ValueError):
        AtlasClient(client_id="client-id")


def test_uppercase_enums_accept_any_casing() -> None:
    connector = BiConnector(read_preference="secondary")

    assert connector.read_preference == "SECONDARY"
    assert connector.model_dump(by_alias=True, exclude_none=True) == {"readPreference": "SECONDARY"}


def test_datetime_values_are_json_encoded() -> None:
    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    client = AtlasClient(public_key="public", private_key="private")
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
