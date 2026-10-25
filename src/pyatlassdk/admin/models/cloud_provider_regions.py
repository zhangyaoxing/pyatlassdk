"""Generated model for CloudProviderRegions. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.cluster_cloud_provider_instance_size import ClusterCloudProviderInstanceSize

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderRegions(BaseModel):
    """Generated model for CloudProviderRegions."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    instance_sizes: list[ClusterCloudProviderInstanceSize] | None = Field(default=None, alias="instanceSizes", description="List of instances sizes that this cloud provider supports.")
    provider: Annotated[Literal["AWS", "GCP", "AZURE"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the Cloud provider.")
