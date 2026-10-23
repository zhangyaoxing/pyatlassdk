"""Generated model for OrgUserUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.org_user_roles_request import OrgUserRolesRequest

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgUserUpdateRequest(BaseModel):
    """Generated model for OrgUserUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: OrgUserRolesRequest | None = None
    team_ids: list[str] | None = Field(default=None, alias="teamIds", description="List of unique 24-hexadecimal digit strings that identifies the teams to assign the MongoDB Cloud user.")
