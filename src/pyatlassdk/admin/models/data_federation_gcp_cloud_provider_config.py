"""Generated model for DataFederationGCPCloudProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataFederationGCPCloudProviderConfig(BaseModel):
    """Configuration for running Data Federation in GCP."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    gcp_service_account: str | None = Field(default=None, alias="gcpServiceAccount", description="The email address of the Google Cloud Platform (GCP) service account created by Atlas which should be authorized to allow Atlas to access Google Cloud Storage.")
    role_id: str = Field(alias="roleId", description="Unique identifier of the role that Data Federation can use to access the data stores. Required if specifying `cloudProviderConfig`.")
