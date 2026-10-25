"""Generated model for EnvironmentValueValues. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.any_value import AnyValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EnvironmentValueValues(BaseModel):
    """Generated model for EnvironmentValueValues."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    none: AnyValue | None = None
    development: AnyValue | None = None
    testing: AnyValue | None = None
    qa: AnyValue | None = None
    production: AnyValue | None = None
