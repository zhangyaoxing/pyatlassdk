"""Generated model for OnlineArchiveSchedule. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.daily_schedule_view import DailyScheduleView
from pyatlassdk.admin.models.default_schedule_view import DefaultScheduleView
from pyatlassdk.admin.models.monthly_schedule_view import MonthlyScheduleView
from pyatlassdk.admin.models.weekly_schedule_view import WeeklyScheduleView

OnlineArchiveSchedule: TypeAlias = DefaultScheduleView | DailyScheduleView | WeeklyScheduleView | MonthlyScheduleView
