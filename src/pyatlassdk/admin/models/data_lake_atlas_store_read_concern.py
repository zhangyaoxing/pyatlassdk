"""Generated model for DataLakeAtlasStoreReadConcern. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeAtlasStoreReadConcern(BaseModel):
    """MongoDB Cloud cluster read concern, which determines the consistency and isolation properties of the data read from an Atlas cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    level: Annotated[Literal["LOCAL", "MAJORITY", "LINEARIZABLE", "SNAPSHOT", "AVAILABLE"], BeforeValidator(upper_case)] | None = Field(default=None, description="Read Concern level that specifies the consistency and availability of the data read.")
