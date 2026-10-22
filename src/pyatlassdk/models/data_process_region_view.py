"""Generated model for DataProcessRegionView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DataProcessRegionView(BaseModel):
    """Settings to configure the region where you wish to store your archived data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "AZURE", "GCP"] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the Cloud service provider where you store your archived data.")
