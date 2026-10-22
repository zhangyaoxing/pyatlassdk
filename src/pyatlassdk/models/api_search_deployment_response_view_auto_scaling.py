"""Generated model for ApiSearchDeploymentResponseViewAutoScaling. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.api_search_compute_auto_scaling_view import ApiSearchComputeAutoScalingView

from pydantic import BaseModel, ConfigDict, Field

class ApiSearchDeploymentResponseViewAutoScaling(BaseModel):
    """Generated model for ApiSearchDeploymentResponseViewAutoScaling."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: ApiSearchComputeAutoScalingView | None = None
