"""Generated model for PaginatedApiStreamsPrivateLinkView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_private_link_connection import StreamsPrivateLinkConnection

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PaginatedApiStreamsPrivateLinkView(BaseModel):
    """Generated model for PaginatedApiStreamsPrivateLinkView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    results: list[StreamsPrivateLinkConnection] = Field(description="List of returned documents that MongoDB Cloud provides when completing this request.")
    total_count: int | None = Field(default=None, alias="totalCount", description="Total number of documents available. When `includeCount` is set to `false`, MongoDB Cloud may omit this value or return it when the count is available without additional calculation. The total number is an estimate and may not be exact.")
