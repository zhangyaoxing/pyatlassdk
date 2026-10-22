"""Generated model for UserAccessListRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class UserAccessListRequest(BaseModel):
    """Generated model for UserAccessListRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="Range of network addresses that you want to add to the access list for the API key. This parameter requires the range to be expressed in classless inter-domain routing (CIDR) notation of Internet Protocol version 4 or version 6 addresses. You can set a value for this parameter or `ipAddress` but not both in the same request.")
    ip_address: str | None = Field(default=None, alias="ipAddress", description="Network address that you want to add to the access list for the API key. This parameter requires the address to be expressed as one Internet Protocol version 4 or version 6 address. You can set a value for this parameter or `cidrBlock` but not both in the same request.")
