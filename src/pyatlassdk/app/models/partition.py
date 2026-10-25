"""Generated model for Partition. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Partition(BaseModel):
    """Generated model for Partition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    key: str | None = None
    type: str | None = None
