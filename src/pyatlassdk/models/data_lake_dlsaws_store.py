"""Generated model for DataLakeDLSAWSStore. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DataLakeDLSAWSStore(BaseModel):
    """Group of settings that define where the data is stored."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the data store. The **databases.[n].collections.[n].dataSources.[n].storeName** field references this values as part of the mapping configuration. To use MongoDB Cloud as a data store, the data lake requires a serverless instance or an `M10` or higher cluster.")
    provider: str
    region: Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "EU_CENTRAL_2", "AP_EAST_1", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTHEAST_4", "AP_SOUTH_1", "AP_SOUTH_2", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "ME_CENTRAL_1", "AF_SOUTH_1", "EU_SOUTH_1", "EU_SOUTH_2", "IL_CENTRAL_1", "CA_WEST_1", "GLOBAL"] | None = Field(default=None, description="Physical location where MongoDB Cloud deploys your AWS-hosted MongoDB cluster nodes. The region you choose can affect network latency for clients accessing your databases. When MongoDB Cloud deploys a dedicated cluster, it checks if a VPC or VPC connection exists for that provider and region. If not, MongoDB Cloud creates them as part of the deployment. MongoDB Cloud assigns the VPC a CIDR block. To limit a new VPC peering connection to one CIDR block and region, create the connection first. Deploy the cluster after the connection starts.")
