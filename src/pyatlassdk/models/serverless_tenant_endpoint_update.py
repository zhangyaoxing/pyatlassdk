"""Generated model for ServerlessTenantEndpointUpdate. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServerlessTenantEndpointUpdate(BaseModel):
    """Update view for a serverless tenant endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    comment: str | None = Field(default=None, description="Human-readable comment associated with the private endpoint.")
    provider_name: Annotated[Literal["AWS", "AZURE"], BeforeValidator(upper_case)] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the tenant endpoint.")
