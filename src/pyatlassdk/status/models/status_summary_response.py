"""Generated model for StatusSummaryResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.status.models.component import Component
from pyatlassdk.status.models.incident import Incident
from pyatlassdk.status.models.page_info import PageInfo
from pyatlassdk.status.models.scheduled_maintenance import ScheduledMaintenance
from pyatlassdk.status.models.status_indicator import StatusIndicator

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StatusSummaryResponse(BaseModel):
    """Generated model for StatusSummaryResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    page: PageInfo
    components: list[Component] = Field(description="List of component statuses")
    incidents: list[Incident] = Field(description="List of unresolved incidents")
    scheduled_maintenances: list[ScheduledMaintenance] = Field(description="List of upcoming or active scheduled maintenances")
    status: StatusIndicator
