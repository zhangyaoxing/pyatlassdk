"""Generated model for CloudProviderEndpointServiceRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderEndpointServiceRequest(BaseModel):
    """Generated model for CloudProviderEndpointServiceRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    port_mapping_enabled: bool | None = Field(default=None, alias="portMappingEnabled", description="Flag that indicates whether this endpoint service uses PSC port-mapping. This is only applicable for GCP Private Endpoint Services.")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="providerName", description="Human-readable label that identifies the cloud service provider for which you want to create the private endpoint service.")
    region: str = Field(description="Cloud provider region in which you want to create the private endpoint service. Regions accepted as values differ for [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/), [Google Cloud Platform](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Microsoft Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).")
    supported_remote_regions: list[str] | None = Field(default=None, alias="supportedRemoteRegions", description="List of regions that the endpoint service supports. Native cross region support is implemented for AWS only.")
