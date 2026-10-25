"""Generated model for OtelLogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.header import Header

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OtelLogIntegrationRequest(BaseModel):
    """Request schema for creating or updating an OpenTelemetry log export integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Annotated[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"], BeforeValidator(upper_case)]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Annotated[Literal["OTEL_LOG_EXPORT"], BeforeValidator(upper_case)] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    otel_endpoint: str = Field(alias="otelEndpoint", description="OpenTelemetry collector endpoint URL. Must be HTTPS and not exceed 2048 characters.")
    otel_supplied_headers: list[Header] = Field(alias="otelSuppliedHeaders", description="HTTP headers for authentication and configuration. Maximum 10 headers, total size limit 2KB.")
