"""Generated model for CreateOrgMcpConfigRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry

from pydantic import BaseModel, ConfigDict, Field

class CreateOrgMcpConfigRequest(BaseModel):
    """Generated model for CreateOrgMcpConfigRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ip_access_list: list[ServiceAccountIPAccessListEntry] | None = Field(default=None, alias="ipAccessList", description="List of IP access list entries that define allowed source addresses for this MCP configuration.")
    mcp_config_name: str = Field(alias="mcpConfigName", description="Human-readable name that identifies this MCP configuration.")
    roles: list[Literal["ORG_MEMBER", "ORG_READ_ONLY", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_GROUP_CREATOR", "ORG_OWNER"]] = Field(description="List of organization roles to assign to this MCP configuration.")
