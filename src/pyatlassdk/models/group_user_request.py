"""Generated model for GroupUserRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class GroupUserRequest(BaseModel):
    """Generated model for GroupUserRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: list[str] = Field(description="One or more project-level roles to assign the MongoDB Cloud user.")
    username: str = Field(description="Email address that represents the username of the MongoDB Cloud user.")
