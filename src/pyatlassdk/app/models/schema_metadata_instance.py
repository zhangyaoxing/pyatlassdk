"""Generated model for SchemaMetadataInstance. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.schema_metadata import SchemaMetadata

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SchemaMetadataInstance(BaseModel):
    """Generated model for SchemaMetadataInstance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(alias="_id")
    metadata: SchemaMetadata
