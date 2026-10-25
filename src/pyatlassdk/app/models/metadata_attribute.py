"""Generated model for MetadataAttribute. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MetadataAttribute(BaseModel):
    """Generated model for MetadataAttribute."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="The [metadata\nattribute](https://www.mongodb.com/docs/atlas/app-services/hosting/file-metadata-attributes)\nname.")
    value: str | None = Field(default=None, description="The [metadata\nattribute](https://www.mongodb.com/docs/atlas/app-services/hosting/file-metadata-attributes)\nvalue.")
