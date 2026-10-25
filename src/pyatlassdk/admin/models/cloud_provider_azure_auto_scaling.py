"""Generated model for CloudProviderAzureAutoScaling. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.azure_compute_auto_scaling_rules import AzureComputeAutoScalingRules

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAzureAutoScaling(BaseModel):
    """Range of instance sizes to which your cluster can scale."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: AzureComputeAutoScalingRules | None = None
