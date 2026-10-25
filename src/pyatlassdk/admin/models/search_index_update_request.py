"""Generated model for SearchIndexUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.text_search_index_definition import TextSearchIndexDefinition
from pyatlassdk.admin.models.vector_search_index_definition import VectorSearchIndexDefinition

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchIndexUpdateRequest(BaseModel):
    """Generated model for SearchIndexUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    definition: TextSearchIndexDefinition | VectorSearchIndexDefinition = Field(description="The index definition to update the search index to.")
