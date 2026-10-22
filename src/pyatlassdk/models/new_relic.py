"""Generated model for NewRelic. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class NewRelic(BaseModel):
    """
    Details to integrate one New Relic account with one MongoDB Cloud project.

    ***IMPORTANT**: Effective Wednesday, June 16th, 2021, New Relic no longer supports the plugin-based integration with MongoDB. We do not recommend that you sign up for the plugin-based integration.

    Consider configuring an alternative monitoring integration before June 16th to maintain visibility into your MongoDB deployments.
    """
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    account_id: str = Field(alias="accountId", description="Unique 40-hexadecimal digit string that identifies your New Relic account.")
    id: str | None = Field(default=None, description="Integration id.")
    license_key: str = Field(alias="licenseKey", description="Unique 40-hexadecimal digit string that identifies your New Relic license.\n\n**IMPORTANT**: Effective Wednesday, June 16th, 2021, New Relic no longer supports the plugin-based integration with MongoDB. We do not recommend that you sign up for the plugin-based integration.\nConsider configuring an alternative monitoring integration before June 16th to maintain visibility into your MongoDB deployments.")
    read_token: str = Field(alias="readToken", description="Query key used to access your New Relic account.")
    type: Literal["NEW_RELIC"] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
    write_token: str = Field(alias="writeToken", description="Insert key associated with your New Relic account.")
