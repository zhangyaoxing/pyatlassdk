"""Generated model for SplunkLogIntegrationResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SplunkLogIntegrationResponse(BaseModel):
    """Details to integrate Splunk log export with one Atlas project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-character hexadecimal digit string that identifies the log integration configuration.")
    log_types: list[Annotated[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"], BeforeValidator(upper_case)]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Annotated[Literal["SPLUNK_LOG_EXPORT"], BeforeValidator(upper_case)] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    hec_token: str = Field(alias="hecToken", description="HTTP Event Collector (HEC) token for authentication.")
    hec_url: str = Field(alias="hecUrl", description="HTTP Event Collector (HEC) endpoint URL.")
