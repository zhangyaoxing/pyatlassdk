"""Generated model for StatusIndicator. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StatusIndicator(BaseModel):
    """Generated model for StatusIndicator."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str = Field(description="Human-readable description")
    indicator: Literal["none", "minor", "major", "critical"] = Field(description="Status indicator level")
