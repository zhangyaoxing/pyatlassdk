"""Generated model for FieldViolation. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class FieldViolation(BaseModel):
    """Generated model for FieldViolation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str = Field(description="A description of why the request element is bad.")
    field: str = Field(description="A path that leads to a field in the request body.")
