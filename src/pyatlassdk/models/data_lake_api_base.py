"""Generated model for DataLakeApiBase. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeApiBase(BaseModel):
    """An aggregation pipeline that applies to the collection."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the view, which corresponds to an aggregation pipeline on a collection.")
    pipeline: str | None = Field(default=None, description="Aggregation pipeline stages to apply to the source collection.")
    source: str | None = Field(default=None, description="Human-readable label that identifies the source collection for the view.")
