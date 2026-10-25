"""Generated model for OrgUserRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.org_user_roles_request import OrgUserRolesRequest

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgUserRequest(BaseModel):
    """Generated model for OrgUserRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: OrgUserRolesRequest
    team_ids: list[str] | None = Field(default=None, alias="teamIds", description="List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.")
    username: str = Field(description="Email address that represents the username of the MongoDB Cloud user.")
