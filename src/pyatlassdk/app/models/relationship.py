"""Generated model for Relationship. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Relationship(BaseModel):
    """A [relationship](https://www.mongodb.com/docs/atlas/app-services/schemas/relationships/) definition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ref: str | None = Field(default=None, description="A reference string for the foreign collection.")
    foreign_key: str | None = Field(default=None, description="The name of the field in the foreign collection that the relationship points to.")
    is_list: bool | None = Field(default=None, description="If `true`:\n\n- the relationship may point to many foreign documents.\n- the local field must be defined as an array in the collection schema.")
