"""Generated model for QueryShapeUpdateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class QueryShapeUpdateRequest(BaseModel):
    """Request body for modifying the rejection status of a query shape."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    status: Annotated[Literal["REJECTED", "UNREJECTED"], BeforeValidator(upper_case)] = Field(description="The rejection status of a query shape. Use REJECTED to prevent the query shape from executing on the cluster, or UNREJECTED to allow it to execute.")
