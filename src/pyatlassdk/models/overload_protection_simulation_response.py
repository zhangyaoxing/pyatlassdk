"""Generated model for OverloadProtectionSimulationResponse. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class OverloadProtectionSimulationResponse(BaseModel):
    """Overload protection simulation for a cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cancel_requested_at: datetime | None = Field(default=None, alias="cancelRequestedAt", description="Date and time when cancellation of the overload protection simulation was requested. This parameter is only present when a cancellation has been requested and expresses its value in the ISO 8601 timestamp format in UTC.")
    cluster_name: str = Field(alias="clusterName", description="Human-readable label that identifies the cluster on which the simulation is running.")
    duration_seconds: int = Field(alias="durationSeconds", description="Duration of the overload protection simulation in seconds.")
    expires_at: datetime = Field(alias="expiresAt", description="Date and time when the overload protection simulation expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal character string that identifies the project that contains the cluster.")
    request_date: datetime = Field(alias="requestDate", description="Date and time when the overload protection simulation was requested. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    simulation_id: str = Field(alias="simulationId", description="Unique identifier of the overload protection simulation.")
    state: str = Field(description="Current state of the overload protection simulation.")
