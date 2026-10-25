"""Generated model for ExtraRetentionSetting. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ExtraRetentionSetting(BaseModel):
    """Extra retention setting item in the desired backup policy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    frequency_type: Annotated[Literal["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY", "ON_DEMAND"], BeforeValidator(upper_case)] | None = Field(default=None, alias="frequencyType", description="The frequency type for the extra retention settings for the cluster.")
    retention_days: int | None = Field(default=None, alias="retentionDays", description="The number of extra retention days for the cluster.")
