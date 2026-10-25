"""Generated model for StreamsOptions. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link
from pyatlassdk.admin.models.streams_autoscaling import StreamsAutoscaling
from pyatlassdk.admin.models.streams_dlq import StreamsDLQ

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsOptions(BaseModel):
    """Optional configuration for the stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    autoscaling: StreamsAutoscaling | None = None
    dlq: StreamsDLQ | None = None
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
