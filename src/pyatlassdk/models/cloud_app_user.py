"""Generated model for CloudAppUser. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.cloud_access_role_assignment import CloudAccessRoleAssignment
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class CloudAppUser(BaseModel):
    """Generated model for CloudAppUser."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    country: str = Field(description="Two alphabet characters that identifies MongoDB Cloud user's geographic location. This parameter uses the ISO 3166-1a2 code format.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when the current account is created. This value is in the ISO 8601 timestamp format in UTC.")
    email_address: str = Field(alias="emailAddress", description="Email address that belongs to the MongoDB Cloud user.")
    first_name: str = Field(alias="firstName", description="First or given name that belongs to the MongoDB Cloud user.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.")
    last_auth: datetime | None = Field(default=None, alias="lastAuth", description="Date and time when the current account last authenticated. This value is in the ISO 8601 timestamp format in UTC.")
    last_name: str = Field(alias="lastName", description="Last name, family name, or surname that belongs to the MongoDB Cloud user.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    mobile_number: str = Field(alias="mobileNumber", description="Mobile phone number that belongs to the MongoDB Cloud user.")
    password: str = Field(description="Password applied with the username to log in to MongoDB Cloud. MongoDB Cloud does not return this parameter except in response to creating a new MongoDB Cloud user. Only the MongoDB Cloud user can update their password after it has been set from the MongoDB Cloud console.")
    roles: list[CloudAccessRoleAssignment] = Field(description="List of objects that display the MongoDB Cloud user's roles and the corresponding organization or project to which that role applies. A role can apply to one organization or one project but not both.")
    team_ids: list[str] | None = Field(default=None, alias="teamIds", description="List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.")
    username: str = Field(description="Email address that represents the username of the MongoDB Cloud user.")
