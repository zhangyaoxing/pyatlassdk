"""Generated model for DataFederationLimit. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataFederationLimit(BaseModel):
    """Details of user managed limits."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    current_usage: int | None = Field(default=None, alias="currentUsage", description="Amount that indicates the current usage of the limit.")
    default_limit: int | None = Field(default=None, alias="defaultLimit", description="Default value of the limit.")
    maximum_limit: int | None = Field(default=None, alias="maximumLimit", description="Maximum value of the limit.")
    name: str = Field(description="Human-readable label that identifies the user-managed limit to modify.")
    value: int = Field(description="Amount to set the limit to.")
