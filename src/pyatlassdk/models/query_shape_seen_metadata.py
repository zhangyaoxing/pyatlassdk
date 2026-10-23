"""Generated model for QueryShapeSeenMetadata. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class QueryShapeSeenMetadata(BaseModel):
    """Metadata about when a query shape was seen."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    application_name: str | None = Field(default=None, alias="applicationName", description="The name of the application that this query shape came from. This can be set via the MongoDB connection string. The application name is set to unknown for internal MongoDB queries.")
    driver_name: str | None = Field(default=None, alias="driverName", description="The name of the MongoDB driver that this query shape was executed from. The driver name is set to unknown for internal MongoDB queries.")
    driver_version: str | None = Field(default=None, alias="driverVersion", description="The version of the MongoDB driver that this query shape was executed from. The driver version is set to unknown for internal MongoDB queries.")
    timestamp: int | None = Field(default=None, description="Unix epoch milliseconds of the time.")
