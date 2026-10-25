"""Generated model for CloudProviderRegionId. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.aws_deployment_region import AwsDeploymentRegion
from pyatlassdk.app.models.azure_deployment_region import AzureDeploymentRegion
from pyatlassdk.app.models.gcp_deployment_region import GcpDeploymentRegion

CloudProviderRegionId: TypeAlias = AwsDeploymentRegion | AzureDeploymentRegion | GcpDeploymentRegion
