"""Generated model for DatabaseTriggerErrorHandler. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.database_trigger_error_handler_config import DatabaseTriggerErrorHandlerConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerErrorHandler(BaseModel):
    """Generated model for DatabaseTriggerErrorHandler."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: DatabaseTriggerErrorHandlerConfig | None = None
