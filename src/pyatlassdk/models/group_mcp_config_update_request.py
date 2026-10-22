"""Generated model for GroupMcpConfigUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry

from pydantic import BaseModel, ConfigDict, Field

class GroupMcpConfigUpdateRequest(BaseModel):
    """Generated model for GroupMcpConfigUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ip_access_list: list[ServiceAccountIPAccessListEntry] | None = Field(default=None, alias="ipAccessList", description="List of IP access list entries that define allowed source addresses for this MCP configuration. If provided, replaces the existing IP access list.")
    mcp_config_name: str | None = Field(default=None, alias="mcpConfigName", description="Updated human-readable name for this MCP configuration.")
    roles: list[str] | None = Field(default=None, description="List of project roles associated with this MCP configuration. If provided, replaces the existing list of roles.")
