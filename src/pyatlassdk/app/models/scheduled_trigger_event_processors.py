"""Generated model for ScheduledTriggerEventProcessors. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.scheduled_trigger_event_processors_awseventbridge import ScheduledTriggerEventProcessorsAWSEVENTBRIDGE
from pyatlassdk.app.models.scheduled_trigger_event_processors_function import ScheduledTriggerEventProcessorsFUNCTION

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledTriggerEventProcessors(BaseModel):
    """Generated model for ScheduledTriggerEventProcessors."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    function: ScheduledTriggerEventProcessorsFUNCTION | None = Field(default=None, alias="FUNCTION")
    aws_eventbridge: ScheduledTriggerEventProcessorsAWSEVENTBRIDGE | None = Field(default=None, alias="AWS_EVENTBRIDGE")
