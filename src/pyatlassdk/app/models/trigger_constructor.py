"""Generated model for TriggerConstructor. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.authentication_trigger import AuthenticationTrigger
from pyatlassdk.app.models.database_trigger import DatabaseTrigger
from pyatlassdk.app.models.scheduled_trigger import ScheduledTrigger

TriggerConstructor: TypeAlias = DatabaseTrigger | AuthenticationTrigger | ScheduledTrigger
