"""Generated model for CloudGCPProviderSettings. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.cloud_provider_gcp_auto_scaling import CloudProviderGCPAutoScaling

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudGCPProviderSettings(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB hosts."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: str = Field(alias="providerName")
    auto_scaling: CloudProviderGCPAutoScaling | None = Field(default=None, alias="autoScaling")
    instance_size_name: Annotated[Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M140", "M200", "M250", "M300", "M400", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R600", "M30_GEN_2", "M40_GEN_2", "M50_GEN_2", "M60_GEN_2", "M80_GEN_2", "M140_GEN_2", "M200_GEN_2", "M300_GEN_2", "M700_GEN_2", "R40_GEN_2", "R50_GEN_2", "R60_GEN_2", "R80_GEN_2", "R200_GEN_2", "R300_GEN_2", "R400_GEN_2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster.")
    region_name: Annotated[Literal["EASTERN_US", "EASTERN_US_AW", "US_EAST_4", "US_EAST_4_AW", "US_EAST_5", "US_EAST_5_AW", "US_WEST_2", "US_WEST_2_AW", "US_WEST_3", "US_WEST_3_AW", "US_WEST_4", "US_WEST_4_AW", "US_SOUTH_1", "US_SOUTH_1_AW", "CENTRAL_US", "CENTRAL_US_AW", "WESTERN_US", "WESTERN_US_AW", "NORTH_AMERICA_NORTHEAST_1", "NORTH_AMERICA_NORTHEAST_2", "NORTH_AMERICA_SOUTH_1", "SOUTH_AMERICA_EAST_1", "SOUTH_AMERICA_WEST_1", "WESTERN_EUROPE", "EUROPE_NORTH_1", "EUROPE_WEST_2", "EUROPE_WEST_3", "EUROPE_WEST_4", "EUROPE_WEST_6", "EUROPE_WEST_8", "EUROPE_WEST_9", "EUROPE_WEST_10", "EUROPE_WEST_12", "EUROPE_SOUTHWEST_1", "EUROPE_CENTRAL_2", "MIDDLE_EAST_CENTRAL_1", "MIDDLE_EAST_CENTRAL_2", "MIDDLE_EAST_WEST_1", "AUSTRALIA_SOUTHEAST_1", "AUSTRALIA_SOUTHEAST_2", "AFRICA_SOUTH_1", "EASTERN_ASIA_PACIFIC", "NORTHEASTERN_ASIA_PACIFIC", "SOUTHEASTERN_ASIA_PACIFIC", "ASIA_EAST_2", "ASIA_NORTHEAST_2", "ASIA_NORTHEAST_3", "ASIA_SOUTH_1", "ASIA_SOUTH_2", "ASIA_SOUTHEAST_2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="regionName", description="Google Compute Regions.")
