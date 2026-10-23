"""Generated model for StreamsProcessorWithStats. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_options import StreamsOptions

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsProcessorWithStats(BaseModel):
    """An atlas stream processor with optional stats."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(alias="_id", description="Unique 24-hexadecimal character string that identifies the stream processor.")
    effective_tier: Annotated[Literal["SP50", "SP30", "SP10", "SP5", "SP2"], BeforeValidator(upper_case)] = Field(alias="effectiveTier", description="Tier the stream processor is currently running on. The server sets this value from `tier` on create and on every start or restart, may move it within [`minTier`, `maxTier`] while autoscaling is enabled, and restores it to `tier` when autoscaling is disabled. Patching `tier` does not change it directly; the new tier takes effect at the next start or restart.")
    eligible_for_failover: bool | None = Field(default=None, alias="eligibleForFailover", description="Flag that indicates whether the stream processor is eligible for failover.")
    failover_enabled: bool | None = Field(default=None, alias="failoverEnabled", description="Flag that enables or disables failover for the stream processor.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str = Field(description="Human-readable name of the stream processor.")
    options: StreamsOptions | None = None
    pipeline: list[dict[str, dict[str, Any]]] = Field(description="Stream aggregation pipeline you want to apply to your streaming data.")
    state: str = Field(description="The state of the stream processor. Commonly occurring states are 'CREATED', 'STARTED', 'STOPPED' and 'FAILED'.")
    stats: dict[str, dict[str, Any]] | None = Field(default=None, description="The stats associated with the stream processor.")
    tier: Annotated[Literal["SP50", "SP30", "SP10", "SP5", "SP2"], BeforeValidator(upper_case)] | None = Field(default=None, description="Baseline tier of the stream processor. The processor starts or restarts on this tier; `effectiveTier` reports the tier it is currently running.")
