"""Generated model for ApiAtlasInvalidPolicyErrorDetailView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasInvalidPolicyErrorDetailView(BaseModel):
    """Generated model for ApiAtlasInvalidPolicyErrorDetailView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    detail: str | None = Field(default=None, description="A string that provides a detailed description of a validation error.")
