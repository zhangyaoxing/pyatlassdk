"""Generated model for PrivateEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PrivateEndpoint(BaseModel):
    """Generated model for PrivateEndpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    cloud_provider_region: str | None = Field(default=None, description="The cloud provider region that hosts the private endpoint.")
    cloud_provider_endpoint_id: str | None = Field(default=None, description="The private endpoint ID from the cloud provider.")
    comment: str | None = Field(default=None, description="An optional comment that describes the endpoint.")
    endpoint_type: Literal["sync", "general", "legacy"] | None = Field(default=None, description="The type of endpoint. For more information\non migrating deprecated `\"legacy\"` endpoints, see \n[Migrate Legacy Endpoints](https://www.mongodb.com/docs/atlas/app-services/security/private-endpoints/#migrate-a-legacy-endpoint).")
