"""Generated model for SchemaAdvisorItemRecommendation. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.schema_advisor_namespace_triggers import SchemaAdvisorNamespaceTriggers

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SchemaAdvisorItemRecommendation(BaseModel):
    """Generated model for SchemaAdvisorItemRecommendation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    affected_namespaces: list[SchemaAdvisorNamespaceTriggers] | None = Field(default=None, alias="affectedNamespaces", description="List that contains the namespaces and information on why those namespaces triggered the recommendation.")
    description: str | None = Field(default=None, description="Description of the specified recommendation.")
    recommendation: Annotated[Literal["REDUCE_LOOKUP_OPS", "AVOID_UNBOUNDED_ARRAY", "REDUCE_DOCUMENT_SIZE", "REMOVE_UNNECESSARY_INDEXES", "REDUCE_NUMBER_OF_NAMESPACES", "OPTIMIZE_CASE_INSENSITIVE_REGEX_QUERIES", "OPTIMIZE_TEXT_QUERIES"], BeforeValidator(upper_case)] | None = Field(default=None, description="Type of recommendation.")
