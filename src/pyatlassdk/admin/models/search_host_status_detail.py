"""Generated model for SearchHostStatusDetail. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.search_main_index_status_detail import SearchMainIndexStatusDetail
from pyatlassdk.admin.models.search_staged_index_status_detail import SearchStagedIndexStatusDetail

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchHostStatusDetail(BaseModel):
    """Generated model for SearchHostStatusDetail."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    hostname: str | None = Field(default=None, description="Hostname that corresponds to the status detail.")
    main_index: SearchMainIndexStatusDetail | None = Field(default=None, alias="mainIndex")
    queryable: bool | None = Field(default=None, description="Flag that indicates whether the index is queryable on the host.")
    staged_index: SearchStagedIndexStatusDetail | None = Field(default=None, alias="stagedIndex")
    status: Annotated[Literal["DELETING", "FAILED", "STALE", "PENDING", "BUILDING", "READY", "DOES_NOT_EXIST"], BeforeValidator(upper_case)] | None = Field(default=None, description="Condition of the search index when you made this request.\n\n- `DELETING`: The index is being deleted.\n- `FAILED` The index build failed. Indexes can enter the FAILED state due to an invalid index definition.\n- `STALE`: The index is queryable but has stopped replicating data from the indexed collection. Searches on the index may return out-of-date data.\n- `PENDING`: Atlas has not yet started building the index.\n- `BUILDING`: Atlas is building or re-building the index after an edit.\n- `READY`: The index is ready and can support queries.")
