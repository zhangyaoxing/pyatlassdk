"""Generated model for DiskBackupTimeBasedCopyPolicyItem. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupTimeBasedCopyPolicyItem(BaseModel):
    """Specifications for one time-based copy policy item."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    frequency_type: Literal["daily", "hourly", "weekly", "monthly", "yearly", "ondemand"] = Field(alias="frequencyType", description="Human-readable label that identifies the frequency type associated with the copy policy.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this copy policy item.")
    retention_unit: Literal["days", "weeks", "months", "years"] = Field(alias="retentionUnit", description="Unit of time in which MongoDB Cloud measures snapshot copy retention.")
    retention_value: int = Field(alias="retentionValue", description="Duration in days, weeks, months, or years that MongoDB Cloud retains the snapshot copy.")
