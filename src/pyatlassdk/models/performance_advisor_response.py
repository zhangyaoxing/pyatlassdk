"""Generated model for PerformanceAdvisorResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.performance_advisor_index import PerformanceAdvisorIndex
from pyatlassdk.models.performance_advisor_shape import PerformanceAdvisorShape

from pydantic import BaseModel, ConfigDict, Field

class PerformanceAdvisorResponse(BaseModel):
    """Response that contains Performance Advisor suggested indexes and query shapes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    shapes: list[PerformanceAdvisorShape] | None = Field(default=None, description="List of query predicates, sorts, and projections that the Performance Advisor suggests.")
    suggested_indexes: list[PerformanceAdvisorIndex] | None = Field(default=None, alias="suggestedIndexes", description="List that contains the documents with information about the indexes that the Performance Advisor suggests.")
