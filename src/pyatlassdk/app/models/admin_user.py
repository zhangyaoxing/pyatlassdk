"""Generated model for AdminUser. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.admin_user_data import AdminUserData
from pyatlassdk.app.models.admin_user_roles_item import AdminUserRolesItem
from pyatlassdk.app.models.user_identity import UserIdentity

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdminUser(BaseModel):
    """Generated model for AdminUser."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    user_id: str | None = None
    domain_id: str | None = None
    identities: list[UserIdentity] | None = None
    data: AdminUserData | None = None
    type: Literal["normal", "server", "system", "unknown"] | None = None
    roles: list[AdminUserRolesItem] | None = None
