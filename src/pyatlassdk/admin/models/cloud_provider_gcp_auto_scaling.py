"""Generated model for CloudProviderGCPAutoScaling. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.gcp_compute_auto_scaling import GCPComputeAutoScaling

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderGCPAutoScaling(BaseModel):
    """Range of instance sizes to which your cluster can scale."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: GCPComputeAutoScaling | None = None
