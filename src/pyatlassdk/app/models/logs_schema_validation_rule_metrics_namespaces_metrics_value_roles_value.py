"""Generated model for LogsSchemaValidationRuleMetricsNamespacesMetricsValueRolesValue. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaValidationRuleMetricsNamespacesMetricsValueRolesValue(BaseModel):
    """Generated model for LogsSchemaValidationRuleMetricsNamespacesMetricsValueRolesValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    matching_documents: float | None = None
    evaluated_fields: float | None = None
    discarded_fields: float | None = None
