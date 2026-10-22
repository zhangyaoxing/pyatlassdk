"""Generated model for DataProtectionSettings20231001. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.backup_compliance_on_demand_policy_item import BackupComplianceOnDemandPolicyItem
from pyatlassdk.models.backup_compliance_scheduled_policy_item import BackupComplianceScheduledPolicyItem

from pydantic import BaseModel, ConfigDict, Field

class DataProtectionSettings20231001(BaseModel):
    """Generated model for DataProtectionSettings20231001."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    authorized_email: str = Field(alias="authorizedEmail", description="Email address of the user who authorized to update the Backup Compliance Policy  settings.")
    authorized_user_first_name: str = Field(alias="authorizedUserFirstName", description="First name of the user who authorized to updated the Backup Compliance Policy  settings.")
    authorized_user_last_name: str = Field(alias="authorizedUserLastName", description="Last name of the user who authorized to updated the Backup Compliance Policy  settings.")
    copy_protection_enabled: bool | None = Field(default=None, alias="copyProtectionEnabled", description="Flag that indicates whether to prevent cluster users from deleting backups copied to other regions, even if those additional snapshot regions are removed. If unspecified, this value defaults to false.")
    deletable: bool | None = Field(default=None, description="Flag that indicates whether the Backup Compliance Policy is allowed to be disabled. It is default to false and a support ticket needs to be filed to request setting to true.")
    encryption_at_rest_enabled: bool | None = Field(default=None, alias="encryptionAtRestEnabled", description="Flag that indicates whether Encryption at Rest using Customer Key  Management is required for all clusters with a Backup Compliance Policy. If unspecified, this value defaults to false.")
    on_demand_policy_item: BackupComplianceOnDemandPolicyItem | None = Field(default=None, alias="onDemandPolicyItem")
    pit_enabled: bool | None = Field(default=None, alias="pitEnabled", description="Flag that indicates whether the cluster uses Continuous Cloud Backups with a Backup Compliance Policy. If unspecified, this value defaults to false.")
    project_id: str | None = Field(default=None, alias="projectId", description="Unique 24-hexadecimal digit string that identifies the project for the Backup Compliance Policy.")
    restore_window_days: int | None = Field(default=None, alias="restoreWindowDays", description="Number of previous days that you can restore back to with Continuous Cloud Backup with a Backup Compliance Policy. You must specify a positive, non-zero integer, and the maximum retention window can't exceed the hourly retention time. This parameter applies only to Continuous Cloud Backups with a Backup Compliance Policy.")
    scheduled_policy_items: list[BackupComplianceScheduledPolicyItem] | None = Field(default=None, alias="scheduledPolicyItems", description="List that contains the specifications for one scheduled policy.")
    state: Literal["ACTIVE", "ENABLING", "UPDATING", "DISABLING"] | None = Field(default=None, description="Label that indicates the state of the Backup Compliance Policy settings. MongoDB Cloud ignores this setting when you enable or update the Backup Compliance Policy settings.")
    updated_date: datetime | None = Field(default=None, alias="updatedDate", description="ISO 8601 timestamp format in UTC that indicates when the user updated the Data Protection Policy settings. MongoDB Cloud ignores this setting when you enable or update the Backup Compliance Policy settings.")
    updated_user: str | None = Field(default=None, alias="updatedUser", description="Email address that identifies the user who updated the Backup Compliance Policy settings. MongoDB Cloud ignores this email setting when you enable or update the Backup Compliance Policy settings.")
