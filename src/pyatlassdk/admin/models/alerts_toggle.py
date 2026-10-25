"""Generated model for AlertsToggle. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AlertsToggle(BaseModel):
    """Enables or disables the specified alert configuration in the specified project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether to enable or disable the specified alert configuration in the specified project.")
