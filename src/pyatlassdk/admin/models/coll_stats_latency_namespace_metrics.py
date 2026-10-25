"""Generated model for CollStatsLatencyNamespaceMetrics. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.coll_stats_latency_namespace_metric import CollStatsLatencyNamespaceMetric
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CollStatsLatencyNamespaceMetrics(BaseModel):
    """Generated model for CollStatsLatencyNamespaceMetrics."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    metrics: list[CollStatsLatencyNamespaceMetric] = Field(description="List of Coll Stats Latency metric names and their respective units.")
