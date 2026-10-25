"""Generated model for DeploymentConfig. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.deployment_config_automatic_deployment import DeploymentConfigAutomaticDeployment

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DeploymentConfig(BaseModel):
    """A configuration file that controls your app's deployment behavior."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ui_drafts_disabled: bool = Field(description="If `true`, every change made in the Admin UI deploys\nautomatically on save. If `false`, changes are grouped into\na deployment draft that you deploy separately.")
    automatic_deployment: DeploymentConfigAutomaticDeployment = Field(description="Configuration for automatic deployment methods")
    last_modified: float | None = Field(default=None, description="The time this configuration was last modified represented by the number of seconds since the UNIX epoch.")
