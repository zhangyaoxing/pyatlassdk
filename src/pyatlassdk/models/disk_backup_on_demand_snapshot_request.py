"""Generated model for DiskBackupOnDemandSnapshotRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupOnDemandSnapshotRequest(BaseModel):
    """Generated model for DiskBackupOnDemandSnapshotRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when `\"status\" : \"onDemand\"`.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    retention_in_days: int | None = Field(default=None, alias="retentionInDays", description="Number of days that MongoDB Cloud should retain the on-demand snapshot. Must be at least **1**.")
