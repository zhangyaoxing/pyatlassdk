"""Generated model for PrivateNetworkEndpointIdEntry. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PrivateNetworkEndpointIdEntry(BaseModel):
    """Generated model for PrivateNetworkEndpointIdEntry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    azure_link_id: str | None = Field(default=None, alias="azureLinkId", description="Link ID that identifies the Azure private endpoint connection.")
    comment: str | None = Field(default=None, description="Human-readable string to associate with this private endpoint.")
    customer_endpoint_dns_name: str | None = Field(default=None, alias="customerEndpointDNSName", description="Human-readable label to identify customer's VPC endpoint DNS name. If defined, you must also specify a value for `region`.")
    customer_endpoint_ip_address: str | None = Field(default=None, alias="customerEndpointIPAddress", description="IP address used to connect to the Azure private endpoint.")
    endpoint_id: str = Field(alias="endpointId", description="Unique string that identifies the private endpoint. For AWS, this is a 22-character alphanumeric string in the format `vpce-<17 hex characters>`. For Azure, this is the full resource ID in the format `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateEndpoints/{endpointName}`.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message describing a failure approving the private endpoint request.")
    provider: Annotated[Literal["AWS", "AZURE"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the cloud service provider. Atlas Data Lake supports Amazon Web Services and Azure.")
    region: str | None = Field(default=None, description="Human-readable label to identify the region of customer's VPC endpoint. If defined, you must also specify a value for `customerEndpointDNSName`.")
    status: Annotated[Literal["PENDING", "OK", "FAILED", "DELETING"], BeforeValidator(upper_case)] | None = Field(default=None, description="Status of the private endpoint connection request.")
    type: Annotated[Literal["DATA_LAKE"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the resource type associated with this private endpoint.")
