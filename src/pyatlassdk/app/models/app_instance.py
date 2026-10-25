"""Generated model for AppInstance. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.cloud_provider_region_id import CloudProviderRegionId
from pyatlassdk.app.models.deployment_location import DeploymentLocation
from pyatlassdk.app.models.deployment_model import DeploymentModel
from pyatlassdk.app.models.nullable_app_environment import NullableAppEnvironment

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppInstance(BaseModel):
    """A specific, existing application."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="The name of the application. Must begin with a letter and\nmay only contain ASCII letters, numbers, underscores, and\nhyphens.")
    provider_region: CloudProviderRegionId | None = Field(default=None, description="The short identifier of a cloud provider-specific deployment region.\nSome regions are available for global deployment while others are\nonly available for local apps. See [Cloud Deployment\nRegions](https://www.mongodb.com/docs/atlas/app-services/apps/deployment-models-and-regions/).")
    location: DeploymentLocation | None = Field(default=None, description="The application's physical deployment location. This should\nagree with the more specific `provider_region` value. For\nexample, an App with a `provider_region` of `aws-us-west-2`\nmaps to a `location` of `US-OR`.")
    deployment_model: DeploymentModel | None = None
    environment: NullableAppEnvironment | None = None
    id: str | None = Field(default=None, alias="_id", description="The application's unique internal ID.")
    client_app_id: str | None = Field(default=None, description="The application's public App ID.")
    domain_id: str | None = Field(default=None, description="The application's associated domain ID.")
    group_id: str | None = Field(default=None, description="The application's [Atlas Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).")
    last_used: int | None = Field(default=None, description="The time this app was last used in [UNIX time](https://en.wikipedia.org/wiki/Unix_time) (i.e. the number of seconds since Jan 1, 1970).")
    last_modified: int | None = Field(default=None, description="The time this app was last modified in [UNIX time](https://en.wikipedia.org/wiki/Unix_time) (i.e. the number of seconds since Jan 1, 1970).")
    product: Literal["standard", "atlas", "data-api", "device-sync"] | None = Field(default=None, description="The product this app is for.")
