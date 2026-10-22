"""Generated model for AzureCloudProviderSettings. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.cloud_provider_azure_auto_scaling import CloudProviderAzureAutoScaling

from pydantic import BaseModel, ConfigDict, Field

class AzureCloudProviderSettings(BaseModel):
    """Group of cloud provider settings that configure the provisioned MongoDB hosts."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: str = Field(alias="providerName")
    auto_scaling: CloudProviderAzureAutoScaling | None = Field(default=None, alias="autoScaling")
    disk_type_name: Literal["P2", "P3", "P4", "P6", "P10", "P15", "P20", "P30", "P40", "P50"] | None = Field(default=None, alias="diskTypeName", description="Disk type that corresponds to the host's root volume for Azure instances. If omitted, the default disk type for the selected `providerSettings.instanceSizeName` applies.")
    instance_size_name: Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M90", "M200", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "M60_NVME", "M80_NVME", "M200_NVME", "M300_NVME", "M400_NVME", "M600_NVME"] | None = Field(default=None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster.")
    region_name: Literal["US_CENTRAL", "US_EAST", "US_EAST_2", "US_NORTH_CENTRAL", "US_WEST", "US_SOUTH_CENTRAL", "EUROPE_NORTH", "EUROPE_WEST", "US_WEST_CENTRAL", "US_WEST_2", "US_WEST_3", "CANADA_EAST", "CANADA_CENTRAL", "BRAZIL_SOUTH", "BRAZIL_SOUTHEAST", "AUSTRALIA_CENTRAL", "AUSTRALIA_CENTRAL_2", "AUSTRALIA_EAST", "AUSTRALIA_SOUTH_EAST", "GERMANY_WEST_CENTRAL", "GERMANY_NORTH", "SWEDEN_CENTRAL", "SWEDEN_SOUTH", "SWITZERLAND_NORTH", "SWITZERLAND_WEST", "UK_SOUTH", "UK_WEST", "NORWAY_EAST", "NORWAY_WEST", "INDIA_CENTRAL", "INDIA_SOUTH", "INDIA_WEST", "CHINA_EAST", "CHINA_NORTH", "ASIA_EAST", "JAPAN_EAST", "JAPAN_WEST", "ASIA_SOUTH_EAST", "KOREA_CENTRAL", "KOREA_SOUTH", "FRANCE_CENTRAL", "FRANCE_SOUTH", "SOUTH_AFRICA_NORTH", "SOUTH_AFRICA_WEST", "UAE_CENTRAL", "UAE_NORTH", "QATAR_CENTRAL", "POLAND_CENTRAL", "ISRAEL_CENTRAL", "ITALY_NORTH", "SPAIN_CENTRAL", "MEXICO_CENTRAL", "NEW_ZEALAND_NORTH", "US_GOV_VIRGINIA", "US_GOV_ARIZONA", "US_GOV_TEXAS"] | None = Field(default=None, alias="regionName", description="Microsoft Azure Regions.")
