"""Generated model for AtlasClusterServiceConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.atlas_cluster_service_config_instance import AtlasClusterServiceConfigInstance

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasClusterServiceConstructor(BaseModel):
    """Generated model for AtlasClusterServiceConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: AtlasClusterServiceConfigInstance | None = None
