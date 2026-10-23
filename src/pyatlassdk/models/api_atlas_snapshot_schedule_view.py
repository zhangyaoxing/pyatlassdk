"""Generated model for ApiAtlasSnapshotScheduleView. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasSnapshotScheduleView(BaseModel):
    """Generated model for ApiAtlasSnapshotScheduleView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_checkpoint_interval_min: Literal[15, 30, 60] = Field(alias="clusterCheckpointIntervalMin", description="Quantity of time expressed in minutes between successive cluster checkpoints. This parameter applies only to sharded clusters. This number determines the granularity of continuous cloud backups for sharded clusters.")
    cluster_id: str = Field(alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the snapshot you want to return.")
    daily_snapshot_retention_days: Literal[0, 3, 4, 5, 6, 7, 15, 30, 60, 90, 120, 180, 360] = Field(alias="dailySnapshotRetentionDays", description="Quantity of time to keep daily snapshots. MongoDB Cloud expresses this value in days. Set this value to `0` to disable daily snapshot retention.")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the cluster.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    monthly_snapshot_retention_months: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 24, 36] = Field(alias="monthlySnapshotRetentionMonths", description="Number of months that MongoDB Cloud must keep monthly snapshots. Set this value to `0` to disable monthly snapshot retention.")
    point_in_time_window_hours: int = Field(alias="pointInTimeWindowHours", description="Number of hours before the current time from which MongoDB Cloud can create a Continuous Cloud Backup snapshot.")
    snapshot_interval_hours: Literal[6, 8, 12, 24] = Field(alias="snapshotIntervalHours", description="Number of hours that must elapse before taking another snapshot.")
    snapshot_retention_days: Literal[2, 3, 4, 5] = Field(alias="snapshotRetentionDays", description="Number of days that MongoDB Cloud must keep recent snapshots.")
    weekly_snapshot_retention_weeks: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 52] = Field(alias="weeklySnapshotRetentionWeeks", description="Number of weeks that MongoDB Cloud must keep weekly snapshots. Set this value to `0` to disable weekly snapshot retention.")
