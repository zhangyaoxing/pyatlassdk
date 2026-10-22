from __future__ import annotations

from pyatlassdk import AtlasClient
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
