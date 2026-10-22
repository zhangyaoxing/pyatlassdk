"""Generated model for CreateDataProcessRegionView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class CreateDataProcessRegionView(BaseModel):
    """Settings to configure the region where you wish to store your archived data."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "AZURE", "GCP"] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the Cloud service provider where you wish to store your archived data. `AZURE` or `GCP` may be selected only if it is the Cloud service provider for the cluster and no archives for any other cloud provider have been created for the cluster.")
