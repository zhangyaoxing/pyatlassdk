"""Generated model for ShardKeys. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.shard_keys_key_item import ShardKeysKeyItem

from pydantic import BaseModel, ConfigDict, Field

class ShardKeys(BaseModel):
    """Document that configures the shard key on the destination cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    key: list[ShardKeysKeyItem] = Field(description="List of fields to use for the shard key.")
