"""Generated model for EventTypeDetails. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class EventTypeDetails(BaseModel):
    """A singular type of event."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    alertable: bool | None = Field(default=None, description="Whether or not this event type can be configured as an alert via the API.")
    description: str | None = Field(default=None, description="Description of the event type.")
    event_type: str | None = Field(default=None, alias="eventType", description="Enum representation of the event type.")
