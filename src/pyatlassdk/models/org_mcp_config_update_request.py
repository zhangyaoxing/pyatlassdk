"""Generated model for OrgMcpConfigUpdateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry

from pydantic import BaseModel, ConfigDict, Field

class OrgMcpConfigUpdateRequest(BaseModel):
    """Generated model for OrgMcpConfigUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ip_access_list: list[ServiceAccountIPAccessListEntry] | None = Field(default=None, alias="ipAccessList", description="List of IP access list entries that define allowed source addresses for this MCP configuration. If provided, replaces the existing IP access list.")
    mcp_config_name: str | None = Field(default=None, alias="mcpConfigName", description="Updated human-readable name for this MCP configuration.")
    roles: list[Literal["ORG_MEMBER", "ORG_READ_ONLY", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_GROUP_CREATOR", "ORG_OWNER"]] | None = Field(default=None, description="List of organization roles associated with this MCP configuration. If provided, replaces the existing list of roles.")
