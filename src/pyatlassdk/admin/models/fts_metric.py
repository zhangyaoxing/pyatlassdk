"""Generated model for FTSMetric. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FTSMetric(BaseModel):
    """Measurement of one Atlas Search status when MongoDB Atlas received this request."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    metric_name: Annotated[Literal["INDEX_SIZE_ON_DISK", "NUMBER_OF_DELETES", "NUMBER_OF_ERROR_QUERIES", "NUMBER_OF_GETMORE_COMMANDS", "NUMBER_OF_INDEX_FIELDS", "NUMBER_OF_INSERTS", "NUMBER_OF_SUCCESS_QUERIES", "NUMBER_OF_UPDATES", "REPLICATION_LAG", "TOTAL_NUMBER_OF_QUERIES", "FTS_DISK_USAGE", "FTS_PROCESS_CPU_KERNEL", "FTS_PROCESS_CPU_USER", "FTS_PROCESS_NORMALIZED_CPU_KERNEL", "FTS_PROCESS_NORMALIZED_CPU_USER", "FTS_PROCESS_RESIDENT_MEMORY", "FTS_PROCESS_SHARED_MEMORY", "FTS_PROCESS_VIRTUAL_MEMORY", "JVM_CURRENT_MEMORY", "JVM_MAX_MEMORY", "PAGE_FAULTS"], BeforeValidator(upper_case)] | None = Field(alias="metricName", description="Human-readable label that identifies this Atlas Search hardware, status, or index measurement.")
    units: Annotated[Literal["BYTES", "BYTES_PER_SECOND", "GIGABYTES", "GIGABYTES_PER_HOUR", "KILOBYTES", "MEGABYTES", "MEGABYTES_PER_SECOND", "MILLISECONDS", "MILLISECONDS_LOGSCALE", "PERCENT", "SCALAR", "SCALAR_PER_SECOND", "SECONDS"], BeforeValidator(upper_case)] | None = Field(description="Unit of measurement that applies to this Atlas Search metric.")
