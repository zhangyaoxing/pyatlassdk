"""Generated model for DatadogLogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatadogLogIntegrationRequest(BaseModel):
    """Request schema for creating or updating a Datadog log export integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Annotated[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"], BeforeValidator(upper_case)]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Annotated[Literal["DATADOG_LOG_EXPORT"], BeforeValidator(upper_case)] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    api_key: str = Field(alias="apiKey", description="API key for authentication.")
    region: Annotated[Literal["US1", "US3", "US5", "EU", "AP1", "AP2", "US1_FED"], BeforeValidator(upper_case)] = Field(description="Datadog site/region for log ingestion. Valid values: US1, US3, US5, EU, AP1, AP2, US1_FED.")
