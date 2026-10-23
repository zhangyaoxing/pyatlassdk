"""Generated model for OpsGenie. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OpsGenie(BaseModel):
    """Details to integrate one OpsGenie account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key: str = Field(alias="apiKey", description="Key that allows MongoDB Cloud to access your OpsGenie account.\n\n**NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:\n\n* View or edit the alert through the Atlas UI.\n\n* Query the alert for the notification through the Atlas Administration API.")
    id: str | None = Field(default=None, description="Integration id.")
    region: Annotated[Literal["US", "EU"], BeforeValidator(upper_case)] | None = Field(default=None, description="Two-letter code that indicates which regional URL MongoDB uses to access the OpsGenie API.")
    type: Annotated[Literal["OPS_GENIE"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
