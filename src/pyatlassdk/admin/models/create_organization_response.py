"""Generated model for CreateOrganizationResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.api_key_user_details import ApiKeyUserDetails
from pyatlassdk.admin.models.atlas_organization import AtlasOrganization
from pyatlassdk.admin.models.org_service_account import OrgServiceAccount

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CreateOrganizationResponse(BaseModel):
    """Generated model for CreateOrganizationResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key: ApiKeyUserDetails | None = Field(default=None, alias="apiKey")
    federation_settings_id: str | None = Field(default=None, alias="federationSettingsId", description="Unique 24-hexadecimal digit string that identifies the federation that you linked the newly created organization to.")
    org_owner_id: str | None = Field(default=None, alias="orgOwnerId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user that you assigned the Organization Owner role in the new organization.")
    organization: AtlasOrganization | None = None
    service_account: OrgServiceAccount | None = Field(default=None, alias="serviceAccount")
    skip_default_alerts_settings: bool | None = Field(default=None, alias="skipDefaultAlertsSettings", description="Disables automatic alert creation. When set to true, no organization level alerts will be created automatically.")
