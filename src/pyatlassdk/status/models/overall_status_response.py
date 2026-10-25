"""Generated model for OverallStatusResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.status.models.page_info import PageInfo
from pyatlassdk.status.models.status_indicator import StatusIndicator

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OverallStatusResponse(BaseModel):
    """Generated model for OverallStatusResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    page: PageInfo
    status: StatusIndicator
