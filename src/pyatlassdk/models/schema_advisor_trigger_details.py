"""Generated model for SchemaAdvisorTriggerDetails. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class SchemaAdvisorTriggerDetails(BaseModel):
    """Generated model for SchemaAdvisorTriggerDetails."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Description of the trigger type.")
    trigger_type: Literal["PERCENT_QUERIES_USE_LOOKUP", "NUMBER_OF_QUERIES_USE_LOOKUP", "DOCS_CONTAIN_UNBOUNDED_ARRAY", "NUMBER_OF_NAMESPACES", "DOC_SIZE_TOO_LARGE", "NUM_INDEXES", "QUERIES_CONTAIN_CASE_INSENSITIVE_REGEX"] | None = Field(default=None, alias="triggerType", description="Type of trigger.")
