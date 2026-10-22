"""Generated model for SearchTypeSets. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.basic_db_object import BasicDBObject

from pydantic import BaseModel, ConfigDict, Field

class SearchTypeSets(BaseModel):
    """Type sets for an Atlas Search index definition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="Label that identifies the type set name. Each `typeSets.name` must be unique within the same index definition.")
    types: list[BasicDBObject] = Field(description="List of types associated with the type set. Each type definition must include a `type` field specifying the search field type (`autocomplete`, `boolean`, `date`, `geo`, `number`, `objectId`, `string`, `token`, or `uuid`) and may include additional configuration properties specific to that type.")
