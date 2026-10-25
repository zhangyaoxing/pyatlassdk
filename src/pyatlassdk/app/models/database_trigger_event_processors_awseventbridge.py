"""Generated model for DatabaseTriggerEventProcessorsAWSEVENTBRIDGE. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.database_trigger_event_processors_awseventbridge_config import DatabaseTriggerEventProcessorsAWSEVENTBRIDGEConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerEventProcessorsAWSEVENTBRIDGE(BaseModel):
    """Generated model for DatabaseTriggerEventProcessorsAWSEVENTBRIDGE."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: DatabaseTriggerEventProcessorsAWSEVENTBRIDGEConfig | None = None
