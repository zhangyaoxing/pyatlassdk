"""Generated model for FlexConnectionStrings20241113. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class FlexConnectionStrings20241113(BaseModel):
    """Collection of Uniform Resource Locators that point to the MongoDB database."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    standard: str | None = Field(default=None, description="Public connection string that you can use to connect to this cluster. This connection string uses the `mongodb://` protocol.")
    standard_srv: str | None = Field(default=None, alias="standardSrv", description="Public connection string that you can use to connect to this flex cluster. This connection string uses the `mongodb+srv://` protocol.")
