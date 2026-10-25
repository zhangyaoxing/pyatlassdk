"""Generated model for NamespaceObj. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NamespaceObj(BaseModel):
    """Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    type: Literal["collection"] | None = Field(default=None, description="Human-readable label that identifies the type of namespace.")
