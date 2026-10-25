"""Generated model for AdditionalData. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdditionalData(BaseModel):
    """Additional metadata associated with the line item."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    processor_id: str | None = Field(default=None, alias="processorId", description="Identifier of the stream processor associated with the line item.")
    processor_name: str | None = Field(default=None, alias="processorName", description="Name of the stream processor associated with the line item.")
    workspace: str | None = Field(default=None, description="Workspace associated with the line item.")
