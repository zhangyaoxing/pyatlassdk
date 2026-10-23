"""Generated model for AWSKMSConfiguration. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AWSKMSConfiguration(BaseModel):
    """Amazon Web Services (AWS) KMS configuration details and encryption at rest configuration set for the specified project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access_key_id: str | None = Field(default=None, alias="accessKeyID", description="Unique alphanumeric string that identifies an Identity and Access Management (IAM) access key with permissions required to access your Amazon Web Services (AWS) Customer Master Key (CMK).")
    customer_master_key_id: str | None = Field(default=None, alias="customerMasterKeyID", description="Unique alphanumeric string that identifies the Amazon Web Services (AWS) Customer Master Key (CMK) you used to encrypt and decrypt the MongoDB master keys.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled encryption at rest for the specified project through Amazon Web Services (AWS) Key Management Service (KMS). To disable encryption at rest using customer key management and remove the configuration details, pass only this parameter with a value of `false`.")
    region: Annotated[Literal["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "EU_CENTRAL_2", "AP_EAST_1", "AP_EAST_2", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTHEAST_4", "AP_SOUTHEAST_5", "AP_SOUTHEAST_6", "AP_SOUTHEAST_7", "AP_SOUTH_1", "AP_SOUTH_2", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "ME_CENTRAL_1", "AF_SOUTH_1", "EU_SOUTH_1", "EU_SOUTH_2", "IL_CENTRAL_1", "CA_WEST_1", "MX_CENTRAL_1", "GLOBAL"], BeforeValidator(upper_case)] | None = Field(default=None, description="Physical location where MongoDB Cloud deploys your AWS-hosted MongoDB cluster nodes. The region you choose can affect network latency for clients accessing your databases. When MongoDB Cloud deploys a dedicated cluster, it checks if a VPC or VPC connection exists for that provider and region. If not, MongoDB Cloud creates them as part of the deployment. MongoDB Cloud assigns the VPC a CIDR block. To limit a new VPC peering connection to one CIDR block and region, create the connection first. Deploy the cluster after the connection starts.")
    require_private_networking: bool | None = Field(default=None, alias="requirePrivateNetworking", description="Enable connection to your Amazon Web Services (AWS) Key Management Service (KMS) over private networking.")
    role_id: str | None = Field(default=None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies an Amazon Web Services (AWS) Identity and Access Management (IAM) role. This IAM role has the permissions required to manage your AWS customer master key.")
    secret_access_key: str | None = Field(default=None, alias="secretAccessKey", description="Human-readable label of the Identity and Access Management (IAM) secret access key with permissions required to access your Amazon Web Services (AWS) customer master key.")
    valid: bool | None = Field(default=None, description="Flag that indicates whether the Amazon Web Services (AWS) Key Management Service (KMS) encryption key can encrypt and decrypt data.")
