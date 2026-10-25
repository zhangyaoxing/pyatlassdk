"""Generated model for OrganizationInvitation. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.group_role import GroupRole
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrganizationInvitation(BaseModel):
    """Generated model for OrganizationInvitation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when MongoDB Cloud sent the invitation. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    expires_at: datetime | None = Field(default=None, alias="expiresAt", description="Date and time when the invitation from MongoDB Cloud expires. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    group_role_assignments: list[GroupRole] | None = Field(default=None, alias="groupRoleAssignments", description="List of projects that the user will be added to when they accept their invitation to the organization.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this invitation.")
    inviter_username: str | None = Field(default=None, alias="inviterUsername", description="Email address of the MongoDB Cloud user who sent the invitation to join the organization.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization.")
    org_name: str = Field(alias="orgName", description="Human-readable label that identifies this organization.")
    roles: list[Annotated[Literal["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY"], BeforeValidator(upper_case)]] | None = Field(default=None, description="One or more organization-level roles to assign to the MongoDB Cloud user.")
    team_ids: list[str] | None = Field(default=None, alias="teamIds", description="List of unique 24-hexadecimal digit strings that identifies each team.")
    username: str | None = Field(default=None, description="Email address of the MongoDB Cloud user invited to join the organization.")
