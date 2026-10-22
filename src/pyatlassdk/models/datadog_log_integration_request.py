"""Generated model for DatadogLogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DatadogLogIntegrationRequest(BaseModel):
    """Request schema for creating or updating a Datadog log export integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Literal["DATADOG_LOG_EXPORT"] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    api_key: str = Field(alias="apiKey", description="API key for authentication.")
    region: Literal["US1", "US3", "US5", "EU", "AP1", "AP2", "US1_FED"] = Field(description="Datadog site/region for log ingestion. Valid values: US1, US3, US5, EU, AP1, AP2, US1_FED.")
