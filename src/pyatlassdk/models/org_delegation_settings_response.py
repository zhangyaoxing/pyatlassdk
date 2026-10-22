"""Generated model for OrgDelegationSettingsResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class OrgDelegationSettingsResponse(BaseModel):
    """Generated model for OrgDelegationSettingsResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delegated_mcp_access: Literal["DISALLOWED", "READ_ONLY", "READ_WRITE"] | None = Field(default=None, alias="delegatedMcpAccess", description="Policy that controls how MCP (Model Context Protocol) delegated access is permitted within this organization. Possible values are `DISALLOWED`, `READ_ONLY`, and `READ_WRITE`. Defaults to `DISALLOWED`.")
    delegated_partner_access: Literal["DISALLOWED", "READ_WRITE"] | None = Field(default=None, alias="delegatedPartnerAccess", description="Policy that controls whether partner delegated access is permitted within this organization. Possible values are `DISALLOWED` and `READ_WRITE`. Defaults to `DISALLOWED`.")
    idle_refresh_token_lifetime: int | None = Field(default=None, alias="idleRefreshTokenLifetime", description="Maximum number of seconds a refresh token may be idle before it expires. When not set, the system default applies.")
    maximum_refresh_token_lifetime: int | None = Field(default=None, alias="maximumRefreshTokenLifetime", description="Maximum lifetime of a refresh token in seconds, regardless of activity. When not set, the system default applies.")
