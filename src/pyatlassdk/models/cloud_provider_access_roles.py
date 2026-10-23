"""Generated model for CloudProviderAccessRoles. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.cloud_provider_access_awsiam_role import CloudProviderAccessAWSIAMRole
from pyatlassdk.models.cloud_provider_access_azure_service_principal import CloudProviderAccessAzureServicePrincipal
from pyatlassdk.models.cloud_provider_access_gcp_service_account import CloudProviderAccessGCPServiceAccount

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAccessRoles(BaseModel):
    """Generated model for CloudProviderAccessRoles."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws_iam_roles: list[CloudProviderAccessAWSIAMRole] | None = Field(default=None, alias="awsIamRoles", description="List that contains the Amazon Web Services (AWS) IAM roles registered and authorized with MongoDB Cloud.")
    azure_service_principals: list[CloudProviderAccessAzureServicePrincipal] | None = Field(default=None, alias="azureServicePrincipals", description="List that contains the Azure Service Principals registered with MongoDB Cloud.")
    gcp_service_accounts: list[CloudProviderAccessGCPServiceAccount] | None = Field(default=None, alias="gcpServiceAccounts", description="List that contains the Google Service Accounts registered and authorized with MongoDB Cloud.")
