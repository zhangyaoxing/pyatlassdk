"""Generated model for IncidentUpdate. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class IncidentUpdate(BaseModel):
    """Generated model for IncidentUpdate."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    body: str = Field(description="Update message")
    created_at: datetime = Field(description="Timestamp when the update was created (ISO 8601)")
    display_at: datetime | None = Field(description="Timestamp for display (ISO 8601)")
    id: str = Field(description="Unique update identifier")
    incident_id: str = Field(description="Unique incident identifier")
    status: Literal["investigating", "identified", "monitoring", "resolved", "postmortem", "scheduled", "in_progress", "verifying", "completed"] = Field(description="Update status")
    updated_at: datetime = Field(description="Timestamp when the update was last modified (ISO 8601)")
