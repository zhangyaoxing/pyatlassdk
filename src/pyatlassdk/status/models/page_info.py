"""Generated model for PageInfo. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PageInfo(BaseModel):
    """Generated model for PageInfo."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique identifier for the page")
    name: str = Field(description="Name of the status page")
    url: str = Field(description="URL of the status page")
    updated_at: datetime = Field(description="Timestamp when the page was last updated (ISO 8601)")
