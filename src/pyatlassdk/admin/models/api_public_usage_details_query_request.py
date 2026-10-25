"""Generated model for ApiPublicUsageDetailsQueryRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.usage_details_filter_request import UsageDetailsFilterRequest

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiPublicUsageDetailsQueryRequest(BaseModel):
    """Request body for an Invoice Usage Details query with filtering, pagination, and sort."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    filters: UsageDetailsFilterRequest | None = None
    sort_field: Annotated[Literal["USAGE_DATES", "BILL_DATES", "TOTAL_PRICE_CENTS"], BeforeValidator(upper_case)] | None = Field(default=None, alias="sortField", description="Specify the field used to specify how to sort query results. Default to bill date.")
    sort_order: Annotated[Literal["ASCENDING", "DESCENDING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="sortOrder", description="Specify the sort order (ascending / descending) used to specify how to sort query results. Defaults to descending.")
