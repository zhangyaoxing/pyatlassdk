"""Generated model for BadRequestDetail. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.field_violation import FieldViolation

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BadRequestDetail(BaseModel):
    """Bad request detail."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    fields: list[FieldViolation] | None = Field(default=None, description="Describes all violations in a client request.")
