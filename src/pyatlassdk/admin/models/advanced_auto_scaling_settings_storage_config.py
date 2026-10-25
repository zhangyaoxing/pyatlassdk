"""Generated model for AdvancedAutoScalingSettingsStorageConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdvancedAutoScalingSettingsStorageConfig(BaseModel):
    """Generated model for AdvancedAutoScalingSettingsStorageConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    shard_size_limit_gb: int | None = Field(default=None, alias="shardSizeLimitGB", description="Available in Public Preview: Maximum data size that MongoDB Cloud allows each shard of this cluster to reach, expressed in gigabytes. MongoDB Cloud rejects writes to a shard that reaches the limit that it enforces. In `replicationSpecs`, this field reports the limit that you configured, and MongoDB Cloud omits it when you never configured one. In `effectiveReplicationSpecs`, this field reports the limit that MongoDB Cloud enforces: usually the limit that you configured, otherwise the default limit that MongoDB Cloud assigns when it creates or updates the cluster. This value may differ from the limit that you configured due to system-managed changes. This limit applies to every shard of the cluster; set the same value on each region configuration's `autoScaling`, as MongoDB Cloud rejects requests that specify differing values. You can set this only on Atlas INFINITE clusters: MongoDB Cloud rejects any request that names this field, including as `null`, for a cluster or node type that doesn't support it. In a request that includes `replicationSpecs`, omitting `shardSizeLimitGB` or sending it as `null` clears the limit. Omitting `replicationSpecs` preserves it.")
