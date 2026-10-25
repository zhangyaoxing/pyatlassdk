"""Generated model for AllEnvironmentValuesValues. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.specific_environment_values import SpecificEnvironmentValues

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AllEnvironmentValuesValues(BaseModel):
    """Generated model for AllEnvironmentValuesValues."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    none: SpecificEnvironmentValues | None = None
    development: SpecificEnvironmentValues | None = None
    testing: SpecificEnvironmentValues | None = None
    qa: SpecificEnvironmentValues | None = None
    production: SpecificEnvironmentValues | None = None
