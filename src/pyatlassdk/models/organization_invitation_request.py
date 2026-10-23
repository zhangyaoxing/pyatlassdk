"""Generated model for OrganizationInvitationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.organization_invitation_group_role_assignments_request import OrganizationInvitationGroupRoleAssignmentsRequest

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrganizationInvitationRequest(BaseModel):
    """Generated model for OrganizationInvitationRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_role_assignments: list[OrganizationInvitationGroupRoleAssignmentsRequest] | None = Field(default=None, alias="groupRoleAssignments", description="List of projects that the user will be added to when they accept their invitation to the organization.")
    roles: list[Annotated[Literal["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY"], BeforeValidator(upper_case)]] | None = Field(default=None, description="One or more organization level roles to assign to the MongoDB Cloud user.")
    team_ids: list[str] | None = Field(default=None, alias="teamIds", description="List of teams to which you want to invite the desired MongoDB Cloud user.")
    username: str | None = Field(default=None, description="Email address that belongs to the desired MongoDB Cloud user.")
