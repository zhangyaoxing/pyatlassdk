"""Generated model for DiskBackupExportJob. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.backup_label import BackupLabel
from pyatlassdk.models.disk_backup_export_member import DiskBackupExportMember
from pyatlassdk.models.export_status import ExportStatus
from pyatlassdk.models.link import Link
from pyatlassdk.models.state_reason import StateReason

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupExportJob(BaseModel):
    """Generated model for DiskBackupExportJob."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    components: list[DiskBackupExportMember] | None = Field(default=None, description="Information on the export job for each replica set in the sharded cluster.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when a user or Atlas created the Export Job. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    custom_data: list[BackupLabel] | None = Field(default=None, alias="customData", description="Collection of key-value pairs that represent custom data for the metadata file that MongoDB Cloud uploads when the Export Job finishes.")
    export_bucket_id: str = Field(alias="exportBucketId", description="Unique 24-hexadecimal character string that identifies the Export Bucket.")
    export_status: ExportStatus | None = Field(default=None, alias="exportStatus")
    finished_at: datetime | None = Field(default=None, alias="finishedAt", description="Date and time when this Export Job completed. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies the restore job.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    prefix: str | None = Field(default=None, description="Prefix used for all blob storage objects uploaded as part of the Export Job.")
    snapshot_id: str | None = Field(default=None, alias="snapshotId", description="Unique 24-hexadecimal character string that identifies the snapshot.")
    state: Literal["Cancelled", "Failed", "InProgress", "Queued", "Successful"] | None = Field(default=None, description="State of the Export Job.")
    state_reason: StateReason | None = Field(default=None, alias="stateReason")
