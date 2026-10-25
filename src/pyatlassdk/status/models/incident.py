"""Generated model for Incident. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.status.models.incident_update import IncidentUpdate

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Incident(BaseModel):
    """Generated model for Incident."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime = Field(description="Timestamp when the incident was created (ISO 8601)")
    id: str = Field(description="Unique identifier for the incident")
    impact: Literal["none", "minor", "major", "critical", "maintenance"] = Field(description="Impact level")
    incident_updates: list[IncidentUpdate] = Field(description="List of updates for the incident")
    monitoring_at: datetime | None = Field(default=None, description="Timestamp when monitoring started (ISO 8601)")
    name: str = Field(description="Incident name")
    page_id: str = Field(description="Unique page identifier")
    postmortem_body: str | None = Field(default=None, description="Postmortem analysis body")
    postmortem_body_last_updated_at: datetime | None = Field(default=None, description="Timestamp when postmortem was last updated (ISO 8601)")
    postmortem_ignored: bool | None = Field(default=None, description="Whether postmortem is ignored")
    postmortem_notified_subscribers: bool | None = Field(default=None, description="Whether subscribers were notified of postmortem")
    postmortem_published_at: datetime | None = Field(default=None, description="Timestamp when postmortem was published (ISO 8601)")
    resolved_at: datetime | None = Field(default=None, description="Timestamp when the incident was resolved (ISO 8601)")
    scheduled_for: datetime | None = Field(default=None, description="Scheduled start time (for maintenances) (ISO 8601)")
    scheduled_remind_prior: bool | None = Field(default=None, description="Whether to send reminders prior to the scheduled time")
    scheduled_reminded_at: datetime | None = Field(default=None, description="Timestamp when reminders were sent (ISO 8601)")
    scheduled_until: datetime | None = Field(default=None, description="Scheduled end time (ISO 8601)")
    shortlink: str = Field(description="Short URL for the incident")
    status: Literal["investigating", "identified", "monitoring", "resolved", "postmortem"] = Field(description="Current incident status")
    updated_at: datetime = Field(description="Timestamp when the incident was last updated (ISO 8601)")
