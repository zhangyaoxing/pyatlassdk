"""Generated model for ExtraRetentionSetting. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ExtraRetentionSetting(BaseModel):
    """Extra retention setting item in the desired backup policy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    frequency_type: Literal["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY", "ON_DEMAND"] | None = Field(default=None, alias="frequencyType", description="The frequency type for the extra retention settings for the cluster.")
    retention_days: int | None = Field(default=None, alias="retentionDays", description="The number of extra retention days for the cluster.")
