"""Generated model for PerformanceAdvisorSlowQueryMetrics. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class PerformanceAdvisorSlowQueryMetrics(BaseModel):
    """Metrics from a slow query log."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    docs_examined: int | None = Field(default=None, alias="docsExamined", description="The number of documents in the collection that MongoDB scanned in order to carry out the operation.")
    docs_examined_returned_ratio: float | None = Field(default=None, alias="docsExaminedReturnedRatio", description="Ratio of documents examined to documents returned.")
    docs_returned: int | None = Field(default=None, alias="docsReturned", description="The number of documents returned by the operation.")
    from_user_connection: bool | None = Field(default=None, alias="fromUserConnection", description="This boolean will be true when the server can identify the query source as non-server. This field is only available for MDB 8.0+.")
    has_auto_embedding: bool | None = Field(default=None, alias="hasAutoEmbedding", description="Flag that indicates whether the slow query used automated embedding, where MongoDB Cloud generates embeddings from raw text at query time instead of the client supplying a precomputed vector.")
    has_index_coverage: bool | None = Field(default=None, alias="hasIndexCoverage", description="Indicates if the query has index coverage.")
    has_rerank: bool | None = Field(default=None, alias="hasRerank", description="Flag that indicates whether the slow query used the `$rerank` aggregation stage, which reorders results using Voyage AI reranking models. Always `false` for MongoDB deployments earlier than 8.3.")
    has_sort: bool | None = Field(default=None, alias="hasSort", description="This boolean will be true when a query cannot use the ordering in the index to return the requested sorted results; i.e. MongoDB must sort the documents after it receives the documents from a cursor.")
    keys_examined: int | None = Field(default=None, alias="keysExamined", description="The number of index keys that MongoDB scanned in order to carry out the operation.")
    keys_examined_returned_ratio: float | None = Field(default=None, alias="keysExaminedReturnedRatio", description="Ratio of keys examined to documents returned.")
    num_yields: int | None = Field(default=None, alias="numYields", description="The number of times the operation yielded to allow other operations to complete.")
    operation_execution_time: int | None = Field(default=None, alias="operationExecutionTime", description="Total execution time of a query in milliseconds.")
    response_length: int | None = Field(default=None, alias="responseLength", description="The length in bytes of the operation's result document.")
    tokens_used: int | None = Field(default=None, alias="tokensUsed", description="The total inference tokens consumed by this operation, including tokens used by `$rerank`. Returned only for inference queries that consumed tokens; it is omitted otherwise, including for MongoDB deployments earlier than 8.3.")
