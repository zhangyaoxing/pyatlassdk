"""Generated model for FullSchema. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.schema_definition import SchemaDefinition
from pyatlassdk.app.models.schema_metadata import SchemaMetadata
from pyatlassdk.app.models.schema_relationships import SchemaRelationships

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FullSchema(BaseModel):
    """Generated model for FullSchema."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    metadata: SchemaMetadata | None = None
    schema_: SchemaDefinition | None = Field(default=None, alias="schema")
    relationships: SchemaRelationships | None = None
