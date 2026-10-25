"""Generated model for AiModelsRateLimitUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AiModelsRateLimitUpdateRequest(BaseModel):
    """Generated model for AiModelsRateLimitUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    requests_per_minute_limit: int = Field(alias="requestsPerMinuteLimit", description="The number of requests per minute allowed for this model group. Must be a positive integer. Cannot be more than the organization level limit for this group model.")
    tokens_per_minute_limit: int = Field(alias="tokensPerMinuteLimit", description="The number of tokens per minute allowed for this model group. Must be a positive integer. Cannot be more than the organization level limit for this group model.")
