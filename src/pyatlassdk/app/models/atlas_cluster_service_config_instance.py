"""Generated model for AtlasClusterServiceConfigInstance. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasClusterServiceConfigInstance(BaseModel):
    """Generated model for AtlasClusterServiceConfigInstance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_id: float | None = Field(default=None, alias="clusterId", description="The service ID.")
    group_name: str | None = Field(default=None, alias="groupName", description="The name of the group that contains the service.")
    org_name: str | None = Field(default=None, alias="orgName", description="The name of the organization that contains the service.")
