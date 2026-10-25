"""Generated model for DeploymentMigration. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.app_deployment_settings import AppDeploymentSettings

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DeploymentMigration(BaseModel):
    """Generated model for DeploymentMigration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    status: Literal["started", "downtime", "enabling_event_subscriptions", "cleanup", "successful", "failed"] | None = None
    message: str | None = Field(default=None, description="A description of the current migration status.")
    updated_at: str | None = Field(default=None, description="A timestamp of the most recent update to the deployment migration.")
    from_: AppDeploymentSettings | None = Field(default=None, alias="from", description="The App's deployment model and cloud provider region at the start of the migration")
    to: AppDeploymentSettings | None = Field(default=None, description="The migration's target deployment model and cloud provider\nregion. At the end of a successful migration, the App uses\nthese deployment settings instead of the settings described\nby `from`.")
