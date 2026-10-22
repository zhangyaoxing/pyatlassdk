"""Generated model for DataFederationTenantQueryLimit. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class DataFederationTenantQueryLimit(BaseModel):
    """Details of a tenant-level query limit for Data Federation. Query limit is the limit on the amount of usage during a time period based on cost."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    current_usage: int | None = Field(default=None, alias="currentUsage", description="Amount that indicates the current usage of the limit.")
    default_limit: int | None = Field(default=None, alias="defaultLimit", description="Default value of the limit.")
    last_modified_date: datetime | None = Field(default=None, alias="lastModifiedDate", description="Only used for Data Federation limits. Timestamp that indicates when this usage limit was last modified. This field uses the ISO 8601 timestamp format in UTC.")
    maximum_limit: int | None = Field(default=None, alias="maximumLimit", description="Maximum value of the limit.")
    name: str = Field(description="Human-readable label that identifies the user-managed limit to modify.")
    overrun_policy: Literal["BLOCK", "BLOCK_AND_KILL"] | None = Field(default=None, alias="overrunPolicy", description="Only used for Data Federation limits. Action to take when the usage limit is exceeded. If limit span is set to QUERY, this is ignored because MongoDB Cloud stops the query when it exceeds the usage limit.")
    tenant_name: str | None = Field(default=None, alias="tenantName", description="Human-readable label that identifies the Federated Database Instance. If specified, the usage limit is for the specified federated database instance only. If omitted, the usage limit is for all federated database instances in the project.")
    value: int = Field(description="Amount to set the limit to.")
