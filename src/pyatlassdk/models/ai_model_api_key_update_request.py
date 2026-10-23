"""Generated model for AiModelApiKeyUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AiModelApiKeyUpdateRequest(BaseModel):
    """Generated model for AiModelApiKeyUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="A new name for the API key.")
