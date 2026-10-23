"""Generated model for TenantHardwareSpec20240805. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class TenantHardwareSpec20240805(BaseModel):
    """Generated model for TenantHardwareSpec20240805."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    disk_size_gb: float | None = Field(default=None, alias="diskSizeGB", description="Storage capacity of instance data volumes expressed in gigabytes. Increase this number to add capacity.\n\n This value must be equal for all shards and node types.\n\n This value is not configurable on M0/M2/M5 clusters.\n\n MongoDB Cloud requires this parameter if you set `replicationSpecs`.\n\n If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. \n\n Storage charge calculations depend on whether you choose the default value or a custom value.\n\n The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.")
    effective_instance_size: Annotated[Literal["FLEX", "M2", "M5", "M0"], BeforeValidator(upper_case)] | None = Field(default=None, alias="effectiveInstanceSize", description="The true tenant instance size. This is present to support backwards compatibility for deprecated provider types and/or instance sizes.")
    instance_size: Annotated[Literal["M0", "M2", "M5"], BeforeValidator(upper_case)] | None = Field(default=None, alias="instanceSize", description="Hardware specification for the instances in this M0/M2/M5 tier cluster.")
