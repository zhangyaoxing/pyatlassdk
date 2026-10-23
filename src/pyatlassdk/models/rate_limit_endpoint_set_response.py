"""Generated model for RateLimitEndpointSetResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.rate_limit_endpoint_set_capacity import RateLimitEndpointSetCapacity
from pyatlassdk.models.rate_limit_endpoint_set_endpoint import RateLimitEndpointSetEndpoint
from pyatlassdk.models.rate_limit_endpoint_set_refill_duration_seconds import RateLimitEndpointSetRefillDurationSeconds
from pyatlassdk.models.rate_limit_endpoint_set_refill_rate import RateLimitEndpointSetRefillRate

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RateLimitEndpointSetResponse(BaseModel):
    """Generated model for RateLimitEndpointSetResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    capacity: RateLimitEndpointSetCapacity | None = None
    endpoint_set_id: str | None = Field(default=None, alias="endpointSetId", description="The ID of the endpoint set.")
    endpoint_set_name: str | None = Field(default=None, alias="endpointSetName", description="The endpoint set name.")
    endpoints: list[RateLimitEndpointSetEndpoint] | None = Field(default=None, description="A list of endpoints associated with the specified endpoint set.")
    refill_duration_seconds: RateLimitEndpointSetRefillDurationSeconds | None = Field(default=None, alias="refillDurationSeconds")
    refill_rate: RateLimitEndpointSetRefillRate | None = Field(default=None, alias="refillRate")
    scope: Annotated[Literal["IP", "GROUP", "ORGANIZATION", "USER"], BeforeValidator(upper_case)] | None = Field(default=None, description="The scope of the endpoint set.")
