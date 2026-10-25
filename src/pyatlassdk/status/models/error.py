"""Generated model for Error. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Error(BaseModel):
    """Generated model for Error."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    message: str = Field(description="Error message")
    code: int | None = Field(default=None, description="Error code")
