"""Generated model for GroupActiveUserResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class GroupActiveUserResponse(BaseModel):
    """Generated model for GroupActiveUserResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.")
    org_membership_status: Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"] = Field(alias="orgMembershipStatus", description="String enum that indicates the user's organization membership status: ACTIVE (member), PENDING (invited), `INVITATION_EXPIRED` (invitation expired), or `INVITATION_REJECTED` (invitation declined).")
    roles: list[str] = Field(description="One or more project-level roles assigned to the MongoDB Cloud user.")
    username: str = Field(description="Email address that represents the username of the MongoDB Cloud user.")
    country: str | None = Field(default=None, description="Two-character alphabetical string that identifies the MongoDB Cloud user's geographic location. This parameter uses the ISO 3166-1a2 code format.")
    created_at: datetime = Field(alias="createdAt", description="Date and time when MongoDB Cloud created the current account. This value is in the ISO 8601 timestamp format in UTC.")
    first_name: str = Field(alias="firstName", description="First or given name that belongs to the MongoDB Cloud user.")
    last_auth: datetime | None = Field(default=None, alias="lastAuth", description="Date and time when the current account last authenticated. This value is in the ISO 8601 timestamp format in UTC.")
    last_name: str = Field(alias="lastName", description="Last name, family name, or surname that belongs to the MongoDB Cloud user.")
    mobile_number: str | None = Field(default=None, alias="mobileNumber", description="Mobile phone number that belongs to the MongoDB Cloud user.")
