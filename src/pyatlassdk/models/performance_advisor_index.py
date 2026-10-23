"""Generated model for PerformanceAdvisorIndex. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.performance_advisor_index_collation import PerformanceAdvisorIndexCollation
from pyatlassdk.models.performance_advisor_index_index_item import PerformanceAdvisorIndexIndexItem

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PerformanceAdvisorIndex(BaseModel):
    """Generated model for PerformanceAdvisorIndex."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    avg_obj_size: float | None = Field(default=None, alias="avgObjSize", description="The average size of an object in the collection of this index.")
    collation: PerformanceAdvisorIndexCollation | None = Field(default=None, description="Collation the queries behind this suggestion run with. An index only serves a query when the two share a collation, so an index created from this suggestion must be created with it. Absent when those queries use the default (simple) collation.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this index.")
    impact: list[str] | None = Field(default=None, description="List that contains unique 24-hexadecimal character string that identifies the query shapes in this response that the Performance Advisor suggests.")
    index: list[PerformanceAdvisorIndexIndexItem] | None = Field(default=None, description="List that contains documents that specify a key in the index and its sort order.")
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    weight: float | None = Field(default=None, description="Estimated performance improvement that the suggested index provides. This value corresponds to **Impact** in the Performance Advisor user interface.")
