"""Generated model for CloudSearchMetrics. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.fts_metric import FTSMetric
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudSearchMetrics(BaseModel):
    """Generated model for CloudSearchMetrics."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project.")
    hardware_metrics: list[FTSMetric] = Field(alias="hardwareMetrics", description="List that contains all host compute, memory, and storage utilization dedicated to Atlas Search when MongoDB Atlas received this request.")
    index_metrics: list[FTSMetric] = Field(alias="indexMetrics", description="List that contains all performance and utilization measurements that Atlas Search index performed by the time MongoDB Atlas received this request.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    process_id: str = Field(alias="processId", description="Hostname and port that identifies the process.")
    status_metrics: list[FTSMetric] = Field(alias="statusMetrics", description="List that contains all available Atlas Search status metrics when MongoDB Atlas received this request.")
