"""Generated model for StreamsProcessor. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.document import Document
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_options import StreamsOptions

from pydantic import BaseModel, ConfigDict, Field

class StreamsProcessor(BaseModel):
    """An atlas stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal character string that identifies the stream processor.")
    effective_tier: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] = Field(alias="effectiveTier", description="Tier the stream processor is currently running on. The server sets this value from `tier` on create and on every start or restart, may move it within [`minTier`, `maxTier`] while autoscaling is enabled, and restores it to `tier` when autoscaling is disabled. Patching `tier` does not change it directly; the new tier takes effect at the next start or restart.")
    failover_enabled: bool | None = Field(default=None, alias="failoverEnabled", description="Flag that enables or disables failover for the stream processor.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable name of the stream processor.")
    options: StreamsOptions | None = None
    pipeline: list[Document] | None = Field(default=None, description="Stream aggregation pipeline you want to apply to your streaming data.")
    tier: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] | None = Field(default=None, description="Baseline tier of the stream processor. The processor starts or restarts on this tier; `effectiveTier` reports the tier it is currently running.")
