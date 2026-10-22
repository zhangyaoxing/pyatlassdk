"""Generated model for UserAccessRoleAssignment. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class UserAccessRoleAssignment(BaseModel):
    """Generated model for UserAccessRoleAssignment."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: list[str] | None = Field(default=None, description="List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project.")
    user_id: str | None = Field(default=None, alias="userId", description="Unique 24-hexadecimal digit string that identifies the organization API key.")
