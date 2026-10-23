"""Generated model for PrivateIPModeView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PrivateIPModeView(BaseModel):
    """Generated model for PrivateIPModeView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool = Field(description="Flag that indicates whether someone enabled **Connect via Peering Only** mode for the specified project.")
