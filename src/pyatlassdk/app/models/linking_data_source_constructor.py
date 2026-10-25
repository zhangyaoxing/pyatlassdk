"""Generated model for LinkingDataSourceConstructor. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.linking_data_source_config import LinkingDataSourceConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LinkingDataSourceConstructor(BaseModel):
    """Generated model for LinkingDataSourceConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Create a name to identify each cluster you want to link.")
    type: Literal["mongodb-atlas", "datalake"] | None = Field(default=None, description="The type of the data source you want to link. ")
    config: LinkingDataSourceConfig | None = None
