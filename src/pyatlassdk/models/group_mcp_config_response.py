"""Generated model for GroupMcpConfigResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry

from pydantic import BaseModel, ConfigDict, Field

class GroupMcpConfigResponse(BaseModel):
    """Generated model for GroupMcpConfigResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_id: str | None = Field(default=None, alias="clientId", description="Unique identifier for the Service Account client associated with this MCP configuration. Use this Service Account to connect to the Atlas Remote MCP.")
    egress_client_id: str | None = Field(default=None, alias="egressClientId", description="Unique identifier for the egress Service Account client associated with this MCP configuration. This Service Account is managed by MongoDB Atlas.")
    ip_access_list: list[ServiceAccountIPAccessListEntry] | None = Field(default=None, alias="ipAccessList", description="List of IP access list entries that define allowed source addresses for this MCP configuration.")
    mcp_config_id: str | None = Field(default=None, alias="mcpConfigId", description="Unique identifier that identifies this MCP configuration.")
    mcp_config_name: str | None = Field(default=None, alias="mcpConfigName", description="Human-readable name that identifies this MCP configuration.")
    roles: list[str] | None = Field(default=None, description="List of project roles associated with this MCP configuration.")
