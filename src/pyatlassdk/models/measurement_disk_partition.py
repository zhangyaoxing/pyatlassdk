"""Generated model for MeasurementDiskPartition. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MeasurementDiskPartition(BaseModel):
    """Generated model for MeasurementDiskPartition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    partition_name: str | None = Field(default=None, alias="partitionName", description="Human-readable label of the disk or partition to which the measurements apply.")
