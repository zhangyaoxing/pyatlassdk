"""Generated model for StreamsGCPConnectionConfig. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class StreamsGCPConnectionConfig(BaseModel):
    """GCP-specific configuration for the connection."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    service_account_id: str | None = Field(default=None, alias="serviceAccountId", description="Email address of the Google Cloud Platform (GCP) service account that Atlas Streams uses to connect to the GCP Pub/Sub resources.")
