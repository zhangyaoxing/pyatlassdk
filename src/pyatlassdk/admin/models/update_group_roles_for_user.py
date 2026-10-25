"""Generated model for UpdateGroupRolesForUser. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UpdateGroupRolesForUser(BaseModel):
    """Generated model for UpdateGroupRolesForUser."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_roles: list[str] | None = Field(default=None, alias="groupRoles", description="One or more project-level roles to assign to the MongoDB Cloud user.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
