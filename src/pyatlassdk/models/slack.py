"""Generated model for Slack. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class Slack(BaseModel):
    """Details to integrate one Slack account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_token: str = Field(alias="apiToken", description="Key that allows MongoDB Cloud to access your Slack account.\n\n**NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:\n\n* View or edit the alert through the Atlas UI.\n\n* Query the alert for the notification through the Atlas Administration API.\n\n**IMPORTANT**: Slack integrations now use the OAuth2 verification method and must  be initially configured, or updated from a legacy integration, through the Atlas  third-party service integrations page. Legacy tokens will soon no longer be  supported.")
    channel_name: str | None = Field(alias="channelName", description="Name of the Slack channel to which MongoDB Cloud sends alert notifications.")
    id: str | None = Field(default=None, description="Integration id.")
    team_name: str | None = Field(default=None, alias="teamName", description="Human-readable label that identifies your Slack team. Set this parameter when you configure a legacy Slack integration.")
    type: Literal["SLACK"] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
