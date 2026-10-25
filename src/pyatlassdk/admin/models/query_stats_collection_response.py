"""Generated model for QueryStatsCollectionResponse. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.query_stats_collection_rate_limited_response import QueryStatsCollectionRateLimitedResponse
from pyatlassdk.admin.models.query_stats_collection_sampled_response import QueryStatsCollectionSampledResponse

QueryStatsCollectionResponse: TypeAlias = QueryStatsCollectionSampledResponse | QueryStatsCollectionRateLimitedResponse
