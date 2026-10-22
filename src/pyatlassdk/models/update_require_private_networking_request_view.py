"""Generated model for UpdateRequirePrivateNetworkingRequestView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class UpdateRequirePrivateNetworkingRequestView(BaseModel):
    """Request body to toggle the private-networking requirement for an existing export bucket."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    require_private_networking: bool = Field(alias="requirePrivateNetworking", description="True to require private networking; false to disable it.")
