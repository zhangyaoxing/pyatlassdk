"""Generated model for DataSource. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.atlas_cluster import AtlasCluster
from pyatlassdk.app.models.atlas_federated_instance import AtlasFederatedInstance

DataSource: TypeAlias = AtlasCluster | AtlasFederatedInstance
