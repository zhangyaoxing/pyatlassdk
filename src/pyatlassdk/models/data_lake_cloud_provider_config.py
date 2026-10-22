"""Generated model for DataLakeCloudProviderConfig. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.data_federation_azure_cloud_provider_config import DataFederationAzureCloudProviderConfig
from pyatlassdk.models.data_federation_gcp_cloud_provider_config import DataFederationGCPCloudProviderConfig
from pyatlassdk.models.data_lake_aws_cloud_provider_config import DataLakeAWSCloudProviderConfig

from pydantic import BaseModel, ConfigDict, Field

class DataLakeCloudProviderConfig(BaseModel):
    """Cloud provider where this Federated Database Instance is hosted."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws: DataLakeAWSCloudProviderConfig | None = None
    azure: DataFederationAzureCloudProviderConfig | None = None
    gcp: DataFederationGCPCloudProviderConfig | None = None
