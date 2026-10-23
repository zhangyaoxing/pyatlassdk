"""Generated model for GCPNetworkPeeringConnectionSettings. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GCPNetworkPeeringConnectionSettings(BaseModel):
    """Group of Network Peering connection settings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    container_id: str = Field(alias="containerId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Details of the error returned when requesting a GCP network peering resource. The resource returns `null` if the request succeeded.")
    gcp_project_id: str = Field(alias="gcpProjectId", description="Human-readable label that identifies the GCP project that contains the network that you want to peer with the MongoDB Cloud VPC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the network peering connection.")
    network_name: str = Field(alias="networkName", description="Human-readable label that identifies the network to peer with the MongoDB Cloud VPC.")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="providerName", description="Cloud service provider that serves the requested network peering connection.")
    status: Annotated[Literal["ADDING_PEER", "WAITING_FOR_USER", "AVAILABLE", "FAILED", "DELETING"], BeforeValidator(upper_case)] | None = Field(default=None, description="State of the network peering connection at the time you made the request.")
