"""Generated model for SampleDatasetStatus. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class SampleDatasetStatus(BaseModel):
    """Generated model for SampleDatasetStatus."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal character string that identifies this sample dataset.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster into which you loaded the sample dataset.")
    complete_date: datetime | None = Field(default=None, alias="completeDate", description="Date and time when the sample dataset load job completed. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    create_date: datetime | None = Field(default=None, alias="createDate", description="Date and time when you started the sample dataset load job. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Details of the error returned when MongoDB Cloud loads the sample dataset. This endpoint returns null if state has a value other than FAILED.")
    state: Literal["WORKING", "FAILED", "COMPLETED"] | None = Field(default=None, description="Status of the sample dataset load job.")
