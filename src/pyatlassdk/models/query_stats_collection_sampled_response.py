"""Generated model for QueryStatsCollectionSampledResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class QueryStatsCollectionSampledResponse(BaseModel):
    """Entries were collected by sampling each operation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    mode: Literal["RATE_LIMITED", "SAMPLED"] = Field(description="Method used to collect `queryStats` entries on the cluster's processes.")
    sample_rate: float = Field(alias="sampleRate", description="Fraction of operations recorded. Dividing reported counts by this rate yields an unbiased estimate of the true totals.")
