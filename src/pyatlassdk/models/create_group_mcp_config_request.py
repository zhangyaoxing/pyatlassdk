"""Generated model for CreateGroupMcpConfigRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CreateGroupMcpConfigRequest(BaseModel):
    """Generated model for CreateGroupMcpConfigRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ip_access_list: list[ServiceAccountIPAccessListEntry] | None = Field(default=None, alias="ipAccessList", description="List of IP access list entries that define allowed source addresses for this MCP configuration.")
    mcp_config_name: str = Field(alias="mcpConfigName", description="Human-readable name that identifies this MCP configuration.")
    roles: list[str] = Field(description="List of project roles to assign to this MCP configuration.")
