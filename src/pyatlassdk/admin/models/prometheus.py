"""Generated model for Prometheus. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Prometheus(BaseModel):
    """Details to integrate one Prometheus account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool = Field(description="Flag that indicates whether someone has activated the Prometheus integration.")
    id: str | None = Field(default=None, description="Integration id.")
    password: str | None = Field(default=None, description="Password needed to allow MongoDB Cloud to access your Prometheus account.")
    send_user_provided_resource_tags_enabled: bool | None = Field(default=None, alias="sendUserProvidedResourceTagsEnabled", description="Toggle sending user provided group and cluster resource tags with the Prometheus metrics.")
    service_discovery: Literal["http", "file"] = Field(alias="serviceDiscovery", description="Desired method to discover the Prometheus service.")
    type: Annotated[Literal["PROMETHEUS"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
    username: str = Field(description="Human-readable label that identifies your Prometheus incoming webhook.")
