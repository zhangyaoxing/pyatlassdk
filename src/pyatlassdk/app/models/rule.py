"""Generated model for Rule. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.filter_constructor import FilterConstructor
from pyatlassdk.app.models.role_constructor import RoleConstructor

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Rule(BaseModel):
    """A data access rule that defines user roles and query filters for a collection in a linked data source."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The rule's unique ObjectId identifier.")
    roles: list[RoleConstructor] | None = Field(default=None, description="A list of data access roles.")
    filters: list[FilterConstructor] | None = Field(default=None, description="A list of filters for incoming operations.")
    database: str = Field(description="The name of a database in the linked data source.")
    collection: str = Field(description="The name of a collection in the specified `database`.")
