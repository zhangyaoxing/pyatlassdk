"""Generated model for OrgUserRolesRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.group_role_assignment import GroupRoleAssignment

from pydantic import BaseModel, ConfigDict, Field

class OrgUserRolesRequest(BaseModel):
    """Organization and project level roles to assign the MongoDB Cloud user within one organization."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_role_assignments: list[GroupRoleAssignment] | None = Field(default=None, alias="groupRoleAssignments", description="List of project level role assignments to assign the MongoDB Cloud user.")
    org_roles: list[Literal["ORG_OWNER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY", "ORG_MEMBER"]] = Field(alias="orgRoles", description="One or more organization level roles to assign the MongoDB Cloud user.")
