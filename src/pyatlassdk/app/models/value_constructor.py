"""Generated model for ValueConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.any_value import AnyValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ValueConstructor(BaseModel):
    """Generated model for ValueConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str
    private: bool
    from_secret: bool = Field(description="If `true`, the value is a reference by name to a\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/).")
    value: AnyValue
