"""Generated model for ApiSearchDeploymentResponseView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.api_search_deployment_effective_spec_view import ApiSearchDeploymentEffectiveSpecView
from pyatlassdk.admin.models.api_search_deployment_response_view_auto_scaling import ApiSearchDeploymentResponseViewAutoScaling
from pyatlassdk.admin.models.api_search_deployment_spec_view import ApiSearchDeploymentSpecView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiSearchDeploymentResponseView(BaseModel):
    """Generated model for ApiSearchDeploymentResponseView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_scaling: ApiSearchDeploymentResponseViewAutoScaling | None = Field(default=None, alias="autoScaling", description="Autoscaling settings configured for this Search deployment.")
    baseline_specs: list[ApiSearchDeploymentEffectiveSpecView] | None = Field(default=None, alias="baselineSpecs", description="List of starting settings for the Search Nodes in each cluster region.")
    effective_specs: list[ApiSearchDeploymentEffectiveSpecView] | None = Field(default=None, alias="effectiveSpecs", description="List of settings that configure the Search Nodes for your cluster. Each entry describes one region or, when `shardId` is present, one shard in one region.")
    encryption_at_rest_provider: Annotated[Literal["NONE", "AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="encryptionAtRestProvider", description="Cloud service provider that manages your customer keys to provide an additional layer of Encryption At Rest for the cluster.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the search deployment.")
    specs: list[ApiSearchDeploymentSpecView] | None = Field(default=None, description="Deprecated. `specs` will be removed in a future release. We strongly recommend that you use `effectiveSpecs` instead.")
    state_name: Annotated[Literal["IDLE", "PAUSED", "UPDATING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="stateName", description="Human-readable label that indicates the current operating condition of this search deployment.")
