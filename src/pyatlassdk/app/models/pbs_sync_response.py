"""Generated model for PbsSyncResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.partition import Partition

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PbsSyncResponse(BaseModel):
    """Generated model for PbsSyncResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    service_id: str | None = Field(default=None, description="The Service ID for the currently synced cluster, if there is one.")
    partition_fields: list[Partition] | None = Field(default=None, description="A list of valid partition keys based on the cluster's collection\nschemas.")
