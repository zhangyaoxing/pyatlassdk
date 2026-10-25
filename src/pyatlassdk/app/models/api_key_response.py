"""Generated model for ApiKeyResponse. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiKeyResponse(BaseModel):
    """Generated model for ApiKeyResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    name: str | None = None
    disabled: str | None = None
