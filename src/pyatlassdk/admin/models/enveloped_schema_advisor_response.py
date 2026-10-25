"""Generated model for EnvelopedSchemaAdvisorResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link
from pyatlassdk.admin.models.schema_advisor_response import SchemaAdvisorResponse

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EnvelopedSchemaAdvisorResponse(BaseModel):
    """Response envelope that wraps the response payload in `content` and includes response metadata such as `status` and `locations`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    content: SchemaAdvisorResponse
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    locations: list[str] | None = Field(default=None, description="URLs of resources created by this request.")
    status: int = Field(description="HTTP status code returned with this response.")
