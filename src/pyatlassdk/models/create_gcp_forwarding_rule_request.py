"""Generated model for CreateGCPForwardingRuleRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CreateGCPForwardingRuleRequest(BaseModel):
    """Generated model for CreateGCPForwardingRuleRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    endpoint_name: str | None = Field(default=None, alias="endpointName", description="Human-readable label that identifies the Google Cloud consumer forwarding rule that you created.")
    ip_address: str | None = Field(default=None, alias="ipAddress", description="One Private Internet Protocol version 4 (IPv4) address to which this Google Cloud consumer forwarding rule resolves.")
