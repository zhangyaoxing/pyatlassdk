"""Generated model for PerformanceAdvisorSlowQueryList. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.performance_advisor_slow_query import PerformanceAdvisorSlowQuery

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PerformanceAdvisorSlowQueryList(BaseModel):
    """Generated model for PerformanceAdvisorSlowQueryList."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    slow_queries: list[PerformanceAdvisorSlowQuery] | None = Field(default=None, alias="slowQueries", description="List of operations that the Performance Advisor detected that took longer to execute than a specified threshold.")
