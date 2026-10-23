"""Generated model for ComponentLabel. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ComponentLabel(BaseModel):
    """Human-readable labels applied to this MongoDB Cloud component."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    key: str | None = Field(default=None, description="Key applied to tag and categorize this component.")
    value: str | None = Field(default=None, description="Value set to the Key applied to tag and categorize this component.")
