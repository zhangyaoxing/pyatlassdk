"""Generated model for QueryStatsCollectionRateLimitedResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class QueryStatsCollectionRateLimitedResponse(BaseModel):
    """Entries were collected by rate-limiting read queries."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    mode: Annotated[Literal["RATE_LIMITED", "SAMPLED"], BeforeValidator(upper_case)] = Field(description="Method used to collect `queryStats` entries on the cluster's processes.")
    rate_limit_per_second: int = Field(alias="rateLimitPerSecond", description="Maximum read queries recorded per second.")
