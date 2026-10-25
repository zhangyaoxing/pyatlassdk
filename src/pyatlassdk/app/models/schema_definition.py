"""Generated model for SchemaDefinition. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SchemaDefinition(BaseModel):
    """A valid [schema](https://www.mongodb.com/docs/atlas/app-services/schemas) for the collection."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    bson_type: Literal["object", "array", "string", "number", "int", "long", "double", "decimal", "date", "timestamp", "bool", "null", "regex", "objectId", "binary", "uuid", "function", "javascript", "symbol", "minKey", "maxKey"] | None = Field(default=None, alias="bsonType", description="The [BSON type](https://www.mongodb.com/docs/atlas/app-services/schemas/types/#std-label-schema-types) of the field.")
    title: str | None = Field(default=None, description="A human-readable title for the schema.")
    required: list[str] | None = Field(default=None, description="For `object` schemas, an array of field names that are\nrequired in instances of the object.")
    properties: dict[str, SchemaDefinition] | None = Field(default=None, description="An object where each field name is a property in the schema.\nThe corresponding value is a\n[schema](https://www.mongodb.com/docs/atlas/app-services/schemas/types/#std-label-schema-types)\ndefinition for that field.")

SchemaDefinition.model_rebuild()
