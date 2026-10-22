"""Generated model for QueryStatsCollectionRateLimitedResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class QueryStatsCollectionRateLimitedResponse(BaseModel):
    """Entries were collected by rate-limiting read queries."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    mode: Literal["RATE_LIMITED", "SAMPLED"] = Field(description="Method used to collect `queryStats` entries on the cluster's processes.")
    rate_limit_per_second: int = Field(alias="rateLimitPerSecond", description="Maximum read queries recorded per second.")
