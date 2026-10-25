"""Generated model for UpdateCustomDBRole. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.database_inherited_role import DatabaseInheritedRole
from pyatlassdk.admin.models.database_privilege_action import DatabasePrivilegeAction

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UpdateCustomDBRole(BaseModel):
    """Generated model for UpdateCustomDBRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    actions: list[DatabasePrivilegeAction] | None = Field(default=None, description="List of the individual privilege actions that the role grants.")
    inherited_roles: list[DatabaseInheritedRole] | None = Field(default=None, alias="inheritedRoles", description="List of the built-in roles that this custom role inherits.")
