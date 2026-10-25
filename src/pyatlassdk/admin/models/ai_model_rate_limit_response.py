"""Generated model for AiModelRateLimitResponse. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AiModelRateLimitResponse(BaseModel):
    """Generated model for AiModelRateLimitResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud: str | None = Field(default=None, description="Cloud provider scope for this rate limit. Use \"ANY\" for cloud-agnostic scope.")
    endpoint: str | None = Field(default=None, description="Server-computed endpoint hostname derived from `cloud` and `geography`. This field is read-only and must not be supplied in request bodies.")
    geography: str | None = Field(default=None, description="Geography scope for this rate limit. Use \"ANY\" for geography-agnostic scope.")
    model_group_name: str | None = Field(default=None, alias="modelGroupName", description="Identifier used to reference this model group.")
    model_names: list[str] | None = Field(default=None, alias="modelNames", description="List of embedding model names included in this model group.")
    requests_per_minute_limit: int | None = Field(default=None, alias="requestsPerMinuteLimit", description="The number of requests per minute allowed for this model group. Must be a positive integer. Cannot be more than the organization level limit for this group model.")
    tokens_per_minute_limit: int | None = Field(default=None, alias="tokensPerMinuteLimit", description="The number of tokens per minute allowed for this model group. Must be a positive integer. Cannot be more than the organization level limit for this group model.")
