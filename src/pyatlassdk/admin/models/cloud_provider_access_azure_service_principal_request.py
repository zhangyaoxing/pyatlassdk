"""Generated model for CloudProviderAccessAzureServicePrincipalRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.cloud_provider_access_feature_usage import CloudProviderAccessFeatureUsage

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAccessAzureServicePrincipalRequest(BaseModel):
    """Details that describe the features linked to the Azure Service Principal."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the role.")
    atlas_azure_app_id: str | None = Field(default=None, alias="atlasAzureAppId", description="Azure Active Directory Application ID of Atlas. This field is optional and will be derived from the Azure subscription if not provided.")
    created_date: datetime | None = Field(default=None, alias="createdDate", description="Date and time when this Azure Service Principal was created. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    feature_usages: list[CloudProviderAccessFeatureUsage] | None = Field(default=None, alias="featureUsages", description="List that contains application features associated with this Azure Service Principal.")
    last_updated_date: datetime | None = Field(default=None, alias="lastUpdatedDate", description="Date and time when this Azure Service Principal was last updated. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the role.")
    service_principal_id: str | None = Field(default=None, alias="servicePrincipalId", description="UUID string that identifies the Azure Service Principal.")
    tenant_id: str | None = Field(default=None, alias="tenantId", description="UUID String that identifies the Azure Active Directory Tenant ID.")
