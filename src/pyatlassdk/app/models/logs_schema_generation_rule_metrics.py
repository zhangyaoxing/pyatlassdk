"""Generated model for LogsSchemaGenerationRuleMetrics. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.logs_schema_generation_rule_metrics_namespaces_metrics_value import LogsSchemaGenerationRuleMetricsNamespacesMetricsValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaGenerationRuleMetrics(BaseModel):
    """Generated model for LogsSchemaGenerationRuleMetrics."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespaces_metrics: dict[str, LogsSchemaGenerationRuleMetricsNamespacesMetricsValue] | None = None
