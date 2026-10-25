"""Generated model for MongoDBAccessLogsList. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.mongo_db_access_logs import MongoDBAccessLogs

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MongoDBAccessLogsList(BaseModel):
    """Generated model for MongoDBAccessLogsList."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access_logs: list[MongoDBAccessLogs] | None = Field(default=None, alias="accessLogs", description="Authentication attempt, one per object, made against the cluster.")
