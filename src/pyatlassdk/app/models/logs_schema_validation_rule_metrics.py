"""Generated model for LogsSchemaValidationRuleMetrics. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_schema_validation_rule_metrics_namespaces_metrics_value import LogsSchemaValidationRuleMetricsNamespacesMetricsValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaValidationRuleMetrics(BaseModel):
    """Generated model for LogsSchemaValidationRuleMetrics."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespaces_metrics: dict[str, LogsSchemaValidationRuleMetricsNamespacesMetricsValue] | None = None
