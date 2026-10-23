"""Generated model for FlexBackupRestoreJobCreate20241113. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexBackupRestoreJobCreate20241113(BaseModel):
    """Details to create one restore job of a flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delivery_type: Annotated[Literal["RESTORE", "DOWNLOAD"], BeforeValidator(upper_case)] | None = Field(default=None, alias="deliveryType", description="Means by which this resource returns the snapshot to the requesting MongoDB Cloud user.")
    expiration_date: datetime | None = Field(default=None, alias="expirationDate", description="Date and time when the download link no longer works. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the restore job.")
    instance_name: str | None = Field(default=None, alias="instanceName", description="Human-readable label that identifies the source instance.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    project_id: str | None = Field(default=None, alias="projectId", description="Unique 24-hexadecimal digit string that identifies the project from which the restore job originated.")
    restore_finished_date: datetime | None = Field(default=None, alias="restoreFinishedDate", description="Date and time when MongoDB Cloud completed writing this snapshot. MongoDB Cloud changes the status of the restore job to `CLOSED`. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    restore_scheduled_date: datetime | None = Field(default=None, alias="restoreScheduledDate", description="Date and time when MongoDB Cloud will restore this snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    snapshot_finished_date: datetime | None = Field(default=None, alias="snapshotFinishedDate", description="Date and time when MongoDB Cloud completed writing this snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    snapshot_id: str = Field(alias="snapshotId", description="Unique 24-hexadecimal digit string that identifies the snapshot to restore.")
    snapshot_url: str | None = Field(default=None, alias="snapshotUrl", description="Internet address from which you can download the compressed snapshot files. The resource returns this parameter when  `\"deliveryType\" : \"DOWNLOAD\"`.")
    status: Annotated[Literal["PENDING", "QUEUED", "RUNNING", "FAILED", "COMPLETED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Phase of the restore workflow for this job at the time this resource made this request.")
    target_deployment_item_name: str = Field(alias="targetDeploymentItemName", description="Human-readable label that identifies the instance or cluster on the target project to which you want to restore the snapshot. You can restore the snapshot to another flex cluster or dedicated cluster tier.")
    target_project_id: str | None = Field(default=None, alias="targetProjectId", description="Unique 24-hexadecimal digit string that identifies the project that contains the instance or cluster to which you want to restore the snapshot.")
