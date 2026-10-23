"""Generated model for Raw. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Raw(BaseModel):
    """Additional meta information captured about this event. The response returns this parameter as a JSON object when the query parameter `includeRaw=true`. The list of fields in the raw document may change. Don't rely on raw values for formal monitoring."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    t: str | None = Field(default=None, alias="_t", description="Unique identifier of event type.")
    alert_config_id: str | None = Field(default=None, alias="alertConfigId", description="Unique 24-hexadecimal digit string that identifies the alert configuration related to the event.")
    cid: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred.")
    cre: datetime | None = Field(default=None, description="Date and time when this event occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    description: str | None = Field(default=None, description="Description of the event.")
    gn: str | None = Field(default=None, description="Human-readable label that identifies the project.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the event.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    org_name: str | None = Field(default=None, alias="orgName", description="Human-readable label that identifies the organization that contains the project.")
    severity: Annotated[Literal["INFO", "WARNING", "ERROR", "CRITICAL"], BeforeValidator(upper_case)] | None = Field(default=None, description="Severity of the event.")
