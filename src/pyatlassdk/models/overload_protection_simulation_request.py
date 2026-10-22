"""Generated model for OverloadProtectionSimulationRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class OverloadProtectionSimulationRequest(BaseModel):
    """Request to start an overload protection simulation for a cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    duration_seconds: int = Field(alias="durationSeconds", description="Duration of the overload protection simulation in seconds.")
