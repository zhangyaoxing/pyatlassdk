"""Generated model for DiskGBAutoScaling. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskGBAutoScaling(BaseModel):
    """Setting that enables disk auto-scaling."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether this cluster enables disk auto-scaling. The maximum memory allowed for the selected cluster tier and the oplog size can limit storage auto-scaling.")
