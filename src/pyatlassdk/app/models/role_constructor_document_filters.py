"""Generated model for RoleConstructorDocumentFilters. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.expression import Expression

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RoleConstructorDocumentFilters(BaseModel):
    """Generated model for RoleConstructorDocumentFilters."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    read: Expression = Field(description="A rule expression that evaluates to `true` if the role can read the document.")
    write: Expression = Field(description="A rule expression that evaluates to `true` if the role can write to the document.")
