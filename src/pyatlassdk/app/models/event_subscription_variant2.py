"""Generated model for EventSubscriptionVariant2. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.app._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EventSubscriptionVariant2(BaseModel):
    """Generated model for EventSubscriptionVariant2."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    name: str | None = None
    type: Annotated[Literal["SYNCTRANSLATOR"], BeforeValidator(upper_case)] | None = None
    function_id: str | None = None
    disabled: bool | None = None
    config: None = None
    last_modified: float | None = None
