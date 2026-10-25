"""Generated model for Dependency. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Dependency(BaseModel):
    """Generated model for Dependency."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="The name of the uploaded dependency.")
    version: str | None = Field(default=None, description="The version of the uploaded dependency.")
