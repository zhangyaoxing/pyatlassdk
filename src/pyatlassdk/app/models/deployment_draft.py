"""Generated model for DeploymentDraft. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.app_instance import AppInstance

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DeploymentDraft(BaseModel):
    """Generated model for DeploymentDraft."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The unique ID of the draft.")
    user_id: str | None = Field(default=None, description="The unique `_id` value of the MongoDB Cloud user that created the draft.")
    app: AppInstance | None = None
