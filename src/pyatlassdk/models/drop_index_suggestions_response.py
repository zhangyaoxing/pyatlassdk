"""Generated model for DropIndexSuggestionsResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.drop_index_suggestions_index import DropIndexSuggestionsIndex

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DropIndexSuggestionsResponse(BaseModel):
    """Response that contains Performance Advisor drop index suggestions."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    hidden_indexes: list[DropIndexSuggestionsIndex] | None = Field(default=None, alias="hiddenIndexes", description="List that contains the documents with information about the hidden indexes that the Performance Advisor suggests to remove.")
    redundant_indexes: list[DropIndexSuggestionsIndex] | None = Field(default=None, alias="redundantIndexes", description="List that contains the documents with information about the redundant indexes that the Performance Advisor suggests to remove.")
    unused_indexes: list[DropIndexSuggestionsIndex] | None = Field(default=None, alias="unusedIndexes", description="List that contains the documents with information about the unused indexes that the Performance Advisor suggests to remove.")
