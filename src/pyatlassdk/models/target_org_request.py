"""Generated model for TargetOrgRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class TargetOrgRequest(BaseModel):
    """Generated model for TargetOrgRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access_list_ips: list[str] | None = Field(default=None, alias="accessListIps", description="IP address access list entries associated with the API key.")
