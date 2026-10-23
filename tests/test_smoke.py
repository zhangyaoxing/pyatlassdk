from __future__ import annotations

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
    assert connector.model_dump(by_alias=True, exclude_none=True) == {
        "readPreference": "SECONDARY"
    }
