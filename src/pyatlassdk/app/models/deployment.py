"""Generated model for Deployment. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.deployment_location import DeploymentLocation

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Deployment(BaseModel):
    """Generated model for Deployment."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The unique ID of the deployment.")
    name: str | None = Field(default=None, description="The name of the deployment. By default, this is the same\nvalue as ``_id``.")
    app_id: str | None = Field(default=None, description="The unique `_id` value of the Atlas App Services App.")
    draft_id: str | None = Field(default=None, description="The unique `_id` value of the deployment draft associated with the\ndeployment, if applicable.")
    user_id: str | None = Field(default=None, description="The unique `_id` value of the MongoDB Cloud user that deployed the draft.")
    deployed_at: int | None = Field(default=None, description="The time at which the deployment was made. Represented as the number of\nseconds since January 1, 1970.")
    origin: str | None = Field(default=None, description="The deployment method used to create the deployment.")
    commit: str | None = Field(default=None, description="The commit hash of the deployment (Automatic GitHub Deployment)")
    status: str | None = Field(default=None, description="A message that indicates whether or not the deployment was\nsuccessful.")
    status_error_message: str | None = Field(default=None, description="The error message of the error that caused the deployment to fail, if\napplicable.")
    diff_url: str | None = Field(default=None, description="A link to the diff of changes in the deployment")
    remote_location: DeploymentLocation | None = None
