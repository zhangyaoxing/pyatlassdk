"""Generated model for DataLakeDLSGCPStore. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeDLSGCPStore(BaseModel):
    """Group of settings that define where the data is stored."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the data store. The **databases.[n].collections.[n].dataSources.[n].storeName** field references this values as part of the mapping configuration. To use MongoDB Cloud as a data store, the data lake requires a serverless instance or an `M10` or higher cluster.")
    provider: str
    region: Annotated[Literal["ASIA_EAST_2", "ASIA_NORTHEAST_2", "ASIA_NORTHEAST_3", "ASIA_SOUTH_1", "ASIA_SOUTH_2", "ASIA_SOUTHEAST_2", "AUSTRALIA_SOUTHEAST_1", "AUSTRALIA_SOUTHEAST_2", "CENTRAL_US", "EASTERN_ASIA_PACIFIC", "EASTERN_US", "EUROPE_CENTRAL_2", "EUROPE_NORTH_1", "EUROPE_WEST_2", "EUROPE_WEST_3", "EUROPE_WEST_4", "EUROPE_WEST_6", "EUROPE_WEST_10", "EUROPE_WEST_12", "MIDDLE_EAST_CENTRAL_1", "MIDDLE_EAST_CENTRAL_2", "MIDDLE_EAST_WEST_1", "NORTH_AMERICA_NORTHEAST_1", "NORTH_AMERICA_NORTHEAST_2", "NORTHEASTERN_ASIA_PACIFIC", "SOUTH_AMERICA_EAST_1", "SOUTH_AMERICA_WEST_1", "SOUTHEASTERN_ASIA_PACIFIC", "US_EAST_4", "US_EAST_5", "US_WEST_2", "US_WEST_3", "US_WEST_4", "US_SOUTH_1", "WESTERN_EUROPE", "WESTERN_US"], BeforeValidator(upper_case)] | None = Field(default=None, description="Google Cloud Platform Regions.")
