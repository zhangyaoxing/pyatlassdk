"""Generated model for CloudProviderRegion. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.cloud_provider_region_id import CloudProviderRegionId
from pyatlassdk.app.models.deployment_model import DeploymentModel

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderRegion(BaseModel):
    """Generated model for CloudProviderRegion."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: CloudProviderRegionId | None = Field(default=None, description="The short identifier of a cloud provider-specific deployment region.\nSome regions are available for global deployment while others are\nonly available for local apps. See [Cloud Deployment\nRegions](https://www.mongodb.com/docs/atlas/app-services/apps/deployment-models-and-regions/#cloud-deployment-regions).")
    name: str | None = Field(default=None, description="A descriptive name for the region.")
    cloud_provider: str | None = Field(default=None, description="The cloud provider that hosts the region.")
    country: str | None = Field(default=None, description="The country where the region is physically hosted.")
    deployment_models: list[DeploymentModel] | None = Field(default=None, description="The [deployment\nmodels](https://www.mongodb.com/docs/atlas/app-services/apps/deployment-models-and-regions/#deployment-models)\nthat this region supports.")
