"""Generated model for OrgPendingUserResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.org_user_roles_response import OrgUserRolesResponse

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgPendingUserResponse(BaseModel):
    """Generated model for OrgPendingUserResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.")
    org_membership_status: Annotated[Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"], BeforeValidator(upper_case)] = Field(alias="orgMembershipStatus", description="String enum that indicates the user's organization membership status: ACTIVE (member), PENDING (invited), `INVITATION_EXPIRED` (invitation expired), or `INVITATION_REJECTED` (invitation declined).")
    roles: OrgUserRolesResponse
    team_ids: list[str] | None = Field(default=None, alias="teamIds", description="List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.")
    username: str = Field(description="Email address that represents the username of the MongoDB Cloud user.")
    invitation_created_at: datetime = Field(alias="invitationCreatedAt", description="Date and time when MongoDB Cloud sent the invitation. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. This field is absent for active users.")
    invitation_expires_at: datetime | None = Field(default=None, alias="invitationExpiresAt", description="Date and time when the invitation from MongoDB Cloud expires. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. This field is absent for active users and null for rejected invitations.")
    inviter_username: str = Field(alias="inviterUsername", description="Username of the MongoDB Cloud user who sent the invitation to join the organization.")
