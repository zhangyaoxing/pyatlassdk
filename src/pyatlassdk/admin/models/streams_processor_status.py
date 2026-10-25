"""Generated model for StreamsProcessorStatus. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsProcessorStatus(BaseModel):
    """Desired status change to apply to a tenant's stream processors."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    mode: Annotated[Literal["GRACEFUL", "FORCED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Strategy for the processor: GRACEFUL - attempt to stop the processor, error if processor cannot be stopped. if stop was successful, start the processor in the new region with the latest checkpoint.  FORCED - attempt to stop the processor, proceed to starting the processor in the new region with checkpoints disabled regardless of whether or not the stop succeeds.")
    region: str | None = Field(default=None, description="Name of the region against which to apply the status change. Required when `status` is `FAILED_OVER`; optional otherwise.")
    status: Annotated[Literal["STARTED", "STOPPED", "FAILED_OVER"], BeforeValidator(upper_case)] = Field(description="Represents the desired action to apply to stream processors within a workspace, such as starting all processors, stopping all processors, or performing a bulk regional failover.")
