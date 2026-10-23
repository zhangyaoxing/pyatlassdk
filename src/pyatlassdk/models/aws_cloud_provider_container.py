"""Generated model for AWSCloudProviderContainer. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AWSCloudProviderContainer(BaseModel):
    """Collection of settings that configures the network container for a virtual private connection on Amazon Web Services."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the network peering container.")
    provider_name: Annotated[Literal["AWS", "GCP", "AZURE", "TENANT", "SERVERLESS"], BeforeValidator(upper_case)] | None = Field(default=None, alias="providerName", description="Cloud service provider that serves the requested network peering containers.")
    provisioned: bool | None = Field(default=None, description="Flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container.")
    atlas_cidr_block: str | None = Field(default=None, alias="atlasCidrBlock", description="IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project. MongoDB Cloud assigns all of the project's clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project.\n\nThese CIDR blocks must fall within the ranges reserved per RFC 1918. AWS and Azure further limit the block to between the `/24` and  `/21` ranges.\n\nTo modify the CIDR block, the target project cannot have:\n\n- Any M10 or greater clusters\n- Any other VPC peering connections\n\n You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project.\n\n **Example:** A project in an Amazon Web Services (AWS) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of `/24` equals 27 three-node replica sets.")
    region_name: Annotated[Literal["US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "EU_CENTRAL_2", "SA_EAST_1", "AP_EAST_1", "AP_EAST_2", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTHEAST_4", "AP_SOUTHEAST_5", "AP_SOUTHEAST_6", "AP_SOUTHEAST_7", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTH_1", "AP_SOUTH_2", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_CENTRAL_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "EU_SOUTH_2", "IL_CENTRAL_1", "CA_WEST_1", "MX_CENTRAL_1", "GLOBAL", "US_GOV_WEST_1", "US_GOV_EAST_1"], BeforeValidator(upper_case)] = Field(alias="regionName", description="Geographic area that Amazon Web Services (AWS) defines to which MongoDB Cloud deployed this network peering container.")
    vpc_id: str | None = Field(default=None, alias="vpcId", description="Unique string that identifies the MongoDB Cloud VPC on AWS.")
