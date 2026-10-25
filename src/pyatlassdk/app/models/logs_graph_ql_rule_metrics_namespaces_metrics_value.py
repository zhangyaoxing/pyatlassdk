"""Generated model for LogsGraphQLRuleMetricsNamespacesMetricsValue. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_graph_ql_rule_metrics_namespaces_metrics_value_roles_value import LogsGraphQLRuleMetricsNamespacesMetricsValueRolesValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsGraphQLRuleMetricsNamespacesMetricsValue(BaseModel):
    """Generated model for LogsGraphQLRuleMetricsNamespacesMetricsValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: dict[str, LogsGraphQLRuleMetricsNamespacesMetricsValueRolesValue] | None = None
    no_matching_role: float | None = None
