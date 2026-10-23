"""Generated model for BackupSnapshot. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.api_bson_timestamp_view import ApiBSONTimestampView
from pyatlassdk.models.backup_snapshot_part import BackupSnapshotPart
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BackupSnapshot(BaseModel):
    """Generated model for BackupSnapshot."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the snapshots you want to return.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster.")
    complete: bool | None = Field(default=None, description="Flag that indicates whether the snapshot exists. This flag returns `false` while MongoDB Cloud creates the snapshot.")
    created: ApiBSONTimestampView | None = None
    do_not_delete: bool | None = Field(default=None, alias="doNotDelete", description="Flag that indicates whether someone can delete this snapshot. You can't set `\"doNotDelete\" : true` and set a timestamp for **expires** in the same request.")
    expires: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud deletes the snapshot. If `\"doNotDelete\" : true`, MongoDB Cloud removes any value set for this parameter. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns the snapshots.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the snapshot.")
    incremental: bool | None = Field(default=None, description="Flag indicating if this is an incremental or a full snapshot.")
    last_oplog_applied_timestamp: ApiBSONTimestampView | None = Field(default=None, alias="lastOplogAppliedTimestamp")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    parts: list[BackupSnapshotPart] | None = Field(default=None, description="Metadata that describes the complete snapshot.\n\n- For a replica set, this array contains a single document.\n- For a sharded cluster, this array contains one document for each shard plus one document for the config host.")
