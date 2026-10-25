"""Generated model for AdvancedDiskBackupSnapshotSchedulePolicy. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.disk_backup_api_policy_item import DiskBackupApiPolicyItem

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdvancedDiskBackupSnapshotSchedulePolicy(BaseModel):
    """List that contains a document for each backup policy item in the desired backup policy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this backup policy.")
    policy_items: list[DiskBackupApiPolicyItem] = Field(alias="policyItems", description="List that contains the specifications for one policy.")
