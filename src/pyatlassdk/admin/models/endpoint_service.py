"""Generated model for EndpointService. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EndpointService(BaseModel):
    """Generated model for EndpointService."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="cloudProvider", description="Cloud service provider that serves the requested endpoint service.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message returned when requesting private connection resource. The resource returns `null` if the request succeeded.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the Private Endpoint Service.")
    region_name: str | None = Field(default=None, alias="regionName", description="Cloud provider region that manages this Private Endpoint Service.")
    status: Annotated[Literal["INITIATING", "AVAILABLE", "WAITING_FOR_USER", "FAILED", "DELETING"], BeforeValidator(upper_case)] | None = Field(default=None, description="State of the Private Endpoint Service connection when MongoDB Cloud received this request.")
