"""Generated model for AvailableCloudProviderRegion. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AvailableCloudProviderRegion(BaseModel):
    """Generated model for AvailableCloudProviderRegion."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    default: bool | None = Field(default=None, description="Flag that indicates whether the cloud provider sets this region as its default. AWS defaults to `US_EAST_1`, GCP defaults to `CENTRAL_US`, and AZURE defaults to `US_WEST_2`.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the supported region.")
