"""Generated model for AdminUserRolesItem. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdminUserRolesItem(BaseModel):
    """Generated model for AdminUserRolesItem."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    role_name: str | None = None
    group_id: str | None = None
