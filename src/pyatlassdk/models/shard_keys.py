"""Generated model for ShardKeys. Do not edit manually."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ShardKeys(BaseModel):
    """Document that configures the shard key on the destination cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    key: list[dict[str, dict[str, Any]]] = Field(description="List of fields to use for the shard key.")
