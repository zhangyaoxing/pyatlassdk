"""Generated model for LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValue. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_schema_additive_change_rule_metrics_namespaces_metrics_value_roles_value import LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValueRolesValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValue(BaseModel):
    """Generated model for LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: dict[str, LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValueRolesValue] | None = None
    no_matching_role: float | None = None
