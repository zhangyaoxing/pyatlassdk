"""Generated model for Trigger. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Trigger(BaseModel):
    """Generated model for Trigger."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The trigger's unique ID.")
