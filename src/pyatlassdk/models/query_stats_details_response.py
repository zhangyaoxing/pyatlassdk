"""Generated model for QueryStatsDetailsResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.query_shape_seen_metadata import QueryShapeSeenMetadata
from pyatlassdk.models.query_stats_collection_response import QueryStatsCollectionResponse
from pyatlassdk.models.query_stats_summary import QueryStatsSummary

from pydantic import BaseModel, ConfigDict, Field

class QueryStatsDetailsResponse(BaseModel):
    """Metadata and summary statistics for a given query shape."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    first_seen: QueryShapeSeenMetadata | None = Field(default=None, alias="firstSeen")
    last_seen: QueryShapeSeenMetadata | None = Field(default=None, alias="lastSeen")
    query_stats: QueryStatsSummary | None = Field(default=None, alias="queryStats")
    query_stats_collection: QueryStatsCollectionResponse | None = Field(default=None, alias="queryStatsCollection")
