"""Generated model for NewValue. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.any_value import AnyValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NewValue(BaseModel):
    """Generated model for NewValue."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str
    private: bool
    value: AnyValue
