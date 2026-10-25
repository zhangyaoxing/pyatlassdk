"""Generated model for DataSourceConstructor. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.atlas_cluster_constructor import AtlasClusterConstructor
from pyatlassdk.app.models.atlas_federated_instance_constructor import AtlasFederatedInstanceConstructor

DataSourceConstructor: TypeAlias = AtlasClusterConstructor | AtlasFederatedInstanceConstructor
