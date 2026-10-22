"""Generated model for DiskBackupApiPolicyItem. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DiskBackupApiPolicyItem(BaseModel):
    """Specifications for one policy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    frequency_interval: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 40] = Field(alias="frequencyInterval", description="Number that indicates the frequency interval for a set of Snapshots. A value of `1` specifies the first instance of the corresponding `frequencyType`.\n\n- In a yearly policy item, `1` indicates that the yearly Snapshot occurs on the first day of January and `12` indicates the first day of December.\n\n- In a monthly policy item, `1` indicates that the monthly Snapshot occurs on the first day of the month and `40` indicates the last day of the month.\n\n- In a weekly policy item, `1` indicates that the weekly Snapshot occurs on Monday and `7` indicates Sunday.\n\n- In an hourly policy item, you can set the frequency interval to `1`, `2`, `4`, `6`, `8`, or `12`. For hourly policy items for NVMe clusters, MongoDB Cloud accepts only `12` as the frequency interval value.\n\n MongoDB Cloud ignores this setting for non-hourly policy items in Backup Compliance Policy settings.")
    frequency_type: Literal["daily", "hourly", "weekly", "monthly", "yearly", "ondemand"] = Field(alias="frequencyType", description="Human-readable label that identifies the frequency type associated with the backup policy.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this backup policy item.")
    retention_unit: Literal["days", "weeks", "months", "years"] = Field(alias="retentionUnit", description="Unit of time in which MongoDB Cloud measures Snapshot retention.")
    retention_value: int = Field(alias="retentionValue", description="Duration in days, weeks, months, or years that MongoDB Cloud retains the Snapshot. For less frequent policy items, MongoDB Cloud requires that you specify a value greater than or equal to the value specified for more frequent policy items.\n\nFor example: If the hourly policy item specifies a retention of two days, you must specify two days or greater for the retention of the weekly policy item.")
