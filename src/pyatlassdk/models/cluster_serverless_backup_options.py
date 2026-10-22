"""Generated model for ClusterServerlessBackupOptions. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ClusterServerlessBackupOptions(BaseModel):
    """Group of settings that configure serverless backup."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    serverless_continuous_backup_enabled: bool | None = Field(default=None, alias="serverlessContinuousBackupEnabled", description="Flag that indicates whether the serverless instance uses **Serverless Continuous Backup**.\n If this parameter is `false`, the serverless instance uses **Basic Backup**.\n\n | Option | Description |\n |---|---|\n | Serverless Continuous Backup | Atlas takes incremental [snapshots](https://www.mongodb.com/docs/atlas/backup/cloud-backup/overview/#std-label-serverless-snapshots) of the data in your serverless instance every six hours and lets you restore the data from a selected point in time within the last 72 hours. Atlas also takes daily snapshots and retains these daily snapshots for 35 days. To learn more, see [Serverless Instance Costs](https://www.mongodb.com/docs/atlas/billing/serverless-instance-costs/#std-label-serverless-instance-costs). |\n | Basic Backup | Atlas takes incremental [snapshots](https://www.mongodb.com/docs/atlas/backup/cloud-backup/overview/#std-label-serverless-snapshots) of the data in your serverless instance every six hours and retains only the two most recent snapshots. You can use this option for free. |")
