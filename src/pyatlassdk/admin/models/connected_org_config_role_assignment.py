"""Generated model for ConnectedOrgConfigRoleAssignment. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ConnectedOrgConfigRoleAssignment(BaseModel):
    """Generated model for ConnectedOrgConfigRoleAssignment."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to which this role belongs. Each element within `roleAssignments` can have a value for `groupId` or `orgId`, but not both.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which this role belongs. Each element within `roleAssignments` can have a value for `orgId` or `groupId`, but not both.")
    role: str | None = Field(default=None, description="Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team. These roles include organization- and project-level roles.")
