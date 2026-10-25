"""Generated model for DiskBackupSnapshotRestoreJob. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.admin.models.api_bson_timestamp_view import ApiBSONTimestampView
from pyatlassdk.admin.models.api_private_download_delivery_url import ApiPrivateDownloadDeliveryUrl
from pyatlassdk.admin.models.disk_backup_restore_member import DiskBackupRestoreMember
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupSnapshotRestoreJob(BaseModel):
    """Generated model for DiskBackupSnapshotRestoreJob."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cancelled: bool | None = Field(default=None, description="Flag that indicates whether someone canceled this restore job.")
    components: list[DiskBackupRestoreMember] | None = Field(default=None, description="Information on the restore job for each replica set in the sharded cluster.")
    delivery_type: Literal["automated", "download", "pointInTime"] = Field(alias="deliveryType", description="Human-readable label that categorizes the restore job to create.")
    delivery_url: list[str] | None = Field(default=None, alias="deliveryUrl", description="One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download. MongoDB Cloud returns this parameter when `\"deliveryType\" : \"download\"`.")
    desired_timestamp: ApiBSONTimestampView | None = Field(default=None, alias="desiredTimestamp")
    expired: bool | None = Field(default=None, description="Flag that indicates whether the restore job expired.")
    expires_at: datetime | None = Field(default=None, alias="expiresAt", description="Date and time when the restore job expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    failed: bool | None = Field(default=None, description="Flag that indicates whether the restore job failed.")
    finished_at: datetime | None = Field(default=None, alias="finishedAt", description="Date and time when the restore job completed. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies the restore job.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    oplog_inc: int | None = Field(default=None, alias="oplogInc", description="Oplog operation number from which you want to restore this snapshot. This number represents the second part of an Oplog timestamp. The resource returns this parameter when `\"deliveryType\" : \"pointInTime\"` and `oplogTs` exceeds `0`.")
    oplog_ts: int | None = Field(default=None, alias="oplogTs", description="Date and time from which you want to restore this snapshot. This parameter expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch. This number represents the first part of an Oplog timestamp. The resource returns this parameter when `\"deliveryType\" : \"pointInTime\"` and `oplogTs` exceeds `0`.")
    point_in_time_utc_seconds: int | None = Field(default=None, alias="pointInTimeUTCSeconds", description="Date and time from which MongoDB Cloud restored this snapshot. This parameter expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch. The resource returns this parameter when `\"deliveryType\" : \"pointInTime\"` and `pointInTimeUTCSeconds` exceeds `0`.")
    private_download_delivery_urls: list[ApiPrivateDownloadDeliveryUrl] | None = Field(default=None, alias="privateDownloadDeliveryUrls", description="One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download and the corresponding private endpoint(s). MongoDB Cloud returns this parameter when `\"deliveryType\" : \"download\"` and the download can be performed privately.")
    snapshot_id: str | None = Field(default=None, alias="snapshotId", description="Unique 24-hexadecimal character string that identifies the snapshot.")
    target_cluster_name: str | None = Field(default=None, alias="targetClusterName", description="Human-readable label that identifies the target cluster to which the restore job restores the snapshot. The resource returns this parameter when `\"deliveryType\":` `\"automated\"`. Required for `automated` and `pointInTime` restore types.")
    target_group_id: str | None = Field(default=None, alias="targetGroupId", description="Unique 24-hexadecimal digit string that identifies the target project for the specified `targetClusterName`. Required for `automated` and `pointInTime` restore types.")
    timestamp: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud took the snapshot associated with `snapshotId`. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
