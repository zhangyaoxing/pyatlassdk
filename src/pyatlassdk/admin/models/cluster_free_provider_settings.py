"""Generated model for ClusterFreeProviderSettings. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.cluster_free_auto_scaling import ClusterFreeAutoScaling

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterFreeProviderSettings(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB hosts."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: str = Field(alias="providerName")
    auto_scaling: ClusterFreeAutoScaling | None = Field(default=None, alias="autoScaling")
    backing_provider_name: Annotated[Literal["AWS", "GCP", "AZURE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the multi-tenant host. The resource returns this parameter when `providerSettings.providerName` is `TENANT` and `providerSetting.instanceSizeName` is `M0`, `M2` or `M5`. \n\nPlease note that using an `instanceSize` of M2 or M5 will create a Flex cluster instead. Support for the `instanceSize` of M2 or M5 will be discontinued in January 2026. We recommend using the Create Flex Cluster API for such configurations moving forward.")
    effective_instance_size_name: Annotated[Literal["FLEX", "M2", "M5", "M0"], BeforeValidator(upper_case)] | None = Field(default=None, alias="effectiveInstanceSizeName", description="The true tenant instance size. This is present to support backwards compatibility for deprecated provider types and/or instance sizes.")
    instance_size_name: Annotated[Literal["M0", "M2", "M5"], BeforeValidator(upper_case)] | None = Field(default=None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster. You must set `providerSettings.providerName` to `TENANT` and specify the cloud service provider in `providerSettings.backingProviderName`.")
    region_name: str | None = Field(default=None, alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/). For multi-region clusters, see `replicationSpec.{region}`.")
