"""Generated model for ApiPublicUsageDetailsQueryRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.usage_details_filter_request import UsageDetailsFilterRequest

from pydantic import BaseModel, ConfigDict, Field

class ApiPublicUsageDetailsQueryRequest(BaseModel):
    """Request body for an Invoice Usage Details query with filtering, pagination, and sort."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    filters: UsageDetailsFilterRequest | None = None
    sort_field: Literal["USAGE_DATES", "BILL_DATES", "TOTAL_PRICE_CENTS"] | None = Field(default=None, alias="sortField", description="Specify the field used to specify how to sort query results. Default to bill date.")
    sort_order: Literal["ASCENDING", "DESCENDING"] | None = Field(default=None, alias="sortOrder", description="Specify the sort order (ascending / descending) used to specify how to sort query results. Defaults to descending.")
