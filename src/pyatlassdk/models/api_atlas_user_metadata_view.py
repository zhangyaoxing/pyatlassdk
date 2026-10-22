"""Generated model for ApiAtlasUserMetadataView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasUserMetadataView(BaseModel):
    """The user that last updated the atlas resource policy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies a user.")
    name: str | None = Field(default=None, description="Human-readable label that describes a user.")
