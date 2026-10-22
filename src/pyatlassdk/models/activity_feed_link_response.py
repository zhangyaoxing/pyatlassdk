"""Generated model for ActivityFeedLinkResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class ActivityFeedLinkResponse(BaseModel):
    """Response containing a shareable activity feed link."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    link: str = Field(description="Shareable link to the activity feed with pre-applied filters.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
