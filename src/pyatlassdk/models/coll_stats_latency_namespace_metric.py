"""Generated model for CollStatsLatencyNamespaceMetric. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class CollStatsLatencyNamespaceMetric(BaseModel):
    """Coll Stats Latency metric name and its unit of measurement."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    metric_name: Literal["READS_OPS", "READS_LATENCY", "AVERAGE_READS_LATENCY", "READS_P50_VALUE", "READS_P95_VALUE", "READS_P99_VALUE", "WRITES_OPS", "WRITES_LATENCY", "AVERAGE_WRITES_LATENCY", "WRITES_P50_VALUE", "WRITES_P95_VALUE", "WRITES_P99_VALUE", "COMMANDS_OPS", "COMMANDS_LATENCY", "AVERAGE_COMMANDS_LATENCY", "COMMANDS_P50_VALUE", "COMMANDS_P95_VALUE", "COMMANDS_P99_VALUE", "TOTAL_OPS", "TOTAL_LATENCY", "AVERAGE_TOTAL_OPS_LATENCY", "TOTAL_OPS_P50_VALUE", "TOTAL_OPS_P95_VALUE", "TOTAL_OPS_P99_VALUE"] | None = Field(alias="metricName", description="Human-readable label that identifies this metric.")
    units: Literal["MILLISECONDS"] | None = Field(description="Unit of measurement that applies to this metric.")
