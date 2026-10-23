"""Generated model for PerformanceAdvisorOperationView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.performance_advisor_op_stats import PerformanceAdvisorOpStats
from pyatlassdk.models.performance_advisor_operation_view_predicates_item import PerformanceAdvisorOperationViewPredicatesItem

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PerformanceAdvisorOperationView(BaseModel):
    """Generated model for PerformanceAdvisorOperationView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    predicates: list[PerformanceAdvisorOperationViewPredicatesItem] | None = Field(default=None, description="List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Observability Viewer** or **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values.")
    raw: str | None = Field(default=None, description="Opaque serialized raw slow query log line or query shape for the query shape to be improved with index suggestions. The format isn't stable, so don't parse this value. Accessing this value requires **Project Observability Viewer** or **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud returns `null`.")
    stats: PerformanceAdvisorOpStats | None = None
