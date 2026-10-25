"""Generated model for LogsGraphQLRuleMetrics. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_graph_ql_rule_metrics_namespaces_metrics_value import LogsGraphQLRuleMetricsNamespacesMetricsValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsGraphQLRuleMetrics(BaseModel):
    """Generated model for LogsGraphQLRuleMetrics."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespaces_metrics: dict[str, LogsGraphQLRuleMetricsNamespacesMetricsValue] | None = None
