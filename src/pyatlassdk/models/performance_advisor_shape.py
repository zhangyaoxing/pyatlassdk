"""Generated model for PerformanceAdvisorShape. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.performance_advisor_operation_view import PerformanceAdvisorOperationView

from pydantic import BaseModel, ConfigDict, Field

class PerformanceAdvisorShape(BaseModel):
    """Generated model for PerformanceAdvisorShape."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    avg_ms: int | None = Field(default=None, alias="avgMs", description="Average duration in milliseconds for the queries examined that match this shape.")
    count: int | None = Field(default=None, description="Number of queries examined that match this shape.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this shape. This string exists only for the duration of this API request.")
    inefficiency_score: int | None = Field(default=None, alias="inefficiencyScore", description="Average number of documents read for every document that the query returns.")
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    operations: list[PerformanceAdvisorOperationView] | None = Field(default=None, description="List that contains specific about individual queries.")
