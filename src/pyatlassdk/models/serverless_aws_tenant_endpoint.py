"""Generated model for ServerlessAWSTenantEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ServerlessAWSTenantEndpoint(BaseModel):
    """View for a serverless AWS tenant endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the private endpoint.")
    cloud_provider_endpoint_id: str | None = Field(default=None, alias="cloudProviderEndpointId", description="Unique string that identifies the private endpoint's network interface.")
    comment: str | None = Field(default=None, description="Human-readable comment associated with the private endpoint.")
    endpoint_service_name: str | None = Field(default=None, alias="endpointServiceName", description="Unique string that identifies the Amazon Web Services (AWS) PrivateLink endpoint service. MongoDB Cloud returns null while it creates the endpoint service.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Human-readable error message that indicates error condition associated with establishing the private endpoint connection.")
    provider_name: Literal["AWS"] | None = Field(default=None, alias="providerName", description="Human-readable label that identifies the cloud service provider.")
    status: Literal["RESERVATION_REQUESTED", "RESERVED", "INITIATING", "AVAILABLE", "FAILED", "DELETING"] | None = Field(default=None, description="Human-readable label that indicates the current operating status of the private endpoint.")
