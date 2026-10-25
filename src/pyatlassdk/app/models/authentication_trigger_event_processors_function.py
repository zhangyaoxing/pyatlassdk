"""Generated model for AuthenticationTriggerEventProcessorsFUNCTION. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.authentication_trigger_event_processors_function_config import AuthenticationTriggerEventProcessorsFUNCTIONConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthenticationTriggerEventProcessorsFUNCTION(BaseModel):
    """Generated model for AuthenticationTriggerEventProcessorsFUNCTION."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: AuthenticationTriggerEventProcessorsFUNCTIONConfig | None = None
