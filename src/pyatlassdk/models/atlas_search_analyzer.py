"""Generated model for AtlasSearchAnalyzer. Do not edit manually."""

from __future__ import annotations

from typing import Any
from pyatlassdk.models.basic_db_object import BasicDBObject

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasSearchAnalyzer(BaseModel):
    """Generated model for AtlasSearchAnalyzer."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    char_filters: list[BasicDBObject] | None = Field(default=None, alias="charFilters", description="Filters that examine text one character at a time and perform filtering operations.")
    name: str = Field(description="Name that identifies the custom analyzer. Names must be unique within an index, and must not start with any of the following strings:\n- `lucene.`\n- `builtin.`\n- `mongodb.`")
    token_filters: list[BasicDBObject] | None = Field(default=None, alias="tokenFilters", description="Filter that performs operations such as:\n\n- Stemming, which reduces related words, such as \"talking\", \"talked\", and \"talks\" to their root word \"talk\".\n\n- Redaction, which is the removal of sensitive information from public documents.")
    tokenizer: dict[str, dict[str, Any]] = Field(description="Tokenizer that you want to use to create tokens. Tokens determine how Atlas Search splits up text into discrete chunks for indexing.")
