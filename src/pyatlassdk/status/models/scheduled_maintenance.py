"""Generated model for ScheduledMaintenance. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.status.models.incident_update import IncidentUpdate

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledMaintenance(BaseModel):
    """Generated model for ScheduledMaintenance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime = Field(description="Timestamp when created (ISO 8601)")
    id: str = Field(description="Unique maintenance identifier")
    impact: Literal["none", "minor", "major", "critical", "maintenance"] = Field(description="Impact level")
    incident_updates: list[IncidentUpdate] = Field(description="List of updates")
    monitoring_at: datetime | None = Field(default=None, description="Timestamp when monitoring started (ISO 8601)")
    name: str = Field(description="Maintenance name")
    page_id: str = Field(description="Unique page identifier")
    postmortem_body: str | None = Field(default=None, description="Postmortem body")
    postmortem_body_last_updated_at: datetime | None = Field(default=None, description="Timestamp when the postmortem was last updated (ISO 8601)")
    postmortem_ignored: bool | None = Field(default=None, description="Whether the postmortem is ignored")
    postmortem_notified_subscribers: bool | None = Field(default=None, description="Whether subscribers were notified of the postmortem")
    postmortem_published_at: datetime | None = Field(default=None, description="Timestamp when the postmortem was published (ISO 8601)")
    resolved_at: datetime | None = Field(default=None, description="Timestamp when the maintenance was resolved (ISO 8601)")
    scheduled_for: datetime = Field(description="Scheduled start (ISO 8601)")
    scheduled_remind_prior: bool | None = Field(default=None, description="Whether to send reminders prior to the scheduled maintenance")
    scheduled_reminded_at: datetime | None = Field(default=None, description="Timestamp when reminders were sent (ISO 8601)")
    scheduled_until: datetime = Field(description="Scheduled end time (ISO 8601)")
    shortlink: str = Field(description="Short URL for the maintenance")
    status: Literal["scheduled", "in_progress", "verifying", "completed"] = Field(description="Current maintenance status")
    updated_at: datetime = Field(description="Timestamp when the maintenance was last updated (ISO 8601)")
