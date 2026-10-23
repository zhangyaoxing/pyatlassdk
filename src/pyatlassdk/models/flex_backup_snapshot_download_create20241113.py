"""Generated model for FlexBackupSnapshotDownloadCreate20241113. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexBackupSnapshotDownloadCreate20241113(BaseModel):
    """Details for one backup snapshot download of a flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    snapshot_id: str = Field(alias="snapshotId", description="Unique 24-hexadecimal digit string that identifies the snapshot to download.")
