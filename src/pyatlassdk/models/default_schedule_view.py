"""Generated model for DefaultScheduleView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DefaultScheduleView(BaseModel):
    """Regular frequency and duration when archiving process occurs."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["DEFAULT", "DAILY", "WEEKLY", "MONTHLY"] = Field(description="Type of schedule.")
