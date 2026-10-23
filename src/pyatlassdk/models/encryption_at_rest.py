"""Generated model for EncryptionAtRest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.awskms_configuration import AWSKMSConfiguration
from pyatlassdk.models.azure_key_vault import AzureKeyVault
from pyatlassdk.models.google_cloud_kms import GoogleCloudKMS

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EncryptionAtRest(BaseModel):
    """Generated model for EncryptionAtRest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws_kms: AWSKMSConfiguration | None = Field(default=None, alias="awsKms")
    azure_key_vault: AzureKeyVault | None = Field(default=None, alias="azureKeyVault")
    enabled_for_search_nodes: bool | None = Field(default=None, alias="enabledForSearchNodes", description="Flag that indicates whether Encryption at Rest for Dedicated Search Nodes is enabled in the specified project.")
    google_cloud_kms: GoogleCloudKMS | None = Field(default=None, alias="googleCloudKms")
