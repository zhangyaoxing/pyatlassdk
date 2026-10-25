"""Generated model for IncidentsResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.status.models.incident import Incident
from pyatlassdk.status.models.page_info import PageInfo

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class IncidentsResponse(BaseModel):
    """Generated model for IncidentsResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    page: PageInfo
    incidents: list[Incident] = Field(description="List of incidents")
