"""Generated model for OrgOtelLogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.org_log_integration_header import OrgLogIntegrationHeader

from pydantic import BaseModel, ConfigDict, Field

class OrgOtelLogIntegrationRequest(BaseModel):
    """Request schema for creating an organization-level OpenTelemetry log integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Literal["EVENTS"]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Literal["OTEL_LOG_EXPORT"] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    otel_endpoint: str = Field(alias="otelEndpoint", description="OpenTelemetry collector endpoint URL. Must be HTTPS and not exceed 2048 characters.")
    otel_supplied_headers: list[OrgLogIntegrationHeader] = Field(alias="otelSuppliedHeaders", description="HTTP headers for authentication and configuration. Maximum 10 headers, total size limit 2KB.")
