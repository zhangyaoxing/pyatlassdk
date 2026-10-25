"""Generated model for DataLakeAzureBlobStore. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeAzureBlobStore(BaseModel):
    """Group of settings that define where the data is stored."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the data store. The **databases.[n].collections.[n].dataSources.[n].storeName** field references this values as part of the mapping configuration. To use MongoDB Cloud as a data store, the data lake requires a serverless instance or an `M10` or higher cluster.")
    provider: str
    container_name: str | None = Field(default=None, alias="containerName", description="Human-readable label that identifies the name of the container.")
    delimiter: str | None = Field(default=None, description="Delimiter.")
    prefix: str | None = Field(default=None, description="Prefix.")
    public: bool | None = Field(default=None, description="Flag that indicates whether the blob store is public. If set to `true`, MongoDB Cloud doesn't use the configured Azure service principal to access the blob store. If set to `false`, the configured Azure service principal must include permissions to access the blob store.")
    region: Annotated[Literal["US_CENTRAL", "US_EAST", "US_EAST_2", "US_NORTH_CENTRAL", "US_WEST", "US_SOUTH_CENTRAL", "EUROPE_NORTH", "EUROPE_WEST", "US_WEST_CENTRAL", "US_WEST_2", "US_WEST_3", "CANADA_EAST", "CANADA_CENTRAL", "BRAZIL_SOUTH", "BRAZIL_SOUTHEAST", "AUSTRALIA_CENTRAL", "AUSTRALIA_CENTRAL_2", "AUSTRALIA_EAST", "AUSTRALIA_SOUTH_EAST", "GERMANY_CENTRAL", "GERMANY_NORTH_EAST", "GERMANY_WEST_CENTRAL", "GERMANY_NORTH", "SWEDEN_CENTRAL", "SWEDEN_SOUTH", "SWITZERLAND_NORTH", "SWITZERLAND_WEST", "UK_SOUTH", "UK_WEST", "NORWAY_EAST", "NORWAY_WEST", "INDIA_CENTRAL", "INDIA_SOUTH", "INDIA_WEST", "CHINA_EAST", "CHINA_NORTH", "ASIA_EAST", "JAPAN_EAST", "JAPAN_WEST", "ASIA_SOUTH_EAST", "KOREA_CENTRAL", "KOREA_SOUTH", "FRANCE_CENTRAL", "FRANCE_SOUTH", "SOUTH_AFRICA_NORTH", "SOUTH_AFRICA_WEST", "UAE_CENTRAL", "UAE_NORTH", "QATAR_CENTRAL"], BeforeValidator(upper_case)] | None = Field(default=None, description="Microsoft Azure Regions.")
    replacement_delimiter: str | None = Field(default=None, alias="replacementDelimiter", description="Replacement Delimiter.")
    service_url: str | None = Field(default=None, alias="serviceURL", description="Service URL.")
