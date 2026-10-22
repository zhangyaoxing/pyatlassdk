"""Generated model for VictorOps. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class VictorOps(BaseModel):
    """Details to integrate one Splunk On-Call account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key: str = Field(alias="apiKey", description="Key that allows MongoDB Cloud to access your VictorOps account.\n\n**NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:\n\n* View or edit the alert through the Atlas UI.\n\n* Query the alert for the notification through the Atlas Administration API.")
    id: str | None = Field(default=None, description="Integration id.")
    routing_key: str | None = Field(default=None, alias="routingKey", description="Routing key associated with your Splunk On-Call account.")
    type: Literal["VICTOR_OPS"] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
