"""Generated model for ClusterFlexProviderSettings. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterFlexProviderSettings(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB hosts."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: str = Field(alias="providerName")
    backing_provider_name: Annotated[Literal["AWS", "GCP", "AZURE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the multi-tenant host. The resource returns this parameter when `providerSettings.providerName` is `FLEX` and `providerSetting.instanceSizeName` is `FLEX`.")
    instance_size_name: Annotated[Literal["FLEX"], BeforeValidator(upper_case)] | None = Field(default=None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster. You must set `providerSettings.providerName` to `FLEX` and specify the cloud service provider in `providerSettings.backingProviderName`.")
    region_name: str | None = Field(default=None, alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).")
