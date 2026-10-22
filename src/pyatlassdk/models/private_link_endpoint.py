"""Generated model for PrivateLinkEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class PrivateLinkEndpoint(BaseModel):
    """Generated model for PrivateLinkEndpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "AZURE", "GCP"] = Field(alias="cloudProvider", description="Cloud service provider that serves the requested endpoint.")
    delete_requested: bool | None = Field(default=None, alias="deleteRequested", description="Flag that indicates whether MongoDB Cloud received a request to remove the specified private endpoint from the private endpoint service.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message returned when requesting private connection resource. The resource returns `null` if the request succeeded.")
    region_name: str | None = Field(default=None, alias="regionName", description="Region name of the private endpoint.")
