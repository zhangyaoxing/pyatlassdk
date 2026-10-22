"""Generated model for OrgDelegationSettingsUpdateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class OrgDelegationSettingsUpdateRequest(BaseModel):
    """Generated model for OrgDelegationSettingsUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delegated_mcp_access: Literal["DISALLOWED", "READ_ONLY", "READ_WRITE"] | None = Field(default=None, alias="delegatedMcpAccess", description="Policy that controls how MCP (Model Context Protocol) delegated access is permitted within this organization. Possible values are `DISALLOWED`, `READ_ONLY`, and `READ_WRITE`. Defaults to `DISALLOWED`.")
    delegated_partner_access: Literal["DISALLOWED", "READ_WRITE"] | None = Field(default=None, alias="delegatedPartnerAccess", description="Policy that controls whether partner delegated access is permitted within this organization. Possible values are `DISALLOWED` and `READ_WRITE`. Defaults to `DISALLOWED`.")
    idle_refresh_token_lifetime: int | None = Field(default=None, alias="idleRefreshTokenLifetime", description="Maximum number of seconds a refresh token may be idle before it expires. Omit to leave unchanged; set to null to reset to the system default. Must be between 1 and 31536000 (1 year) when provided.")
    maximum_refresh_token_lifetime: int | None = Field(default=None, alias="maximumRefreshTokenLifetime", description="Maximum lifetime of a refresh token in seconds, regardless of activity. Omit to leave unchanged; set to null to reset to the system default. Must be between 1 and 31536000 (1 year) when provided.")
