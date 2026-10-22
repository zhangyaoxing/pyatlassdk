"""Generated model for DiskBackupCopyPolicyItem. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.disk_backup_on_demand_copy_policy_item import DiskBackupOnDemandCopyPolicyItem
from pyatlassdk.models.disk_backup_time_based_copy_policy_item import DiskBackupTimeBasedCopyPolicyItem

DiskBackupCopyPolicyItem: TypeAlias = DiskBackupOnDemandCopyPolicyItem | DiskBackupTimeBasedCopyPolicyItem
