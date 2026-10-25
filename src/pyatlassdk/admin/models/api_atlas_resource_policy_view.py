"""Generated model for ApiAtlasResourcePolicyView. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.admin.models.api_atlas_policy_view import ApiAtlasPolicyView
from pyatlassdk.admin.models.api_atlas_user_metadata_view import ApiAtlasUserMetadataView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasResourcePolicyView(BaseModel):
    """Generated model for ApiAtlasResourcePolicyView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_by_user: ApiAtlasUserMetadataView | None = Field(default=None, alias="createdByUser")
    created_date: datetime | None = Field(default=None, alias="createdDate", description="Date and time in UTC when the atlas resource policy was created.")
    description: str | None = Field(default=None, description="Description of the atlas resource policy.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies the atlas resource policy.")
    last_updated_by_user: ApiAtlasUserMetadataView | None = Field(default=None, alias="lastUpdatedByUser")
    last_updated_date: datetime | None = Field(default=None, alias="lastUpdatedDate", description="Date and time in UTC when the atlas resource policy was last updated.")
    name: str | None = Field(default=None, description="Human-readable label that describes the atlas resource policy.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal character string that identifies the organization the atlas resource policy belongs to.")
    policies: list[ApiAtlasPolicyView] | None = Field(default=None, description="List of policies that make up the atlas resource policy.")
    version: str | None = Field(default=None, description="A string that identifies the version of the atlas resource policy.")
