"""Generated model for CreateAWSEndpointRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class CreateAWSEndpointRequest(BaseModel):
    """Group of Private Endpoint settings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "AZURE", "GCP"] | None = Field(default=None, alias="cloudProvider", description="Cloud service provider that manages this private endpoint.")
    id: str = Field(description="Unique string that identifies the private endpoint's network interface that someone added to this private endpoint service.")
