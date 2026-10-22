"""Generated model for StreamsKafkaNetworking. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_kafka_networking_access import StreamsKafkaNetworkingAccess

from pydantic import BaseModel, ConfigDict, Field

class StreamsKafkaNetworking(BaseModel):
    """Networking configuration for Streams connections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access: StreamsKafkaNetworkingAccess | None = None
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
