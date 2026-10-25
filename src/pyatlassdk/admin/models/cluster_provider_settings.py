"""Generated model for ClusterProviderSettings. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.aws_cloud_provider_settings import AWSCloudProviderSettings
from pyatlassdk.admin.models.azure_cloud_provider_settings import AzureCloudProviderSettings
from pyatlassdk.admin.models.cloud_gcp_provider_settings import CloudGCPProviderSettings
from pyatlassdk.admin.models.cluster_flex_provider_settings import ClusterFlexProviderSettings
from pyatlassdk.admin.models.cluster_free_provider_settings import ClusterFreeProviderSettings

ClusterProviderSettings: TypeAlias = AWSCloudProviderSettings | AzureCloudProviderSettings | CloudGCPProviderSettings | ClusterFreeProviderSettings | ClusterFlexProviderSettings
