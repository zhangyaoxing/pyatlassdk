"""Generated model for SchemaAdvisorNamespaceTriggers. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.schema_advisor_trigger_details import SchemaAdvisorTriggerDetails

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SchemaAdvisorNamespaceTriggers(BaseModel):
    """Generated model for SchemaAdvisorNamespaceTriggers."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespace: str | None = Field(default=None, description="Namespace of the affected collection. Will be null for `REDUCE_NUMBER_OF_NAMESPACE` recommendation.")
    triggers: list[SchemaAdvisorTriggerDetails] | None = Field(default=None, description="List of triggers that specify why the collection activated the recommendation.")
