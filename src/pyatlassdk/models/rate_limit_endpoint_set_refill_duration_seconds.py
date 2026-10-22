"""Generated model for RateLimitEndpointSetRefillDurationSeconds. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class RateLimitEndpointSetRefillDurationSeconds(BaseModel):
    """The rate limit refill duration for the endpoint set."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    default_value: int | None = Field(default=None, alias="defaultValue", description="The default rate limit refill duration, in seconds, of the endpoint set. Returned if there is a rate limit refill duration override set for the requested entity.")
    value: int | None = Field(default=None, description="The applied rate limit refill duration of the endpoint set.")
