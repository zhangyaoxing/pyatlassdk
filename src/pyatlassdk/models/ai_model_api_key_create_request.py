"""Generated model for AiModelApiKeyCreateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AiModelApiKeyCreateRequest(BaseModel):
    """Generated model for AiModelApiKeyCreateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud: Literal["ANY"] = Field(description="Cloud provider scope for this API key. Use \"ANY\" for a cloud-agnostic scope. Additional cloud values will be supported in future API versions.")
    geography: Literal["ANY"] = Field(description="Geography scope for this API key. Use \"ANY\" for a geography-agnostic scope. Additional geography values will be supported in future API versions.")
    name: str = Field(description="A name for the new API key that will be created.")
