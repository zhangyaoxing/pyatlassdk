"""Generated model for SearchIndexCreateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchIndexCreateRequest(BaseModel):
    """Generated model for SearchIndexCreateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_name: str = Field(alias="collectionName", description="Label that identifies the collection to create an Atlas Search index in.")
    database: str = Field(description="Label that identifies the database that contains the collection to create an Atlas Search index in.")
    name: str = Field(description="Label that identifies this index. Within each namespace, names of all indexes in the namespace must be unique.")
    type: Literal["search", "vectorSearch"] | None = Field(default=None, description="Type of the index. The default type is search.")
