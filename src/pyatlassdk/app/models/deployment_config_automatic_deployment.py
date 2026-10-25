"""Generated model for DeploymentConfigAutomaticDeployment. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DeploymentConfigAutomaticDeployment(BaseModel):
    """Generated model for DeploymentConfigAutomaticDeployment."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="If `true`, the app automatically deploys using the method defined for `provider`.")
    provider: Literal["github"] | None = Field(default=None, description="The type of automatic deployment.")
    installation_ids: list[str] | None = Field(default=None, description="The unique ID values of automatic deployment provider\ninstallations. For example, the `id` value of a [GitHub app\ninstallation](https://docs.github.com/en/rest/apps/installations).")
