"""Generated model for SynonymSource. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SynonymSource(BaseModel):
    """Data set that stores words and their applicable synonyms."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection: str = Field(description="Label that identifies the MongoDB collection that stores words and their applicable synonyms.")
