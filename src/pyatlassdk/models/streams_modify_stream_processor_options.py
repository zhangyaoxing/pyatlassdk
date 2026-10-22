"""Generated model for StreamsModifyStreamProcessorOptions. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_autoscaling import StreamsAutoscaling
from pyatlassdk.models.streams_dlq import StreamsDLQ

from pydantic import BaseModel, ConfigDict, Field

class StreamsModifyStreamProcessorOptions(BaseModel):
    """Additional options for modifying a stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    autoscaling: StreamsAutoscaling | None = None
    dlq: StreamsDLQ | None = None
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    resume_from_checkpoint: bool | None = Field(default=None, alias="resumeFromCheckpoint", description="When true, the modified stream processor resumes from its last checkpoint.")
