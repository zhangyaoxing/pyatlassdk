"""Generated model for ApiAtlasPolicyView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasPolicyView(BaseModel):
    """Generated model for ApiAtlasPolicyView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    body: str | None = Field(default=None, description="A string that defines the permissions for the policy. The syntax used is the Cedar Policy language.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies the policy.")
