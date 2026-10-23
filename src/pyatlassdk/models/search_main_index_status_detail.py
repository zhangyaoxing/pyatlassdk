"""Generated model for SearchMainIndexStatusDetail. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.search_index_definition import SearchIndexDefinition
from pyatlassdk.models.search_index_definition_version import SearchIndexDefinitionVersion

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchMainIndexStatusDetail(BaseModel):
    """Contains status information about the active index."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    definition: SearchIndexDefinition | None = None
    definition_version: SearchIndexDefinitionVersion | None = Field(default=None, alias="definitionVersion")
    message: str | None = Field(default=None, description="Optional message describing an error.")
    queryable: bool | None = Field(default=None, description="Flag that indicates whether the index generation is queryable on the host.")
    status: Annotated[Literal["DELETING", "FAILED", "STALE", "PENDING", "BUILDING", "READY", "DOES_NOT_EXIST"], BeforeValidator(upper_case)] | None = Field(default=None, description="Condition of the search index when you made this request.\n\n- `DELETING`: The index is being deleted.\n- `FAILED` The index build failed. Indexes can enter the FAILED state due to an invalid index definition.\n- `STALE`: The index is queryable but has stopped replicating data from the indexed collection. Searches on the index may return out-of-date data.\n- `PENDING`: Atlas has not yet started building the index.\n- `BUILDING`: Atlas is building or re-building the index after an edit.\n- `READY`: The index is ready and can support queries.")
