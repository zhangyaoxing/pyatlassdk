"""Generated model for CloudProviderAccessFeatureUsage. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAccessFeatureUsage(BaseModel):
    """MongoDB Cloud features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    feature_type: Annotated[Literal["ATLAS_DATA_LAKE", "ENCRYPTION_AT_REST", "EXPORT_SNAPSHOT", "PUSH_BASED_LOG_EXPORT", "ATLAS_LOG_INTEGRATION"], BeforeValidator(upper_case)] | None = Field(default=None, alias="featureType", description="Human-readable label that describes one MongoDB Cloud feature linked to this Amazon Web Services (AWS) Identity and Access Management (IAM) role.")
