"""Generated model for LogsSchemaAdditiveChangeRuleMetrics. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_schema_additive_change_rule_metrics_namespaces_metrics_value import LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaAdditiveChangeRuleMetrics(BaseModel):
    """Generated model for LogsSchemaAdditiveChangeRuleMetrics."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespaces_metrics: dict[str, LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValue] | None = None
