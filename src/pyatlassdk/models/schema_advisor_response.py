"""Generated model for SchemaAdvisorResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.schema_advisor_item_recommendation import SchemaAdvisorItemRecommendation

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SchemaAdvisorResponse(BaseModel):
    """Response that contains Performance Advisor schema suggestions."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    recommendations: list[SchemaAdvisorItemRecommendation] | None = Field(default=None, description="List that contains the documents with information about the schema advice that Performance Advisor suggests.")
