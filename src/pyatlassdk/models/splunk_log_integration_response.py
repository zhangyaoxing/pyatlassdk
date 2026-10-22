"""Generated model for SplunkLogIntegrationResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class SplunkLogIntegrationResponse(BaseModel):
    """Details to integrate Splunk log export with one Atlas project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-character hexadecimal digit string that identifies the log integration configuration.")
    log_types: list[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Literal["SPLUNK_LOG_EXPORT"] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    hec_token: str = Field(alias="hecToken", description="HTTP Event Collector (HEC) token for authentication.")
    hec_url: str = Field(alias="hecUrl", description="HTTP Event Collector (HEC) endpoint URL.")
