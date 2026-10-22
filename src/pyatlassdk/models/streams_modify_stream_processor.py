"""Generated model for StreamsModifyStreamProcessor. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.document import Document
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_modify_stream_processor_options import StreamsModifyStreamProcessorOptions

from pydantic import BaseModel, ConfigDict, Field

class StreamsModifyStreamProcessor(BaseModel):
    """A request to modify an existing stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    failover_enabled: bool | None = Field(default=None, alias="failoverEnabled", description="Flag that enables or disables failover for the stream processor.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="New name for the stream processor.")
    options: StreamsModifyStreamProcessorOptions | None = None
    pipeline: list[Document] | None = Field(default=None, description="New pipeline for the stream processor.")
    tier: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] | None = Field(default=None, description="Baseline processing tier requested by the user.")
