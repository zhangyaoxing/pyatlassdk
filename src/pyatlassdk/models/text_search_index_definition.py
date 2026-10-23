"""Generated model for TextSearchIndexDefinition. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.atlas_search_analyzer import AtlasSearchAnalyzer
from pyatlassdk.models.search_mappings import SearchMappings
from pyatlassdk.models.search_synonym_mapping_definition import SearchSynonymMappingDefinition
from pyatlassdk.models.search_type_sets import SearchTypeSets
from pyatlassdk.models.text_search_index_definition_sort import TextSearchIndexDefinitionSort
from pyatlassdk.models.text_search_index_definition_stored_source import TextSearchIndexDefinitionStoredSource

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class TextSearchIndexDefinition(BaseModel):
    """The text search index definition set by the user."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    analyzer: Literal["lucene.standard", "lucene.simple", "lucene.whitespace", "lucene.keyword", "lucene.arabic", "lucene.armenian", "lucene.basque", "lucene.bengali", "lucene.brazilian", "lucene.bulgarian", "lucene.catalan", "lucene.chinese", "lucene.cjk", "lucene.czech", "lucene.danish", "lucene.dutch", "lucene.english", "lucene.finnish", "lucene.french", "lucene.galician", "lucene.german", "lucene.greek", "lucene.hindi", "lucene.hungarian", "lucene.indonesian", "lucene.irish", "lucene.italian", "lucene.japanese", "lucene.korean", "lucene.kuromoji", "lucene.latvian", "lucene.lithuanian", "lucene.morfologik", "lucene.nori", "lucene.norwegian", "lucene.persian", "lucene.portuguese", "lucene.romanian", "lucene.russian", "lucene.smartcn", "lucene.sorani", "lucene.spanish", "lucene.swedish", "lucene.thai", "lucene.turkish", "lucene.ukrainian"] | None = Field(default=None, description="Specific pre-defined method chosen to convert database field text into searchable words. This conversion reduces the text of fields into the smallest units of text. These units are called a **term** or **token**. This process, known as tokenization, involves making the following changes to the text in fields:\n\n- extracting words\n- removing punctuation\n- removing accents\n- changing to lowercase\n- removing common words\n- reducing words to their root form (stemming)\n- changing words to their base form (lemmatization)\n MongoDB Cloud uses the process you select to build the Atlas Search index.")
    analyzers: list[AtlasSearchAnalyzer] | None = Field(default=None, description="List of user-defined methods to convert database field text into searchable words.")
    mappings: SearchMappings
    num_partitions: int | None = Field(default=None, alias="numPartitions", description="Number of index partitions. Allowed values are [1, 2, 4].")
    search_analyzer: Literal["lucene.standard", "lucene.simple", "lucene.whitespace", "lucene.keyword", "lucene.arabic", "lucene.armenian", "lucene.basque", "lucene.bengali", "lucene.brazilian", "lucene.bulgarian", "lucene.catalan", "lucene.chinese", "lucene.cjk", "lucene.czech", "lucene.danish", "lucene.dutch", "lucene.english", "lucene.finnish", "lucene.french", "lucene.galician", "lucene.german", "lucene.greek", "lucene.hindi", "lucene.hungarian", "lucene.indonesian", "lucene.irish", "lucene.italian", "lucene.japanese", "lucene.korean", "lucene.kuromoji", "lucene.latvian", "lucene.lithuanian", "lucene.morfologik", "lucene.nori", "lucene.norwegian", "lucene.persian", "lucene.portuguese", "lucene.romanian", "lucene.russian", "lucene.smartcn", "lucene.sorani", "lucene.spanish", "lucene.swedish", "lucene.thai", "lucene.turkish", "lucene.ukrainian"] | None = Field(default=None, alias="searchAnalyzer", description="Method applied to identify words when searching this index.")
    sort: TextSearchIndexDefinitionSort | None = Field(default=None, description="Sort definition for the index. When defined, the index will be pre-sorted on the specified fields, which improves query sort performance for those fields. Supports two formats: simple format with field name and direction, or complex format with additional options. The `order` field is required (1=ascending, -1=descending).The `noData` field is optional and controls how missing values are sorted(default: \"lowest\").")
    stored_source: TextSearchIndexDefinitionStoredSource | None = Field(default=None, alias="storedSource", description="Flag that indicates whether to store all fields (true) on Atlas Search. By default, Atlas doesn't store (false) the fields on Atlas Search.  Alternatively, you can specify an object that only contains the list of fields to store (include) or not store (exclude) on Atlas Search. Note that storing all fields (true) is not allowed for vector search indexes. To learn more, see Stored Source Fields.")
    synonyms: list[SearchSynonymMappingDefinition] | None = Field(default=None, description="Rule sets that map words to their synonyms in this index.")
    type_sets: list[SearchTypeSets] | None = Field(default=None, alias="typeSets", description="Type sets for the index.")
