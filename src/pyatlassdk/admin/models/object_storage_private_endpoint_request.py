"""Generated model for ObjectStoragePrivateEndpointRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ObjectStoragePrivateEndpointRequest(BaseModel):
    """Generated model for ObjectStoragePrivateEndpointRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    region_name: Annotated[Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "AP_EAST_1", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTH_1", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "GLOBAL"], BeforeValidator(upper_case)] | None = Field(default=None, alias="regionName", description="Cloud provider region of the S3 bucket that the Object Storage private endpoint accesses. For same-region endpoints, this is also the region where the VPC interface endpoint is deployed.")
    vpc_region_name: Annotated[Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "AP_EAST_1", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTH_1", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "GLOBAL"], BeforeValidator(upper_case)] | None = Field(default=None, alias="vpcRegionName", description="Cloud provider region in which the VPC interface endpoint is deployed. Omit to deploy the interface endpoint in the same region as the S3 bucket (same-region endpoint). Set to a region different from `regionName` to create a cross-region endpoint.")
