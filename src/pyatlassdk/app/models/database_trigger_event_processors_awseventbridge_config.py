"""Generated model for DatabaseTriggerEventProcessorsAWSEVENTBRIDGEConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerEventProcessorsAWSEVENTBRIDGEConfig(BaseModel):
    """Generated model for DatabaseTriggerEventProcessorsAWSEVENTBRIDGEConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    account_id: str | None = Field(default=None, description="An AWS Account ID.")
    region: str | None = Field(default=None, description="An AWS region.")
    extended_json_enabled: bool | None = Field(default=None, description="If `true`, event objects are serialized using EJSON.")
