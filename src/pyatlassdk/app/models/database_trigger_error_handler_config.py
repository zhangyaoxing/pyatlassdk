"""Generated model for DatabaseTriggerErrorHandlerConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerErrorHandlerConfig(BaseModel):
    """Generated model for DatabaseTriggerErrorHandlerConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="If 'true', custom error handling is enabled for the AWS EventBridge trigger.")
    function_id: str | None = Field(default=None, description="The ID of the function invoked when the AWS EventBridge \ntrigger fails and cannot be successfully retried.")
