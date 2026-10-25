"""Generated model for ScheduledMaintenancesResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.status.models.page_info import PageInfo
from pyatlassdk.status.models.scheduled_maintenance import ScheduledMaintenance

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledMaintenancesResponse(BaseModel):
    """Generated model for ScheduledMaintenancesResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    page: PageInfo
    scheduled_maintenances: list[ScheduledMaintenance] = Field(description="List of scheduled maintenances")
