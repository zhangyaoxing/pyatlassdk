"""Generated model for ClusterCloudProviderInstanceSize. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.available_cloud_provider_region import AvailableCloudProviderRegion

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterCloudProviderInstanceSize(BaseModel):
    """Generated model for ClusterCloudProviderInstanceSize."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    available_regions: list[AvailableCloudProviderRegion] | None = Field(default=None, alias="availableRegions", description="List of regions that this cloud provider supports for this instance size.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the instance size or cluster tier.")
