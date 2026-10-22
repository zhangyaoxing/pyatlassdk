"""Generated model for StreamsStartProcessorFailover. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class StreamsStartProcessorFailover(BaseModel):
    """Failover options for starting a stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    clear_checkpoint: bool | None = Field(default=None, alias="clearCheckpoint", description="If true, clears the checkpoint so the failover processor does not resume from it. Applies only to FORCED failover; clearing may cause duplicate or missing records in the output.")
    dry_run: bool | None = Field(default=None, alias="dryRun", description="If true, simulates the operation without making any changes.")
    mode: Literal["GRACEFUL", "FORCED"] | None = Field(default=None, description="Strategy for the processor: GRACEFUL - attempt to stop the processor, error if processor cannot be stopped. if stop was successful, start the processor in the new region with the latest checkpoint.  FORCED - attempt to stop the processor, proceed to starting the processor in the new region with checkpoints disabled regardless of whether or not the stop succeeds.")
    region: str = Field(description="Cloud provider region where the stream processor should be started in failover mode. The region must be a valid region for the stream processor's cloud provider and must be included in the tenant's configured failover regions, or it may be the tenant's default (primary) region.")
