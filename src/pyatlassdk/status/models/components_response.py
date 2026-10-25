"""Generated model for ComponentsResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.status.models.component import Component
from pyatlassdk.status.models.page_info import PageInfo

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ComponentsResponse(BaseModel):
    """Generated model for ComponentsResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    page: PageInfo
    components: list[Component] = Field(description="List of components")
