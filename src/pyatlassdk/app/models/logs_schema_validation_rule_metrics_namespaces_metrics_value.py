"""Generated model for LogsSchemaValidationRuleMetricsNamespacesMetricsValue. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_schema_validation_rule_metrics_namespaces_metrics_value_roles_value import LogsSchemaValidationRuleMetricsNamespacesMetricsValueRolesValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaValidationRuleMetricsNamespacesMetricsValue(BaseModel):
    """Generated model for LogsSchemaValidationRuleMetricsNamespacesMetricsValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: dict[str, LogsSchemaValidationRuleMetricsNamespacesMetricsValueRolesValue] | None = None
    no_matching_role: float | None = None
