"""Generated model for AzureKeyVaultEARPrivateEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AzureKeyVaultEARPrivateEndpoint(BaseModel):
    """Azure Key Vault Encryption At Rest Private Endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AZURE", "AWS"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider for the Encryption At Rest private endpoint.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message for failures associated with the Encryption At Rest private endpoint.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the Private Endpoint Service.")
    private_endpoint_connection_name: str | None = Field(default=None, alias="privateEndpointConnectionName", description="Connection name of the Azure Private Endpoint.")
    region_name: Annotated[Literal["US_CENTRAL", "US_EAST", "US_EAST_2", "US_NORTH_CENTRAL", "US_WEST", "US_SOUTH_CENTRAL", "EUROPE_NORTH", "EUROPE_WEST", "US_WEST_CENTRAL", "US_WEST_2", "US_WEST_3", "CANADA_EAST", "CANADA_CENTRAL", "BRAZIL_SOUTH", "BRAZIL_SOUTHEAST", "AUSTRALIA_CENTRAL", "AUSTRALIA_CENTRAL_2", "AUSTRALIA_EAST", "AUSTRALIA_SOUTH_EAST", "GERMANY_WEST_CENTRAL", "GERMANY_NORTH", "SWEDEN_CENTRAL", "SWEDEN_SOUTH", "SWITZERLAND_NORTH", "SWITZERLAND_WEST", "UK_SOUTH", "UK_WEST", "NORWAY_EAST", "NORWAY_WEST", "INDIA_CENTRAL", "INDIA_SOUTH", "INDIA_WEST", "CHINA_EAST", "CHINA_NORTH", "ASIA_EAST", "JAPAN_EAST", "JAPAN_WEST", "ASIA_SOUTH_EAST", "KOREA_CENTRAL", "KOREA_SOUTH", "FRANCE_CENTRAL", "FRANCE_SOUTH", "SOUTH_AFRICA_NORTH", "SOUTH_AFRICA_WEST", "UAE_CENTRAL", "UAE_NORTH", "QATAR_CENTRAL", "POLAND_CENTRAL", "ISRAEL_CENTRAL", "ITALY_NORTH", "SPAIN_CENTRAL", "MEXICO_CENTRAL", "NEW_ZEALAND_NORTH", "US_GOV_VIRGINIA", "US_GOV_ARIZONA", "US_GOV_TEXAS"], BeforeValidator(upper_case)] | Annotated[Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "EU_CENTRAL_2", "AP_EAST_1", "AP_EAST_2", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTHEAST_4", "AP_SOUTHEAST_5", "AP_SOUTHEAST_6", "AP_SOUTHEAST_7", "AP_SOUTH_1", "AP_SOUTH_2", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "ME_CENTRAL_1", "AF_SOUTH_1", "EU_SOUTH_1", "EU_SOUTH_2", "IL_CENTRAL_1", "CA_WEST_1", "MX_CENTRAL_1", "GLOBAL"], BeforeValidator(upper_case)] | None = Field(default=None, alias="regionName", description="Cloud provider region in which the Encryption At Rest private endpoint is located.")
    status: Annotated[Literal["INITIATING", "PENDING_ACCEPTANCE", "ACTIVE", "FAILED", "PENDING_RECREATION", "DELETING"], BeforeValidator(upper_case)] | None = Field(default=None, description="State of the Encryption At Rest private endpoint.")
