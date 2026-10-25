"""Generated model for PaginatedHostViewAtlas. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.api_host_view_atlas import ApiHostViewAtlas
from pyatlassdk.admin.models.link_atlas import LinkAtlas

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PaginatedHostViewAtlas(BaseModel):
    """Generated model for PaginatedHostViewAtlas."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[LinkAtlas] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    results: list[ApiHostViewAtlas] = Field(description="List of returned documents that MongoDB Cloud provides when completing this request.")
    total_count: int | None = Field(default=None, alias="totalCount", description="Total number of documents available. When `includeCount` is set to `false`, MongoDB Cloud may omit this value or return it when the count is available without additional calculation. The total number is an estimate and may not be exact.")
