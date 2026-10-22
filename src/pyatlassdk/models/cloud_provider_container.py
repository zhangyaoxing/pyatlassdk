"""Generated model for CloudProviderContainer. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.aws_cloud_provider_container import AWSCloudProviderContainer
from pyatlassdk.models.azure_cloud_provider_container import AzureCloudProviderContainer
from pyatlassdk.models.gcp_cloud_provider_container import GCPCloudProviderContainer

CloudProviderContainer: TypeAlias = AzureCloudProviderContainer | GCPCloudProviderContainer | AWSCloudProviderContainer
