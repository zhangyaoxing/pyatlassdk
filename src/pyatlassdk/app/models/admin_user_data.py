"""Generated model for AdminUserData. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdminUserData(BaseModel):
    """Generated model for AdminUserData."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    email: str | None = None
    name: str | None = None
