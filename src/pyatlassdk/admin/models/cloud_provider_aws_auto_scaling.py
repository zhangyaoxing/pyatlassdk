"""Generated model for CloudProviderAWSAutoScaling. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.aws_compute_auto_scaling import AWSComputeAutoScaling

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAWSAutoScaling(BaseModel):
    """Range of instance sizes to which your cluster can scale."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: AWSComputeAutoScaling | None = None
