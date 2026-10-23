"""Generated model for AccessListItemView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AccessListItemView(BaseModel):
    """Generated model for AccessListItemView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="Range of IP addresses in Classless Inter-Domain Routing (CIDR) notation that found in this project's access list.")
    ip_address: str | None = Field(alias="ipAddress", description="IP address included in the API access list.")
