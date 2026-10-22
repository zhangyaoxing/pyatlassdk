"""Generated model for EnvelopedDropIndexSuggestionsResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.drop_index_suggestions_response import DropIndexSuggestionsResponse
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class EnvelopedDropIndexSuggestionsResponse(BaseModel):
    """Response envelope that wraps the response payload in `content` and includes response metadata such as `status` and `locations`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    content: DropIndexSuggestionsResponse
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    locations: list[str] | None = Field(default=None, description="URLs of resources created by this request.")
    status: int = Field(description="HTTP status code returned with this response.")
