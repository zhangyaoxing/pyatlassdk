"""Generated model for FlexProviderSettings20241113. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexProviderSettings20241113(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    backing_provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the flex cluster.")
    disk_size_gb: float | None = Field(default=None, alias="diskSizeGB", description="Storage capacity available to the flex cluster expressed in gigabytes.")
    provider_name: Annotated[Literal["FLEX"], BeforeValidator(upper_case)] | None = Field(default=None, alias="providerName", description="Human-readable label that identifies the provider type.")
    region_name: str | None = Field(default=None, alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB flex cluster. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).")
