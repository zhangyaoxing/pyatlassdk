"""Generated model for BiConnector. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class BiConnector(BaseModel):
    """Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether MongoDB Connector for Business Intelligence is enabled on the specified cluster.")
    read_preference: Literal["PRIMARY", "SECONDARY", "ANALYTICS"] | None = Field(default=None, alias="readPreference", description="Data source node designated for the MongoDB Connector for Business Intelligence on MongoDB Cloud. The MongoDB Connector for Business Intelligence on MongoDB Cloud reads data from the primary, secondary, or analytics node based on your read preferences. Defaults to `ANALYTICS` node, or `SECONDARY` if there are no `ANALYTICS` nodes.")
