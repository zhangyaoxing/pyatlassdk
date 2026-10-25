"""Generated model for SchemaMetadata. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SchemaMetadata(BaseModel):
    """Metadata that describes which linked collection the schema applies to."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    data_source: str | None = Field(default=None, description="The data source name.")
    database: str | None = Field(default=None, description="The database name.")
    collection: str | None = Field(default=None, description="The collection name.")
