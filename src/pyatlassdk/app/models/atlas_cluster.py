"""Generated model for AtlasCluster. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.atlas_cluster_service_config_instance import AtlasClusterServiceConfigInstance

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasCluster(BaseModel):
    """Generated model for AtlasCluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The cluster's unique ID.")
    config: AtlasClusterServiceConfigInstance | None = None
