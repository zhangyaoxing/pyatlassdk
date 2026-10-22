"""Generated model for PartitionFieldView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class PartitionFieldView(BaseModel):
    """Metadata to partition this online archive."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    field_name: str = Field(alias="fieldName", description="Human-readable label that identifies the parameter that MongoDB Cloud uses to partition data. To specify a nested parameter, use the dot notation.")
    field_type: Literal["date", "int", "long", "objectId", "string", "uuid"] | None = Field(default=None, alias="fieldType", description="Data type of the parameter that that MongoDB Cloud uses to partition data. Partition parameters of type UUID must be of binary subtype 4. MongoDB Cloud skips partition parameters of type UUID with subtype 3.")
    order: int = Field(description="Sequence in which MongoDB Cloud slices the collection data to create partitions. The resource expresses this sequence starting with zero. The value of the `criteria.dateField` parameter defaults as the first item in the partition sequence.")
