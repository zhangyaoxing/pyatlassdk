"""Generated model for GroupInvitationUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class GroupInvitationUpdateRequest(BaseModel):
    """Generated model for GroupInvitationUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: list[str] | None = Field(default=None, description="One or more project-level roles to assign to the MongoDB Cloud user.")
