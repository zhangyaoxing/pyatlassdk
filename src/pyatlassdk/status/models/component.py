"""Generated model for Component. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Component(BaseModel):
    """Generated model for Component."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime = Field(description="Timestamp when the component was created (ISO 8601)")
    description: str | None = Field(default=None, description="Description of the component")
    id: str = Field(description="Unique identifier for the component")
    name: str = Field(description="Name of the component")
    only_show_if_degraded: bool = Field(description="Whether to show only if degraded")
    page_id: str = Field(description="Unique page identifier")
    position: int = Field(description="Display position")
    status: Literal["operational", "degraded_performance", "partial_outage", "major_outage"] = Field(description="Current status of the component")
    updated_at: datetime = Field(description="Timestamp when the component was last updated (ISO 8601)")
