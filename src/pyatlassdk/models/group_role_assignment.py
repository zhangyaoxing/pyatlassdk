"""Generated model for GroupRoleAssignment. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class GroupRoleAssignment(BaseModel):
    """Generated model for GroupRoleAssignment."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to which these roles belong.")
    group_roles: list[str] | None = Field(default=None, alias="groupRoles", description="One or more project-level roles assigned to the MongoDB Cloud user.")
