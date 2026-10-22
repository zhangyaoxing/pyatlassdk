"""Generated model for UserCustomDBRole. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.database_inherited_role import DatabaseInheritedRole
from pyatlassdk.models.database_privilege_action import DatabasePrivilegeAction

from pydantic import BaseModel, ConfigDict, Field

class UserCustomDBRole(BaseModel):
    """Generated model for UserCustomDBRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    actions: list[DatabasePrivilegeAction] | None = Field(default=None, description="List of the individual privilege actions that the role grants.")
    inherited_roles: list[DatabaseInheritedRole] | None = Field(default=None, alias="inheritedRoles", description="List of the built-in roles that this custom role inherits.")
    role_name: str = Field(alias="roleName", description="Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.")
