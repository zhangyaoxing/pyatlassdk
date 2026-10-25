"""Generated model for AllEnvironmentValues. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.all_environment_values_values import AllEnvironmentValuesValues

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AllEnvironmentValues(BaseModel):
    """Generated model for AllEnvironmentValues."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    values: AllEnvironmentValuesValues | None = Field(default=None, description="An object that maps each possible environment name to\ndefinitions of the environment values available in that\nenvironment.")
