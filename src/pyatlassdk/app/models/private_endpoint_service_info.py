"""Generated model for PrivateEndpointServiceInfo. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PrivateEndpointServiceInfo(BaseModel):
    """Generated model for PrivateEndpointServiceInfo."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider_region: str | None = None
    service_name: str | None = None
    endpoint_type: Literal["sync", "general", "legacy"] | None = Field(default=None, description="The type of endpoint. For more information\non migrating deprecated `\"legacy\"` endpoints, see \n[Migrate Legacy Endpoints](https://www.mongodb.com/docs/atlas/app-services/security/private-endpoints/#migrate-a-legacy-endpoint).")
