"""Generated model for ApiKey. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiKey(BaseModel):
    """Generated model for ApiKey."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    key: str | None = None
    name: str | None = None
    disabled: str | None = None
