"""Generated model for ScheduledTriggerConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledTriggerConfig(BaseModel):
    """Generated model for ScheduledTriggerConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    schedule: str = Field(description="A [cron expression](https://www.mongodb.com/docs/atlas/app-services/triggers/scheduled-triggers/#cron-expressions) that specifies when the trigger executes.")
    skip_catchup_events: bool | None = Field(default=None, description="If `true`, enabling the trigger after it was disabled\nwill not invoke events that occurred while the trigger\nwas disabled.")
