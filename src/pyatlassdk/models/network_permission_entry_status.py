"""Generated model for NetworkPermissionEntryStatus. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NetworkPermissionEntryStatus(BaseModel):
    """Generated model for NetworkPermissionEntryStatus."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    status: Annotated[Literal["PENDING", "FAILED", "ACTIVE"], BeforeValidator(upper_case)] = Field(alias="STATUS", description="State of the access list entry when MongoDB Cloud made this request.\n\n`ACTIVE`: This access list entry applies to all relevant cloud providers.\n\n`PENDING`: MongoDB Cloud has started to add access list entry. This access list entry may not apply to all cloud providers at the time of this request.\n\n`FAILED`: MongoDB Cloud didn't succeed in adding this access list entry.")
