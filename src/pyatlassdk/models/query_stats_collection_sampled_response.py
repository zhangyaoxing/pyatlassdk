"""Generated model for QueryStatsCollectionSampledResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class QueryStatsCollectionSampledResponse(BaseModel):
    """Entries were collected by sampling each operation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    mode: Annotated[Literal["RATE_LIMITED", "SAMPLED"], BeforeValidator(upper_case)] = Field(description="Method used to collect `queryStats` entries on the cluster's processes.")
    sample_rate: float = Field(alias="sampleRate", description="Fraction of operations recorded. Dividing reported counts by this rate yields an unbiased estimate of the true totals.")
