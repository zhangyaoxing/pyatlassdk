"""Generated model for DailyScheduleView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DailyScheduleView(BaseModel):
    """Regular frequency and duration when archiving process occurs."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["DEFAULT", "DAILY", "WEEKLY", "MONTHLY"] = Field(description="Type of schedule.")
    end_hour: int | None = Field(default=None, alias="endHour", description="Hour of the day when the scheduled window to run one online archive ends. This field uses the UTC time zone. The window must have a duration of at least two hours. If the end time is before or equal to the start time, the window extends to the next day.")
    end_minute: int | None = Field(default=None, alias="endMinute", description="Minute of the hour when the scheduled window to run one online archive ends. This field uses the UTC time zone. The window must have a duration of at least two hours. If the end time is before or equal to the start time, the window extends to the next day.")
    start_hour: int | None = Field(default=None, alias="startHour", description="Hour of the day when the scheduled window to run one online archive starts. This field uses the UTC time zone.")
    start_minute: int | None = Field(default=None, alias="startMinute", description="Minute of the hour when the scheduled window to run one online archive starts. This field uses the UTC time zone.")
