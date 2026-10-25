"""Generated model for AuthProvider. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthProvider(BaseModel):
    """Generated model for AuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The authentication provider's unique ID.")
