"""Generated model for AppDeploymentSettings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.cloud_provider_region_id import CloudProviderRegionId
from pyatlassdk.app.models.deployment_model import DeploymentModel

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppDeploymentSettings(BaseModel):
    """Generated model for AppDeploymentSettings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    deployment_model: DeploymentModel | None = None
    provider_region: CloudProviderRegionId | None = None
