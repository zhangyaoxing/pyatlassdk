"""Generated model for CreateGCPEndpointGroupRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.create_gcp_forwarding_rule_request import CreateGCPForwardingRuleRequest

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CreateGCPEndpointGroupRequest(BaseModel):
    """Group of Private Endpoint settings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Cloud service provider that manages this private endpoint.")
    endpoint_group_name: str = Field(alias="endpointGroupName", description="Human-readable label that identifies a set of endpoints. If this private endpoint belongs to a port-mapped endpoint service, this field is still required but ignored.")
    endpoints: list[CreateGCPForwardingRuleRequest] | None = Field(default=None, description="List of individual private endpoints that comprise this endpoint group. If this endpoint belongs to a port-mapped endpoint service, this field will only take in a list of one private endpoint.")
    gcp_project_id: str = Field(alias="gcpProjectId", description="Unique string that identifies the Google Cloud project in which you created the endpoints. Specify the Google Cloud project ID or project number.")
