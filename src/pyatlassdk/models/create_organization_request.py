"""Generated model for CreateOrganizationRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.create_atlas_organization_api_key import CreateAtlasOrganizationApiKey
from pyatlassdk.models.org_service_account_request import OrgServiceAccountRequest

from pydantic import BaseModel, ConfigDict, Field

class CreateOrganizationRequest(BaseModel):
    """Generated model for CreateOrganizationRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key: CreateAtlasOrganizationApiKey | None = Field(default=None, alias="apiKey")
    federation_settings_id: str | None = Field(default=None, alias="federationSettingsId", description="Unique 24-hexadecimal digit string that identifies the federation to link the newly created organization to. If specified, the proposed Organization Owner of the new organization must have the Organization Owner role in an organization associated with the federation.")
    name: str = Field(description="Human-readable label that identifies the organization.")
    org_owner_id: str | None = Field(default=None, alias="orgOwnerId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user that you want to assign the Organization Owner role. This user must be a member of the same organization as the calling API key. If you provide `federationSettingsId`,  this user must instead have the Organization Owner role on an organization in the specified federation. This parameter is required only when you authenticate with Programmatic API Keys.")
    service_account: OrgServiceAccountRequest | None = Field(default=None, alias="serviceAccount")
    skip_default_alerts_settings: bool | None = Field(default=None, alias="skipDefaultAlertsSettings", description="Disables automatic alert creation. When set to true, no organization level alerts will be created automatically.")
