"""Generated model for WeeklyScheduleView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class WeeklyScheduleView(BaseModel):
    """Regular frequency and duration when archiving process occurs."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Annotated[Literal["DEFAULT", "DAILY", "WEEKLY", "MONTHLY"], BeforeValidator(upper_case)] = Field(description="Type of schedule.")
    day_of_week: int | None = Field(default=None, alias="dayOfWeek", description="Day of the week when the scheduled archive starts. The week starts with Monday (`1`) and ends with Sunday (`7`).")
    end_hour: int | None = Field(default=None, alias="endHour", description="Hour of the day when the scheduled window to run one online archive ends. This field uses the UTC time zone. The window must have a duration of at least two hours. If the end time is before or equal to the start time, the window extends to the next day.")
    end_minute: int | None = Field(default=None, alias="endMinute", description="Minute of the hour when the scheduled window to run one online archive ends. This field uses the UTC time zone. The window must have a duration of at least two hours. If the end time is before or equal to the start time, the window extends to the next day.")
    start_hour: int | None = Field(default=None, alias="startHour", description="Hour of the day when the scheduled window to run one online archive starts. This field uses the UTC time zone.")
    start_minute: int | None = Field(default=None, alias="startMinute", description="Minute of the hour when the scheduled window to run one online archive starts. This field uses the UTC time zone.")
