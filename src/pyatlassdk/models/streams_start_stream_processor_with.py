"""Generated model for StreamsStartStreamProcessorWith. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_autoscaling import StreamsAutoscaling
from pyatlassdk.models.streams_start_processor_failover import StreamsStartProcessorFailover

from pydantic import BaseModel, ConfigDict, Field

class StreamsStartStreamProcessorWith(BaseModel):
    """A request to start a stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    autoscaling: StreamsAutoscaling | None = None
    failover: StreamsStartProcessorFailover | None = None
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    resume_from_checkpoint: bool | None = Field(default=None, alias="resumeFromCheckpoint", description="When true or not specified, the stream processor resumes from its last checkpoint. When false, the stream processor starts fresh.")
    start_at_operation_time: datetime | None = Field(default=None, alias="startAtOperationTime", description="The operation time after which the change stream source should begin reporting. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    tier: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] | None = Field(default=None, description="Baseline processing tier requested by the user.")
