"""Generated model for LogsSchemaGenerationRuleMetricsNamespacesMetricsValue. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_schema_generation_rule_metrics_namespaces_metrics_value_roles_value import LogsSchemaGenerationRuleMetricsNamespacesMetricsValueRolesValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaGenerationRuleMetricsNamespacesMetricsValue(BaseModel):
    """Generated model for LogsSchemaGenerationRuleMetricsNamespacesMetricsValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    roles: dict[str, LogsSchemaGenerationRuleMetricsNamespacesMetricsValueRolesValue] | None = None
    no_matching_role: float | None = None
