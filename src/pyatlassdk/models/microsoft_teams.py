"""Generated model for MicrosoftTeams. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MicrosoftTeams(BaseModel):
    """Details to integrate one Microsoft Teams account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Integration id.")
    microsoft_teams_webhook_url: str = Field(alias="microsoftTeamsWebhookUrl", description="Endpoint web address of the Microsoft Teams webhook to which MongoDB Cloud sends notifications.\n\n**NOTE**: When you view or edit the alert for a Microsoft Teams notification, the URL appears partially redacted.")
    type: Annotated[Literal["MICROSOFT_TEAMS"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
