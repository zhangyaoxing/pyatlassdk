"""Generated model for RateLimitEndpointSetCapacity. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class RateLimitEndpointSetCapacity(BaseModel):
    """The rate limit capacity for the endpoint set."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    default_value: int | None = Field(default=None, alias="defaultValue", description="The default request capacity of the endpoint set. Returned if there is a capacity override set for the requested entity.")
    value: int | None = Field(default=None, description="The applied request capacity of the endpoint set.")
