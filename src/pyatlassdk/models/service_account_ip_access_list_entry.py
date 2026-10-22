"""Generated model for ServiceAccountIPAccessListEntry. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class ServiceAccountIPAccessListEntry(BaseModel):
    """Generated model for ServiceAccountIPAccessListEntry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="Range of network addresses in the access list for the Service Account. This parameter requires the range to be expressed in Classless Inter-Domain Routing (CIDR) notation of Internet Protocol version 4 or version 6 addresses. You can set a value for this parameter or `ipAddress`, but not for both in the same request.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date MongoDB Cloud added the entry was added to the Access List. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    ip_address: str | None = Field(default=None, alias="ipAddress", description="Network address in the access list for the Service Account. This parameter requires the address to be expressed as one Internet Protocol version 4 or version 6 address. You can set a value for this parameter or `cidrBlock`, but not for both in the same request.")
    last_used_address: str | None = Field(default=None, alias="lastUsedAddress", description="Network address that issued the most recent request to the API. This parameter requires the address to be expressed as one Internet Protocol version 4 or version 6 address. The resource returns this parameter after this IP address makes at least one request.")
    last_used_at: datetime | None = Field(default=None, alias="lastUsedAt", description="Date when MongoDB Cloud received the most recent request that originated from this Internet Protocol version 4 or version 6 address. The resource returns this parameter when at least one request originates from this IP address. MongoDB Cloud updates this parameter each time a client accesses the permitted resource, with a delay of up to 5 minutes. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    request_count: int | None = Field(default=None, alias="requestCount", description="The number of requests that has originated from this network address.")
