"""Generated model for DatabaseTriggerEventProcessorsFUNCTION. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.database_trigger_event_processors_function_config import DatabaseTriggerEventProcessorsFUNCTIONConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerEventProcessorsFUNCTION(BaseModel):
    """Generated model for DatabaseTriggerEventProcessorsFUNCTION."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: DatabaseTriggerEventProcessorsFUNCTIONConfig | None = None
