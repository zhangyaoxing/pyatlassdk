"""Generated model for CloudProviderAccessGCPServiceAccount. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.cloud_provider_access_feature_usage import CloudProviderAccessFeatureUsage

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAccessGCPServiceAccount(BaseModel):
    """Details that describe the features linked to the GCP Service Account."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the role.")
    created_date: datetime | None = Field(default=None, alias="createdDate", description="Date and time when this Google Service Account was created. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    feature_usages: list[CloudProviderAccessFeatureUsage] | None = Field(default=None, alias="featureUsages", description="List that contains application features associated with this Google Service Account.")
    gcp_service_account_for_atlas: str | None = Field(default=None, alias="gcpServiceAccountForAtlas", description="Email address for the Google Service Account created by Atlas.")
    role_id: str | None = Field(default=None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies the role.")
    status: Annotated[Literal["IN_PROGRESS", "COMPLETE", "FAILED", "NOT_INITIATED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Provision status of the service account.")
