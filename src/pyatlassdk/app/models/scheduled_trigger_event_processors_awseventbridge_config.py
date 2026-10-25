"""Generated model for ScheduledTriggerEventProcessorsAWSEVENTBRIDGEConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ScheduledTriggerEventProcessorsAWSEVENTBRIDGEConfig(BaseModel):
    """Generated model for ScheduledTriggerEventProcessorsAWSEVENTBRIDGEConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    account_id: str | None = Field(default=None, description="An AWS Account ID.")
    region: str | None = Field(default=None, description="An AWS region.")
    extended_json_enabled: bool | None = Field(default=None, description="If `true`, event objects are serialized using EJSON.")
