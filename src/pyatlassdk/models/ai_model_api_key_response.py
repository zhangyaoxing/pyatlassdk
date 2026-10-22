"""Generated model for AiModelApiKeyResponse. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AiModelApiKeyResponse(BaseModel):
    """Generated model for AiModelApiKeyResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key_id: str | None = Field(default=None, alias="apiKeyId", description="Identifier used to reference this API key in admin API calls.")
    cloud: str | None = Field(default=None, description="Cloud provider scope for this API key. Use \"ANY\" for cloud-agnostic scope.")
    created_at: str | None = Field(default=None, alias="createdAt", description="UTC date when the API key was created. This parameter is formatted as an ISO 8601 timestamp.")
    created_by: str | None = Field(default=None, alias="createdBy", description="Name of the user that created this API key. If no user name is available, the user ID is returned.")
    endpoint: str | None = Field(default=None, description="Server-computed endpoint hostname derived from `cloud` and `geography`. This field is read-only and must not be supplied in request bodies.")
    geography: str | None = Field(default=None, description="Geography scope for this API key. Use \"ANY\" for geography-agnostic scope.")
    group_id: str | None = Field(default=None, alias="groupId", description="ID of the Atlas group this API key belongs to.")
    last_used_at: str | None = Field(default=None, alias="lastUsedAt", description="UTC date when the API key was last used. This parameter is formatted as an ISO 8601 timestamp.")
    masked_secret: str | None = Field(default=None, alias="maskedSecret", description="A partially obfuscated version of the API key secret returned when the API key was created.")
    name: str | None = Field(default=None, description="Arbitrary string identifier assigned to this API key for convenient identification.")
    secret: str | None = Field(default=None, description="The full API key secret used for interacting with the embedding / reranking service. Note: this will only be fully populated in the response to a create API key request. Responses to get, list, and update requests will not include the secret.")
    status: str | None = Field(default=None, description="A string describing the current status of the API key.")
