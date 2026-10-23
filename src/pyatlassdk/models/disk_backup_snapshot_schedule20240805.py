"""Generated model for DiskBackupSnapshotSchedule20240805. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.advanced_disk_backup_snapshot_schedule_policy import AdvancedDiskBackupSnapshotSchedulePolicy
from pyatlassdk.models.auto_export_policy_view import AutoExportPolicyView
from pyatlassdk.models.delete_copied_backups20240805 import DeleteCopiedBackups20240805
from pyatlassdk.models.disk_backup_copy_setting20240805 import DiskBackupCopySetting20240805
from pyatlassdk.models.extra_retention_setting import ExtraRetentionSetting
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupSnapshotSchedule20240805(BaseModel):
    """Generated model for DiskBackupSnapshotSchedule20240805."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_copy_settings_enabled: bool | None = Field(default=None, alias="autoCopySettingsEnabled", description="Flag that indicates whether the copy settings are automatically managed by MongoDB Cloud and sync to the cluster topology.")
    auto_export_enabled: bool | None = Field(default=None, alias="autoExportEnabled", description="Flag that indicates whether MongoDB Cloud automatically exports Cloud Backup Snapshots to the Export Bucket.")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the Snapshot you want to return.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster with the Snapshot you want to return.")
    copy_policy_items_enabled: bool | None = Field(default=None, alias="copyPolicyItemsEnabled", description="Flag that indicates whether copy settings use `copyPolicyItems` instead of `frequencies`. When true, requests must supply `copyPolicyItems` and responses return `copyPolicyItems` only. When false or omitted, requests must supply `frequencies` and responses return `frequencies` only.")
    copy_settings: list[DiskBackupCopySetting20240805] | None = Field(default=None, alias="copySettings", description="List that contains a document for each copy setting item in the desired backup policy.")
    delete_copied_backups: list[DeleteCopiedBackups20240805] | None = Field(default=None, alias="deleteCopiedBackups", description="List that contains a document for each deleted copy setting whose backup copies you want to delete.")
    delete_copy_snapshots: bool | None = Field(default=None, alias="deleteCopySnapshots", description="Flag that indicates whether to delete Snapshot copies that MongoDB Cloud took previously when their associated `copyPolicyItems` are removed from a `copySetting`. This option requires `copyPolicyItemsEnabled` to be true.")
    delete_snapshots: bool | None = Field(default=None, alias="deleteSnapshots", description="Flag that indicates whether to delete Snapshots that MongoDB Cloud took previously when deleting the associated backup policy.")
    export: AutoExportPolicyView | None = None
    extra_retention_settings: list[ExtraRetentionSetting] | None = Field(default=None, alias="extraRetentionSettings", description="List that contains a document for each extra retention setting item in the desired backup policy.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    next_snapshot: datetime | None = Field(default=None, alias="nextSnapshot", description="Date and time when MongoDB Cloud takes the next Snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    policies: list[AdvancedDiskBackupSnapshotSchedulePolicy] = Field(description="Rules set for this backup schedule.")
    reference_hour_of_day: int | None = Field(default=None, alias="referenceHourOfDay", description="Hour of day in Coordinated Universal Time (UTC) that represents when MongoDB Cloud takes the Snapshot.")
    reference_minute_of_hour: int | None = Field(default=None, alias="referenceMinuteOfHour", description="Minute of the `referenceHourOfDay` that represents when MongoDB Cloud takes the Snapshot.")
    restore_window_days: int | None = Field(default=None, alias="restoreWindowDays", description="Number of previous days that you can restore back to with Continuous Cloud Backup accuracy. You must specify a positive, non-zero integer. This parameter applies to continuous Cloud Backups only.")
    update_copy_snapshots: bool | None = Field(default=None, alias="updateCopySnapshots", description="Flag that indicates whether to apply the retention changes for updated copy policy items to Snapshot copies that MongoDB Cloud took previously.")
    update_snapshots: bool | None = Field(default=None, alias="updateSnapshots", description="Flag that indicates whether to apply the retention changes in the updated backup policy to Snapshots that MongoDB Cloud took previously.")
    use_org_and_group_names_in_export_prefix: bool | None = Field(default=None, alias="useOrgAndGroupNamesInExportPrefix", description="Flag that indicates whether to use organization and project names instead of organization and project UUIDs in the path to the metadata files that MongoDB Cloud uploads to your Export Bucket.")
