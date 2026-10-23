"""Generated model for Link. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Link(BaseModel):
    """Generated model for Link."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    href: str | None = Field(default=None, description="Uniform Resource Locator (URL) that points another API resource to which this response has some relationship. This URL often begins with `https://cloud.mongodb.com/api/atlas`.")
    rel: str | None = Field(default=None, description="Uniform Resource Locator (URL) that defines the semantic relationship between this resource and another API resource. This URL often begins with `https://cloud.mongodb.com/api/atlas`.")
