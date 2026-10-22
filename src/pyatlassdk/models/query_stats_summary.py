"""Generated model for QueryStatsSummary. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class QueryStatsSummary(BaseModel):
    """A summary of execution statistics for a given query shape."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    avg_time_to_response_micros: float | None = Field(default=None, alias="avgTimeToResponseMicros", description="Average time in microseconds from the beginning of query processing to the first server response, per execution of queries with the given query shape. Calculated as `totalTimeToResponseMicros` divided by `execCount` over the requested time range. As a duration it can be longer or shorter than `avgWorkingMillis` (reported in milliseconds, so convert before comparing): longer when executions spent time blocked on locks or flow control rather than working, shorter when they kept working after the first batch to return later `getMore` batches.")
    avg_working_millis: float | None = Field(default=None, alias="avgWorkingMillis", description="Average active execution time in milliseconds per execution of queries with the given query shape, calculated as `totalWorkingMillis` divided by `execCount` over the requested time range. Excludes intentional pauses such as time waiting on locks or flow control.")
    bytes_read: float | None = Field(default=None, alias="bytesRead", description="The number of bytes read by the given query shape from the disk to the cache.")
    command: Literal["find", "distinct", "aggregate", "count", "insert", "update", "delete"] | None = Field(default=None, description="The MongoDB command issued for this query shape. The insert, update, and delete commands appear only for clusters running MongoDB 9.0 or later.")
    cpu_time: float | None = Field(default=None, alias="cpuTime", description="Total CPU time in nanoseconds consumed by queries with the given query shape. Available for MDB 8.2 and higher.")
    docs_examined: float | None = Field(default=None, alias="docsExamined", description="Total number of documents examined by queries with the given query shape.")
    docs_examined_ratio: float | None = Field(default=None, alias="docsExaminedRatio", description="Ratio of documents examined to documents returned by queries with the given query shape.")
    docs_returned: float | None = Field(default=None, alias="docsReturned", description="Total number of documents returned by queries with the given query shape.")
    exec_count: float | None = Field(default=None, alias="execCount", description="Total number of times that queries with the given query shape have been executed.")
    keys_deleted: float | None = Field(default=None, alias="keysDeleted", description="Total number of index keys deleted by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    keys_examined: float | None = Field(default=None, alias="keysExamined", description="Total number of in-bounds and out-of-bounds index keys examined by queries with the given query shape.")
    keys_examined_ratio: float | None = Field(default=None, alias="keysExaminedRatio", description="Ratio of in-bounds and out-of-bounds index keys examined to indexes containing documents returned by queries with the given query shape.")
    keys_inserted: float | None = Field(default=None, alias="keysInserted", description="Total number of index keys inserted by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    last_exec_micros: float | None = Field(default=None, alias="lastExecMicros", description="Execution runtime in microseconds for the most recent query with the given query shape.")
    n_deleted: float | None = Field(default=None, alias="nDeleted", description="Total number of documents deleted by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    n_inserted: float | None = Field(default=None, alias="nInserted", description="Total number of documents inserted by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    n_matched: float | None = Field(default=None, alias="nMatched", description="Total number of documents matched by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    n_modified: float | None = Field(default=None, alias="nModified", description="Total number of documents modified by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    n_upserted: float | None = Field(default=None, alias="nUpserted", description="Total number of documents upserted by queries with the given query shape. Available for MongoDB 9.0+ write commands.")
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    p50_exec_micros: float | None = Field(default=None, alias="p50ExecMicros", description="The 50th percentile value of execution time in microseconds. This field is deprecated as the values it reports may be inaccurate. It will be removed in a future release.")
    p90_exec_micros: float | None = Field(default=None, alias="p90ExecMicros", description="The 90th percentile value of execution time in microseconds. This field is deprecated as the values it reports may be inaccurate. It will be removed in a future release.")
    p99_exec_micros: float | None = Field(default=None, alias="p99ExecMicros", description="The 99th percentile value of execution time in microseconds. This field is deprecated as the values it reports may be inaccurate. It will be removed in a future release.")
    query_shape: str | None = Field(default=None, alias="queryShape", description="A query shape is a set of specifications that group similar queries together. Specifications can include filters, sorts, projections, aggregation pipeline stages, a namespace, and others. Queries that have similar specifications have the same query shape.")
    query_shape_hash: str | None = Field(default=None, alias="queryShapeHash", description="A hexadecimal string that represents the hash of a MongoDB query shape.")
    system_query: bool | None = Field(default=None, alias="systemQuery", description="Indicates whether this query shape represents a system-initiated query.")
    total_time_to_response_micros: float | None = Field(default=None, alias="totalTimeToResponseMicros", description="Total time in microseconds from the beginning of query processing to the first server response, summed across executions of queries with the given query shape. Includes time spent waiting on locks or flow control. Stops at the first batch of results, so time spent serving later `getMore` batches is not counted.")
    total_working_millis: float | None = Field(default=None, alias="totalWorkingMillis", description="Total time in milliseconds that queries with the given query shape spent actively executing, summed across executions, including time spent processing `getMore` requests. Excludes intentional pauses such as time waiting on locks or flow control, and time spent waiting for the client.")
