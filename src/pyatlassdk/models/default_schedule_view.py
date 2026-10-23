"""Generated model for DefaultScheduleView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DefaultScheduleView(BaseModel):
    """Regular frequency and duration when archiving process occurs."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Annotated[Literal["DEFAULT", "DAILY", "WEEKLY", "MONTHLY"], BeforeValidator(upper_case)] = Field(description="Type of schedule.")
