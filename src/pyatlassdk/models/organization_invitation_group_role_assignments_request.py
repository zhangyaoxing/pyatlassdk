"""Generated model for OrganizationInvitationGroupRoleAssignmentsRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class OrganizationInvitationGroupRoleAssignmentsRequest(BaseModel):
    """Generated model for OrganizationInvitationGroupRoleAssignmentsRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to which these roles belong.")
    roles: list[str] | None = Field(default=None, description="One or more project-level roles to assign to the MongoDB Cloud user.")
