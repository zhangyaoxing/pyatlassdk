"""Generated model for RateLimitEndpointSetRefillRate. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RateLimitEndpointSetRefillRate(BaseModel):
    """The rate limit refill rate for the endpoint set."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    default_value: int | None = Field(default=None, alias="defaultValue", description="The default rate limit refill rate of the endpoint set. Returned if there is a rate limit refill rate override set for the requested entity.")
    value: int | None = Field(default=None, description="The applied rate limit refill rate of the endpoint set.")
