"""Generated model for ProtectedHours. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ProtectedHours(BaseModel):
    """Defines the a window where maintenance will not begin within."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    end_hour_of_day: int | None = Field(default=None, alias="endHourOfDay", description="Zero-based integer, in the project's configured time zone (see `timeZoneId`), that represents the end hour of the day that maintenance will not begin in.")
    start_hour_of_day: int | None = Field(default=None, alias="startHourOfDay", description="Zero-based integer, in the project's configured time zone (see `timeZoneId`), that represents the beginning hour of the day that maintenance will not begin in.")
