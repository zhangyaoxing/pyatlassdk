"""Generated model for SpecificEnvironmentValues. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.any_value import AnyValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SpecificEnvironmentValues(BaseModel):
    """Generated model for SpecificEnvironmentValues."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    values: dict[str, AnyValue] | None = None
