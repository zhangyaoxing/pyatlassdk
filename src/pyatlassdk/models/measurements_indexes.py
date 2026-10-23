"""Generated model for MeasurementsIndexes. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link
from pyatlassdk.models.metrics_measurement import MetricsMeasurement

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MeasurementsIndexes(BaseModel):
    """Generated model for MeasurementsIndexes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_name: str | None = Field(default=None, alias="collectionName", description="Human-readable label that identifies the collection.")
    database_name: str | None = Field(default=None, alias="databaseName", description="Human-readable label that identifies the database that the specified MongoDB process serves.")
    end: datetime | None = Field(default=None, description="Date and time that specifies when to stop retrieving measurements. If you set **end**, you must set **start**. You can't set this parameter and **period** in the same request. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    granularity: Annotated[Literal["PT1M", "PT5M", "PT1H", "P1D"], BeforeValidator(upper_case)] | None = Field(default=None, description="Duration that specifies the interval between measurement data points. The parameter expresses its value in ISO 8601 timestamp format in UTC. If you set this parameter, you must set either **period** or **start** and **end**.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project. The project contains MongoDB processes that you want to return. The MongoDB process can be either the `mongod` or `mongos`.")
    index_ids: list[str] | None = Field(default=None, alias="indexIds", description="List that contains the Atlas Search index identifiers.")
    index_stats_measurements: list[MetricsMeasurement] | None = Field(default=None, alias="indexStatsMeasurements", description="List that contains the Atlas Search index stats measurements.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    process_id: str | None = Field(default=None, alias="processId", description="Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.")
    start: datetime | None = Field(default=None, description="Date and time that specifies when to start retrieving measurements. If you set **start**, you must set **end**. You can't set this parameter and **period** in the same request. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
