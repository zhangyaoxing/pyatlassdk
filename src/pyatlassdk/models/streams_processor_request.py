"""Generated model for StreamsProcessorRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.document import Document
from pyatlassdk.models.streams_options import StreamsOptions

from pydantic import BaseModel, ConfigDict, Field

class StreamsProcessorRequest(BaseModel):
    """Details to create a stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    failover_enabled: bool | None = Field(default=None, alias="failoverEnabled", description="Flag that enables or disables failover for the stream processor.")
    name: str = Field(description="Human-readable name of the stream processor.")
    options: StreamsOptions | None = None
    pipeline: list[Document] = Field(description="Stream aggregation pipeline you want to apply to your streaming data.")
    tier: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] | None = Field(default=None, description="Baseline processing tier requested by the user.")
