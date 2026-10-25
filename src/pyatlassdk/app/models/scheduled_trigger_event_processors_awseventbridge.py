"""Generated model for ScheduledTriggerEventProcessorsAWSEVENTBRIDGE. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.scheduled_trigger_event_processors_awseventbridge_config import ScheduledTriggerEventProcessorsAWSEVENTBRIDGEConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledTriggerEventProcessorsAWSEVENTBRIDGE(BaseModel):
    """Generated model for ScheduledTriggerEventProcessorsAWSEVENTBRIDGE."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: ScheduledTriggerEventProcessorsAWSEVENTBRIDGEConfig | None = None
