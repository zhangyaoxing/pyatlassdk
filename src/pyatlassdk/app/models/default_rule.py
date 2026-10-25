"""Generated model for DefaultRule. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.filter_constructor import FilterConstructor
from pyatlassdk.app.models.role_constructor import RoleConstructor

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DefaultRule(BaseModel):
    """A data access rule that define defines fallback user roles and query filters for collection's that don't have more specific permissions defined."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The default rule's unique ObjectId identifier.")
    roles: list[RoleConstructor] | None = Field(default=None, description="An ordered list of default user roles.")
    filters: list[FilterConstructor] | None = Field(default=None, description="A list of default [query filters](https://www.mongodb.com/docs/atlas/app-services/reference/config/data_sources/#filters).")
