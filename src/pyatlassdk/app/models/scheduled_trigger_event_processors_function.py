"""Generated model for ScheduledTriggerEventProcessorsFUNCTION. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.scheduled_trigger_event_processors_function_config import ScheduledTriggerEventProcessorsFUNCTIONConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledTriggerEventProcessorsFUNCTION(BaseModel):
    """Generated model for ScheduledTriggerEventProcessorsFUNCTION."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: ScheduledTriggerEventProcessorsFUNCTIONConfig | None = None
