"""Generated model for GroupInvitation. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class GroupInvitation(BaseModel):
    """Generated model for GroupInvitation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when MongoDB Cloud sent the invitation. This parameter expresses its value in ISO 8601 format in UTC.")
    expires_at: datetime | None = Field(default=None, alias="expiresAt", description="Date and time when MongoDB Cloud expires the invitation. This parameter expresses its value in ISO 8601 format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    group_name: str | None = Field(default=None, alias="groupName", description="Human-readable label that identifies the project to which you invited the MongoDB Cloud user.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies the invitation.")
    inviter_username: str | None = Field(default=None, alias="inviterUsername", description="Email address of the MongoDB Cloud user who sent the invitation.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    roles: list[str] | None = Field(default=None, description="One or more organization or project level roles to assign to the MongoDB Cloud user.")
    username: str | None = Field(default=None, description="Email address of the MongoDB Cloud user invited to join the project.")
