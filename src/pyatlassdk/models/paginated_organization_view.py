"""Generated model for PaginatedOrganizationView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.atlas_organization import AtlasOrganization
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class PaginatedOrganizationView(BaseModel):
    """Generated model for PaginatedOrganizationView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    results: list[AtlasOrganization] = Field(description="List of returned documents that MongoDB Cloud provides when completing this request.")
    total_count: int | None = Field(default=None, alias="totalCount", description="Total number of documents available. When `includeCount` is set to `false`, MongoDB Cloud may omit this value or return it when the count is available without additional calculation. The total number is an estimate and may not be exact.")
