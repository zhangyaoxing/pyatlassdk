"""Generated model for AutoExportPolicyView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AutoExportPolicyView(BaseModel):
    """Policy for automatically exporting Cloud Backup Snapshots."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    export_bucket_id: str | None = Field(default=None, alias="exportBucketId", description="Unique 24-hexadecimal character string that identifies the Export Bucket.")
    frequency_type: Literal["monthly", "yearly"] | None = Field(default=None, alias="frequencyType", description="Human-readable label that indicates the rate at which the export policy item occurs.")
