"""Generated model for FieldLevelPermissions. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.expression import Expression

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FieldLevelPermissions(BaseModel):
    """Read and write permissions for a field."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    read: Expression = Field(description="A rule expression that evaluates to `true` if the role can read the field's value.")
    write: Expression = Field(description="A rule expression that evaluates to `true` if the role can write the field's value.")
