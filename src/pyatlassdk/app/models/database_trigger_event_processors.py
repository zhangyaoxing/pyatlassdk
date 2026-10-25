"""Generated model for DatabaseTriggerEventProcessors. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.database_trigger_event_processors_awseventbridge import DatabaseTriggerEventProcessorsAWSEVENTBRIDGE
from pyatlassdk.app.models.database_trigger_event_processors_function import DatabaseTriggerEventProcessorsFUNCTION

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerEventProcessors(BaseModel):
    """Generated model for DatabaseTriggerEventProcessors."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    function: DatabaseTriggerEventProcessorsFUNCTION | None = Field(default=None, alias="FUNCTION")
    aws_eventbridge: DatabaseTriggerEventProcessorsAWSEVENTBRIDGE | None = Field(default=None, alias="AWS_EVENTBRIDGE")
