"""Generated model for LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValueRolesValue. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValueRolesValue(BaseModel):
    """Generated model for LogsSchemaAdditiveChangeRuleMetricsNamespacesMetricsValueRolesValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    matching_documents: float | None = None
    evaluated_fields: float | None = None
    discarded_fields: float | None = None
