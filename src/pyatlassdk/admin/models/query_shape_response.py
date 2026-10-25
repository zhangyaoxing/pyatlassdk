"""Generated model for QueryShapeResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class QueryShapeResponse(BaseModel):
    """Response containing the details and status of a query shape. The query shape field may be null if the user lacks PII view access."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    command: Annotated[Literal["FIND", "DISTINCT", "AGGREGATE", "COUNT", "INSERT", "UPDATE", "DELETE"], BeforeValidator(upper_case)] | None = Field(default=None, description="The MongoDB command type issued for a query shape. The INSERT, UPDATE, and DELETE commands appear only for clusters running MongoDB 9.0 or later.")
    namespace: str | None = Field(default=None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    query_shape: str | None = Field(default=None, alias="queryShape", description="A query shape is a set of specifications that group similar queries together. Specifications can include filters, sorts, projections, aggregation pipeline stages, a namespace, and others. Queries that have similar specifications have the same query shape. This field may be null if the user lacks PII view access.")
    query_shape_hash: str = Field(alias="queryShapeHash", description="A hexadecimal string that represents the hash of a MongoDB query shape.")
    status: Annotated[Literal["REJECTED", "UNREJECTED"], BeforeValidator(upper_case)] = Field(description="The rejection status of a query shape. Use REJECTED to prevent the query shape from executing on the cluster, or UNREJECTED to allow it to execute.")
