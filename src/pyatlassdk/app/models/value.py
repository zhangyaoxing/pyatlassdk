"""Generated model for Value. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.any_value import AnyValue

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Value(BaseModel):
    """Generated model for Value."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    name: str
    private: bool
    from_secret: bool = Field(description="If `true`, the value is a reference by name to a\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/).")
    value: AnyValue
