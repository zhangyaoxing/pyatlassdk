"""Generated model for OrgMcpConfigResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgMcpConfigResponse(BaseModel):
    """Generated model for OrgMcpConfigResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_id: str | None = Field(default=None, alias="clientId", description="Unique identifier for the Service Account client associated with this MCP configuration. Use this Service Account to connect to the Atlas Remote MCP.")
    egress_client_id: str | None = Field(default=None, alias="egressClientId", description="Unique identifier for the egress Service Account client associated with this MCP configuration. This Service Account is managed by MongoDB Atlas.")
    ip_access_list: list[ServiceAccountIPAccessListEntry] | None = Field(default=None, alias="ipAccessList", description="List of IP access list entries that define allowed source addresses for this MCP configuration.")
    mcp_config_id: str | None = Field(default=None, alias="mcpConfigId", description="Unique identifier that identifies this MCP configuration.")
    mcp_config_name: str | None = Field(default=None, alias="mcpConfigName", description="Human-readable name that identifies this MCP configuration.")
    roles: list[Annotated[Literal["ORG_MEMBER", "ORG_READ_ONLY", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_GROUP_CREATOR", "ORG_OWNER"], BeforeValidator(upper_case)]] | None = Field(default=None, description="List of organization roles associated with this MCP configuration.")
