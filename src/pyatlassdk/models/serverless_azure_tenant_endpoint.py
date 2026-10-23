"""Generated model for ServerlessAzureTenantEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServerlessAzureTenantEndpoint(BaseModel):
    """View for a serverless Azure tenant endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the private endpoint.")
    cloud_provider_endpoint_id: str | None = Field(default=None, alias="cloudProviderEndpointId", description="Unique string that identifies the Azure private endpoint's network interface that someone added to this private endpoint service.")
    comment: str | None = Field(default=None, description="Human-readable comment associated with the private endpoint.")
    endpoint_service_name: str | None = Field(default=None, alias="endpointServiceName", description="Unique string that identifies the Azure private endpoint service. MongoDB Cloud returns null while it creates the endpoint service.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Human-readable error message that indicates error condition associated with establishing the private endpoint connection.")
    private_endpoint_ip_address: str | None = Field(default=None, alias="privateEndpointIpAddress", description="IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service.")
    private_link_service_resource_id: str | None = Field(default=None, alias="privateLinkServiceResourceId", description="Root-relative path that identifies the Azure Private Link Service that MongoDB Cloud manages. MongoDB Cloud returns null while it creates the endpoint service.")
    provider_name: Annotated[Literal["AZURE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="providerName", description="Human-readable label that identifies the cloud service provider.")
    status: Annotated[Literal["RESERVATION_REQUESTED", "RESERVED", "INITIATING", "AVAILABLE", "FAILED", "DELETING"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that indicates the current operating status of the private endpoint.")
