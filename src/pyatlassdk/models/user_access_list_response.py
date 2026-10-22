"""Generated model for UserAccessListResponse. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class UserAccessListResponse(BaseModel):
    """Generated model for UserAccessListResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="Range of IP addresses in Classless Inter-Domain Routing (CIDR) notation in the access list for the API key.")
    count: int | None = Field(default=None, description="Total number of requests that have originated from the Internet Protocol (IP) address given as the value of the `lastUsedAddress` parameter.")
    created: datetime | None = Field(default=None, description="Date and time when someone added the network addresses to the specified API access list. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    ip_address: str | None = Field(default=None, alias="ipAddress", description="Network address in the access list for the API key.")
    last_used: datetime | None = Field(default=None, alias="lastUsed", description="Date and time when MongoDB Cloud received the most recent request that originated from this Internet Protocol version 4 or version 6 address. The resource returns this parameter when at least one request has originated from this IP address. MongoDB Cloud updates this parameter each time a client accesses the permitted resource. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    last_used_address: str | None = Field(default=None, alias="lastUsedAddress", description="Network address that issued the most recent request to the API. This parameter requires the address to be expressed as one Internet Protocol version 4 or version 6 address. The resource returns this parameter after this IP address made at least one request.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
