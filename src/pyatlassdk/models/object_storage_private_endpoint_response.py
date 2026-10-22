"""Generated model for ObjectStoragePrivateEndpointResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ObjectStoragePrivateEndpointResponse(BaseModel):
    """Generated model for ObjectStoragePrivateEndpointResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS"] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message for failures associated with the Object Storage private endpoint.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the Private Endpoint Service.")
    private_endpoint_connection_name: str | None = Field(default=None, alias="privateEndpointConnectionName", description="Connection name of the Private Endpoint.")
    region_name: Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "AP_EAST_1", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTH_1", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "GLOBAL"] | None = Field(default=None, alias="regionName", description="Cloud provider region in which the Object Storage bucket is located. For cross-region endpoints, this differs from `vpcRegionName`, which is the region in which the VPC interface endpoint is deployed.")
    status: Literal["INITIATING", "PENDING_ACCEPTANCE", "ACTIVE", "FAILED", "PENDING_RECREATION", "DELETING"] | None = Field(default=None, description="State of the Object Storage private endpoint.")
    vpc_region_name: Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "AP_EAST_1", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTH_1", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "GLOBAL"] | None = Field(default=None, alias="vpcRegionName", description="Cloud provider region in which the VPC interface endpoint is deployed. Echoes `regionName` for same-region endpoints.")
