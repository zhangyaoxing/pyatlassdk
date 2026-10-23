"""Generated model for UserScope. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UserScope(BaseModel):
    """Range of resources available to this database user."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="Human-readable label that identifies the cluster or MongoDB Atlas Data Lake that this database user can access.")
    type: Annotated[Literal["CLUSTER", "DATA_LAKE", "STREAM"], BeforeValidator(upper_case)] = Field(description="Category of resource that this database user can access.")
