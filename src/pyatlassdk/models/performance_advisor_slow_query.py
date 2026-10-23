"""Generated model for PerformanceAdvisorSlowQuery. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.performance_advisor_slow_query_metrics import PerformanceAdvisorSlowQueryMetrics

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PerformanceAdvisorSlowQuery(BaseModel):
    """Details of one slow query that the Performance Advisor detected."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    line: str | None = Field(default=None, description="Text of the MongoDB log related to this slow query.")
    metrics: PerformanceAdvisorSlowQueryMetrics | None = None
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    op_type: str | None = Field(default=None, alias="opType", description="Operation type (read/write/command) associated with this slow query log.")
    replica_state: str | None = Field(default=None, alias="replicaState", description="Replica state associated with this slow query log.")
