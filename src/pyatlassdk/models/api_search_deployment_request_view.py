"""Generated model for ApiSearchDeploymentRequestView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.api_search_deployment_request_spec_view import ApiSearchDeploymentRequestSpecView
from pyatlassdk.models.api_search_deployment_request_view_auto_scaling import ApiSearchDeploymentRequestViewAutoScaling

from pydantic import BaseModel, ConfigDict, Field

class ApiSearchDeploymentRequestView(BaseModel):
    """Generated model for ApiSearchDeploymentRequestView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_scaling: ApiSearchDeploymentRequestViewAutoScaling | None = Field(default=None, alias="autoScaling", description="Settings that let Atlas change the Search Node tier on its own. Bounds apply to the whole deployment, and Atlas scales each region and shard independently within them. Omit to keep autoscaling off.")
    default_node_count: int | None = Field(default=None, alias="defaultNodeCount", description="Default number of Search Nodes per region. Applied to a region without an explicit override.")
    specs: list[ApiSearchDeploymentRequestSpecView] = Field(description="List of settings that configure the Search Nodes for your cluster. Provide one element per region when configuring asymmetric deployments; a single element applies to all regions.")
