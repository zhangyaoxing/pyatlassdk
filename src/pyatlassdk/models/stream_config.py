"""Generated model for StreamConfig. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class StreamConfig(BaseModel):
    """Configuration options for an Atlas Stream Processing Workspace."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    max_tier_size: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] | None = Field(default=None, alias="maxTierSize", description="Max tier size for the Stream Workspace. Configures Memory or VCPU allowances.")
    tier: Literal["SP50", "SP30", "SP10", "SP5", "SP2"] | None = Field(default=None, description="Selected tier for the Stream Workspace. Configures Memory or VCPU allowances.")
