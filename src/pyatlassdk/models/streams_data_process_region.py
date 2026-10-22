"""Generated model for StreamsDataProcessRegion. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.base_streams_region import BaseStreamsRegion
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class StreamsDataProcessRegion(BaseModel):
    """Information about the cloud provider region in which MongoDB Cloud processes the stream."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "GCP", "AZURE", "TENANT", "SERVERLESS"] = Field(alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    region: BaseStreamsRegion
