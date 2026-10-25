"""Generated model for GroupInvitationRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupInvitationRequest(BaseModel):
    """Generated model for GroupInvitationRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: list[str] | None = Field(default=None, description="One or more project level roles to assign to the MongoDB Cloud user.")
    username: str | None = Field(default=None, description="Email address of the MongoDB Cloud user invited to the specified project.")
