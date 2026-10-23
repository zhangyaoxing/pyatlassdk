"""Generated model for AuthenticatedUser. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthenticatedUser(BaseModel):
    """Details about the MongoDB Cloud user that this request is authenticated as."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    username: str | None = Field(default=None, description="Email address that represents the username of the MongoDB Cloud user.")
