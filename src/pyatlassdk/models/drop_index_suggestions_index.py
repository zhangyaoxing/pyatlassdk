"""Generated model for DropIndexSuggestionsIndex. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.drop_index_suggestions_index_collation import DropIndexSuggestionsIndexCollation
from pyatlassdk.models.drop_index_suggestions_index_index_item import DropIndexSuggestionsIndexIndexItem

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DropIndexSuggestionsIndex(BaseModel):
    """Generated model for DropIndexSuggestionsIndex."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access_count: int | None = Field(default=None, alias="accessCount", description="Usage count (since last restart) of index.")
    collation: DropIndexSuggestionsIndexCollation | None = Field(default=None, description="Collation this index was built with. An index only serves a query that runs with the same collation. Absent when the index uses the default (simple) collation.")
    index: list[DropIndexSuggestionsIndexIndexItem] | None = Field(default=None, description="List that contains documents that specify a key in the index and its sort order.")
    name: str | None = Field(default=None, description="Name of index.")
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    shards: list[str] | None = Field(default=None, description="List that contains strings that specifies the shards where the index is found.")
    since: datetime | None = Field(default=None, description="Date of most recent usage of index. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    size_bytes: int | None = Field(default=None, alias="sizeBytes", description="Size of index.")
