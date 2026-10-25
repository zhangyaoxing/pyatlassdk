"""Generated model for AuthenticationTriggerEventProcessors. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.authentication_trigger_event_processors_awseventbridge import AuthenticationTriggerEventProcessorsAWSEVENTBRIDGE
from pyatlassdk.app.models.authentication_trigger_event_processors_function import AuthenticationTriggerEventProcessorsFUNCTION

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthenticationTriggerEventProcessors(BaseModel):
    """Generated model for AuthenticationTriggerEventProcessors."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    function: AuthenticationTriggerEventProcessorsFUNCTION | None = Field(default=None, alias="FUNCTION")
    aws_eventbridge: AuthenticationTriggerEventProcessorsAWSEVENTBRIDGE | None = Field(default=None, alias="AWS_EVENTBRIDGE")
