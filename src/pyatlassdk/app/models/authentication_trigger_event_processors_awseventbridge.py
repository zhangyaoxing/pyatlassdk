"""Generated model for AuthenticationTriggerEventProcessorsAWSEVENTBRIDGE. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.authentication_trigger_event_processors_awseventbridge_config import AuthenticationTriggerEventProcessorsAWSEVENTBRIDGEConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthenticationTriggerEventProcessorsAWSEVENTBRIDGE(BaseModel):
    """Generated model for AuthenticationTriggerEventProcessorsAWSEVENTBRIDGE."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: AuthenticationTriggerEventProcessorsAWSEVENTBRIDGEConfig | None = None
