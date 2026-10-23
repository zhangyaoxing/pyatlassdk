"""Generated model for RateLimitEndpointSetEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RateLimitEndpointSetEndpoint(BaseModel):
    """Generated model for RateLimitEndpointSetEndpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    method: Annotated[Literal["GET", "POST", "PUT", "DELETE", "PATCH"], BeforeValidator(upper_case)] | None = Field(default=None, description="The HTTP method of the endpoint.")
    path: str | None = Field(default=None, description="The URL path of the endpoint.")
