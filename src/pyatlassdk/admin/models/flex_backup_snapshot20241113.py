"""Generated model for FlexBackupSnapshot20241113. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexBackupSnapshot20241113(BaseModel):
    """Details for one snapshot of a flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    expiration: datetime | None = Field(default=None, description="Date and time when the download link no longer works. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    finish_time: datetime | None = Field(default=None, alias="finishTime", description="Date and time when MongoDB Cloud completed writing this snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the snapshot.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    mongo_db_version: str | None = Field(default=None, alias="mongoDBVersion", description="MongoDB host version that the snapshot runs.")
    scheduled_time: datetime | None = Field(default=None, alias="scheduledTime", description="Date and time when MongoDB Cloud will take the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    start_time: datetime | None = Field(default=None, alias="startTime", description="Date and time when MongoDB Cloud began taking the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    status: Annotated[Literal["PENDING", "QUEUED", "RUNNING", "FAILED", "COMPLETED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Phase of the workflow for this snapshot at the time this resource made this request.")
