"""Generated model for ApiAtlasModifyEndpointServiceRequestView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasModifyEndpointServiceRequestView(BaseModel):
    """Generated model for ApiAtlasModifyEndpointServiceRequestView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS"], BeforeValidator(upper_case)] = Field(alias="cloudProvider", description="Human-readable label that identifies the cloud service provider for the private endpoint service which you want to update.")
    supported_remote_regions: list[str] | None = Field(default=None, alias="supportedRemoteRegions", description="List of regions that the endpoint service supports. Native cross region support is implemented for AWS only.")
