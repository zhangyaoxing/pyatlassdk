"""Generated model for DiskBackupCollectionResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class DiskBackupCollectionResponse(BaseModel):
    """Generated model for DiskBackupCollectionResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str = Field(description="Human-readable label that identifies the collection in the database within the snapshot.")
