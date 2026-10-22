"""Generated model for ServerlessProviderSettings. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.base_cloud_provider_instance_size import BaseCloudProviderInstanceSize

from pydantic import BaseModel, ConfigDict, Field

class ServerlessProviderSettings(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB serverless instance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    backing_provider_name: Literal["AWS", "AZURE", "GCP"] = Field(alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the serverless instance.")
    effective_disk_size_gb_limit: int | None = Field(default=None, alias="effectiveDiskSizeGBLimit", description="Storage capacity of instance data volumes expressed in gigabytes. This value is not configurable for Serverless or effectively Flex clusters.")
    effective_instance_size_name: BaseCloudProviderInstanceSize | None = Field(default=None, alias="effectiveInstanceSizeName")
    effective_provider_name: str | None = Field(default=None, alias="effectiveProviderName", description="Cloud service provider on which MongoDB Cloud effectively provisioned the serverless instance.")
    provider_name: Literal["SERVERLESS"] | None = Field(default=None, alias="providerName", description="Human-readable label that identifies the cloud service provider.")
    region_name: str = Field(alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB serverless instance. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).")
