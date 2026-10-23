"""Generated model for DiskBackupOnDemandCopyPolicyItem. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupOnDemandCopyPolicyItem(BaseModel):
    """Specifications for one on-demand copy policy item."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    frequency_type: Literal["daily", "hourly", "weekly", "monthly", "yearly", "ondemand"] = Field(alias="frequencyType", description="Human-readable label that identifies the frequency type associated with the copy policy.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this copy policy item.")
