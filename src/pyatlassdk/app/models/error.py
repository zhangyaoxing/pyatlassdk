"""Generated model for Error. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Error(BaseModel):
    """Generated model for Error."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    error: str | None = Field(default=None, description="A message that describes the error.")
    error_code: str | None = Field(default=None, description="The error type.")
