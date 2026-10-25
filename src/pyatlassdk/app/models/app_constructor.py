"""Generated model for AppConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.cloud_provider_region_id import CloudProviderRegionId
from pyatlassdk.app.models.data_source import DataSource
from pyatlassdk.app.models.deployment_location import DeploymentLocation
from pyatlassdk.app.models.deployment_model import DeploymentModel
from pyatlassdk.app.models.nullable_app_environment import NullableAppEnvironment

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppConstructor(BaseModel):
    """An object that describes a new app to create"""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="The name of the application. Must begin with a letter and\nmay only contain ASCII letters, numbers, underscores, and\nhyphens.")
    provider_region: CloudProviderRegionId | None = Field(default=None, description="The short identifier of a cloud provider-specific deployment region.\nSome regions are available for global deployment while others are\nonly available for local apps. See [Cloud Deployment\nRegions](https://www.mongodb.com/docs/atlas/app-services/apps/deployment-models-and-regions/).")
    location: DeploymentLocation | None = Field(default=None, description="The application's physical deployment location. This should\nagree with the more specific `provider_region` value. For\nexample, an App with a `provider_region` of `aws-us-west-2`\nmaps to a `location` of `US-OR`.")
    deployment_model: DeploymentModel | None = None
    environment: NullableAppEnvironment | None = None
    template_id: str | None = Field(default=None, description="The id of an [App Services template\napp](https://www.mongodb.com/docs/atlas/app-services/reference/template-apps)\nto use as a base for the new app.")
    data_source: DataSource | None = None
