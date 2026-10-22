"""Generated model for CloudProviderAccessGCPServiceAccountRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.cloud_provider_access_feature_usage import CloudProviderAccessFeatureUsage

from pydantic import BaseModel, ConfigDict, Field

class CloudProviderAccessGCPServiceAccountRequest(BaseModel):
    """Details that describe the features linked to the GCP Service Account."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_date: datetime | None = Field(default=None, alias="createdDate", description="Date and time when this GCP Service Account was created. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    feature_usages: list[CloudProviderAccessFeatureUsage] | None = Field(default=None, alias="featureUsages", description="List that contains application features associated with this GCP Service Account.")
    gcp_service_account_for_atlas: str | None = Field(default=None, alias="gcpServiceAccountForAtlas", description="ID string that identifies the GCP Service Account used by Atlas.")
    provider_name: Literal["AWS", "AZURE", "GCP"] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the role.")
    role_id: str | None = Field(default=None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies the role.")
