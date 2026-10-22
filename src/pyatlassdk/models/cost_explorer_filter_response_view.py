"""Generated model for CostExplorerFilterResponseView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class CostExplorerFilterResponseView(BaseModel):
    """Response object to give information about created query."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    token: str | None = Field(default=None, description="The token used to identify the created Cost Explorer query.")
