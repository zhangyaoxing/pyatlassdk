"""Generated model for FlexProviderSettingsCreate20241113. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class FlexProviderSettingsCreate20241113(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    backing_provider_name: Literal["AWS", "AZURE", "GCP"] = Field(alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the flex cluster.")
    disk_size_gb: float | None = Field(default=None, alias="diskSizeGB", description="Storage capacity available to the flex cluster expressed in gigabytes.")
    provider_name: Literal["FLEX"] | None = Field(default=None, alias="providerName", description="Human-readable label that identifies the provider type.")
    region_name: str = Field(alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB flex cluster. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).")
