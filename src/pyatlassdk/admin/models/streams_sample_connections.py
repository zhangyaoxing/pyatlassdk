"""Generated model for StreamsSampleConnections. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsSampleConnections(BaseModel):
    """Sample connections to add to SPI."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    solar: bool | None = Field(default=None, description="Flag that indicates whether to add a `sample_stream_solar` connection.")
