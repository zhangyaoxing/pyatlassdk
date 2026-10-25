"""Generated model for EnvironmentValue. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.environment_value_values import EnvironmentValueValues

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EnvironmentValue(BaseModel):
    """Generated model for EnvironmentValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The environment value's internal ID")
    name: str | None = Field(default=None, description="The environment value name")
    last_modified: float | None = Field(default=None, description="The time this configuration was last modified represented by the number of seconds since the UNIX epoch.")
    values: EnvironmentValueValues | None = Field(default=None, description="An object that maps environment names to values. The\nenvironment value resolves to the current active\nenvironment's mapped value.\n\nIf no value is mapped to the current active environment,\nthe environment value resolves to `undefined`.")
