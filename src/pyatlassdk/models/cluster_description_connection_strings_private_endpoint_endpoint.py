"""Generated model for ClusterDescriptionConnectionStringsPrivateEndpointEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterDescriptionConnectionStringsPrivateEndpointEndpoint(BaseModel):
    """Details of a private endpoint deployed for this cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    endpoint_id: str | None = Field(default=None, alias="endpointId", description="Unique string that the cloud provider uses to identify the private endpoint.")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="providerName", description="Cloud provider in which MongoDB Cloud deploys the private endpoint.")
    region: str | None = Field(default=None, description="Region where the private endpoint is deployed.")
