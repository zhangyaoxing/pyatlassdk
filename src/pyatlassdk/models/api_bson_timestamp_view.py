"""Generated model for ApiBSONTimestampView. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class ApiBSONTimestampView(BaseModel):
    """BSON timestamp that indicates when the checkpoint token entry in the oplog occurred."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    date: datetime | None = Field(default=None, description="Date and time when the oplog recorded this database operation. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    increment: int | None = Field(default=None, description="Order of the database operation that the oplog recorded at specific date and time.")
