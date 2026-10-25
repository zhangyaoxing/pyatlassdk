"""Generated model for DiskBackupExportJobRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.backup_label import BackupLabel
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupExportJobRequest(BaseModel):
    """Generated model for DiskBackupExportJobRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    custom_data: list[BackupLabel] | None = Field(default=None, alias="customData", description="Collection of key-value pairs that represent custom data to add to the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes.")
    export_bucket_id: str = Field(alias="exportBucketId", description="Unique 24-hexadecimal character string that identifies the Export Bucket.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    snapshot_id: str = Field(alias="snapshotId", description="Unique 24-hexadecimal character string that identifies the Cloud Backup Snapshot to export.")
