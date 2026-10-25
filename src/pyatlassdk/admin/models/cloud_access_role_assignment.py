"""Generated model for CloudAccessRoleAssignment. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudAccessRoleAssignment(BaseModel):
    """MongoDB Cloud user's roles and the corresponding organization or project to which that role applies. Each role can apply to one organization or one project but not both."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to which this role belongs. You can set a value for this parameter or `orgId` but not both in the same request.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which this role belongs. You can set a value for this parameter or `groupId` but not both in the same request.")
    role_name: str | None = Field(default=None, alias="roleName", description="Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team. These roles include organization- and project-level roles.")
