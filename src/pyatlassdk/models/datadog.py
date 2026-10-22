"""Generated model for Datadog. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class Datadog(BaseModel):
    """Details to integrate one Datadog account with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key: str = Field(alias="apiKey", description="Key that allows MongoDB Cloud to access your Datadog account.\n\n**NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:\n\n* View or edit the alert through the Atlas UI.\n\n* Query the alert for the notification through the Atlas Administration API.")
    id: str | None = Field(default=None, description="Integration id.")
    region: Literal["US", "EU", "US3", "US5", "AP1", "AP2", "US1_FED"] | None = Field(default=None, description="Two-letter code that indicates which regional URL MongoDB uses to access the Datadog API.")
    send_collection_latency_metrics: bool | None = Field(default=None, alias="sendCollectionLatencyMetrics", description="Toggle sending collection latency metrics that includes database names and collection names and latency metrics on reads, writes, commands, and transactions.")
    send_database_metrics: bool | None = Field(default=None, alias="sendDatabaseMetrics", description="Toggle sending database metrics that includes database names and metrics on the number of collections, storage size, and index size.")
    send_query_stats_metrics: bool | None = Field(default=None, alias="sendQueryStatsMetrics", description="Toggle sending query shape metrics that includes query hash and metrics on latency, execution frequency, documents returned, and timestamps.")
    send_sharding_metrics: bool | None = Field(default=None, alias="sendShardingMetrics", description="Toggle sending sharding metrics that includes sharding distribution and chunk metrics per cluster, shard, and collection.")
    send_user_provided_resource_tags: bool | None = Field(default=None, alias="sendUserProvidedResourceTags", description="Toggle sending user provided group and cluster resource tags with the Datadog metrics.")
    type: Literal["DATADOG"] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
