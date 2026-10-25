"""Generated model for SearchSynonymMappingDefinition. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.admin.models.synonym_source import SynonymSource

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchSynonymMappingDefinition(BaseModel):
    """Synonyms used for this full text index."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    analyzer: Literal["lucene.standard", "lucene.simple", "lucene.whitespace", "lucene.keyword", "lucene.arabic", "lucene.armenian", "lucene.basque", "lucene.bengali", "lucene.brazilian", "lucene.bulgarian", "lucene.catalan", "lucene.chinese", "lucene.cjk", "lucene.czech", "lucene.danish", "lucene.dutch", "lucene.english", "lucene.finnish", "lucene.french", "lucene.galician", "lucene.german", "lucene.greek", "lucene.hindi", "lucene.hungarian", "lucene.indonesian", "lucene.irish", "lucene.italian", "lucene.japanese", "lucene.korean", "lucene.kuromoji", "lucene.latvian", "lucene.lithuanian", "lucene.morfologik", "lucene.nori", "lucene.norwegian", "lucene.persian", "lucene.portuguese", "lucene.romanian", "lucene.russian", "lucene.smartcn", "lucene.sorani", "lucene.spanish", "lucene.swedish", "lucene.thai", "lucene.turkish", "lucene.ukrainian"] = Field(description="Specific pre-defined method chosen to apply to the synonyms to be searched.")
    name: str = Field(description="Label that identifies the synonym definition. Each `synonym.name` must be unique within the same index definition.")
    source: SynonymSource
