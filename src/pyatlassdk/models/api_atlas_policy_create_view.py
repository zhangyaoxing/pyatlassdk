"""Generated model for ApiAtlasPolicyCreateView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasPolicyCreateView(BaseModel):
    """Generated model for ApiAtlasPolicyCreateView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    body: str = Field(description="A string that defines the permissions for the policy. The syntax used is the Cedar Policy language.")
