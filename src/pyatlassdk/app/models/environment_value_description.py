"""Generated model for EnvironmentValueDescription. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EnvironmentValueDescription(BaseModel):
    """Generated model for EnvironmentValueDescription."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The environment value's internal ID")
    name: str | None = Field(default=None, description="The environment value name")
    last_modified: float | None = Field(default=None, description="The time this configuration was last modified represented by the number of seconds since the UNIX epoch.")
