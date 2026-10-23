"""Generated model for StreamsTenantUpdateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.base_streams_region import BaseStreamsRegion
from pyatlassdk.models.link import Link
from pyatlassdk.models.stream_config import StreamConfig
from pyatlassdk.models.streams_data_process_region import StreamsDataProcessRegion
from pyatlassdk.models.streams_processor_status import StreamsProcessorStatus

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsTenantUpdateRequest(BaseModel):
    """Details to update a stream tenant, optionally accompanied by a processor status change (for example, triggering bulk regional failover)."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "GCP", "AZURE", "TENANT", "SERVERLESS"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    failover_regions: list[StreamsDataProcessRegion] | None = Field(default=None, alias="failoverRegions", description="Failover regions for the stream workspace.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    processor_status: StreamsProcessorStatus | None = Field(default=None, alias="processorStatus")
    region: BaseStreamsRegion | None = None
    stream_config: StreamConfig | None = Field(default=None, alias="streamConfig")
