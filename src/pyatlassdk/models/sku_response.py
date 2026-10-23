"""Generated model for SkuResponse. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SkuResponse(BaseModel):
    """Generated model for SkuResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Human-readable short summary of what this SKU represents.")
    id: str | None = Field(default=None, description="Unique string that identifies the SKU.")
