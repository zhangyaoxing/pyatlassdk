"""Generated model for ApiAtlasPolicyMetadataView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasPolicyMetadataView(BaseModel):
    """Generated model for ApiAtlasPolicyMetadataView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    policy_id: str | None = Field(default=None, alias="policyId", description="Unique 24-hexadecimal character string that identifies the policy.")
