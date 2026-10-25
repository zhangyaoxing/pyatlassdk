"""Generated model for StreamsPublicPrivateLinkNetworking. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link
from pyatlassdk.admin.models.streams_public_private_link_networking_access import StreamsPublicPrivateLinkNetworkingAccess

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsPublicPrivateLinkNetworking(BaseModel):
    """Networking configuration for connections that support `PUBLIC` and `PRIVATE_LINK` access types. For GCP connections, use `PRIVATE_LINK` for GCP Private Service Connect (PSC)."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access: StreamsPublicPrivateLinkNetworkingAccess | None = None
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
