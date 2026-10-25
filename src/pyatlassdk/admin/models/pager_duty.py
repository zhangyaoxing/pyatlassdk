"""Generated model for PagerDuty. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PagerDuty(BaseModel):
    """Details to integrate one PagerDuty account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Integration id.")
    region: Annotated[Literal["US", "EU"], BeforeValidator(upper_case)] | None = Field(default=None, description="PagerDuty region that indicates the API Uniform Resource Locator (URL) to use.")
    service_key: str = Field(alias="serviceKey", description="Service key associated with your PagerDuty account.\n\n**NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:\n\n* View or edit the alert through the Atlas UI.\n\n* Query the alert for the notification through the Atlas Administration API.")
    type: Annotated[Literal["PAGER_DUTY"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
