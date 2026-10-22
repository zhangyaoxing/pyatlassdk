"""Generated model for RateLimitEndpointSetEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class RateLimitEndpointSetEndpoint(BaseModel):
    """Generated model for RateLimitEndpointSetEndpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    method: Literal["GET", "POST", "PUT", "DELETE", "PATCH"] | None = Field(default=None, description="The HTTP method of the endpoint.")
    path: str | None = Field(default=None, description="The URL path of the endpoint.")
