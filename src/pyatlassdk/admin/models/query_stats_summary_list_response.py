"""Generated model for QueryStatsSummaryListResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.query_stats_collection_response import QueryStatsCollectionResponse
from pyatlassdk.admin.models.query_stats_summary import QueryStatsSummary

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class QueryStatsSummaryListResponse(BaseModel):
    """Generated model for QueryStatsSummaryListResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    query_stats_collection: QueryStatsCollectionResponse | None = Field(default=None, alias="queryStatsCollection")
    summaries: list[QueryStatsSummary] | None = Field(default=None, description="List of query shape statistic summaries from Query Shape Insights.")
