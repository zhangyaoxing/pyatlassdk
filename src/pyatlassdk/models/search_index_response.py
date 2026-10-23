"""Generated model for SearchIndexResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.search_host_status_detail import SearchHostStatusDetail
from pyatlassdk.models.search_index_definition import SearchIndexDefinition
from pyatlassdk.models.search_index_definition_version import SearchIndexDefinitionVersion

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchIndexResponse(BaseModel):
    """Generated model for SearchIndexResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_name: str | None = Field(default=None, alias="collectionName", description="Label that identifies the collection that contains one or more Atlas Search indexes.")
    database: str | None = Field(default=None, description="Label that identifies the database that contains the collection with one or more Atlas Search indexes.")
    index_id: str | None = Field(default=None, alias="indexID", description="Unique 24-hexadecimal digit string that identifies this Atlas Search index.")
    latest_definition: SearchIndexDefinition | None = Field(default=None, alias="latestDefinition")
    latest_definition_version: SearchIndexDefinitionVersion | None = Field(default=None, alias="latestDefinitionVersion")
    name: str | None = Field(default=None, description="Label that identifies this index. Within each namespace, the names of all indexes must be unique.")
    queryable: bool | None = Field(default=None, description="Flag that indicates whether the index is queryable on all hosts.")
    status: Annotated[Literal["DELETING", "FAILED", "STALE", "PENDING", "BUILDING", "READY", "DOES_NOT_EXIST"], BeforeValidator(upper_case)] | None = Field(default=None, description="Condition of the search index when you made this request.\n\n- `DELETING`: The index is being deleted.\n- `FAILED` The index build failed. Indexes can enter the FAILED state due to an invalid index definition.\n- `STALE`: The index is queryable but has stopped replicating data from the indexed collection. Searches on the index may return out-of-date data.\n- `PENDING`: Atlas has not yet started building the index.\n- `BUILDING`: Atlas is building or re-building the index after an edit.\n- `READY`: The index is ready and can support queries.")
    status_detail: list[SearchHostStatusDetail] | None = Field(default=None, alias="statusDetail", description="List of documents detailing index status on each host.")
    type: Literal["search", "vectorSearch"] | None = Field(default=None, description="Type of the index. The default type is search.")
