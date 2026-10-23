"""Generated model for UsageDetailsFilterRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import date

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UsageDetailsFilterRequest(BaseModel):
    """Request body which contains various fields to filter line items as part of certain Invoice Usage Details queries."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    bill_end_date: date | None = Field(default=None, alias="billEndDate", description="The inclusive billing start date for usage details filter.")
    bill_start_date: date | None = Field(default=None, alias="billStartDate", description="The inclusive billing start date for usage details filter.")
    cluster_ids: list[str] | None = Field(default=None, alias="clusterIds", description="The list of unique cluster ids to be included in the Usage Details filter.")
    group_ids: list[str] | None = Field(default=None, alias="groupIds", description="The list of groups to be included in the Usage Details filter.")
    include_zero_cent_line_items: bool | None = Field(default=None, alias="includeZeroCentLineItems", description="Whether zero cent line items should be included.")
    sku_services: list[Literal["Atlas", "Clusters", "Storage", "Serverless Instances", "Backup", "Data Transfer", "BI Connector", "Premium Features", "Atlas Data Federation", "Atlas Stream Processing", "App Services", "Charts", "Cloud Manager", "Cloud Manager Standard/Premium", "Legacy Backup", "AI Model APIs", "Automated Embedding", "Native Reranking", "Agent Engine", "Flex Consulting", "Support", "Credits"]] | None = Field(default=None, alias="skuServices", description="The list of projects to be included in the Cost Explorer Query.")
    usage_end_date: date | None = Field(default=None, alias="usageEndDate", description="The inclusive billing start date for usage details filter.")
    usage_start_date: date | None = Field(default=None, alias="usageStartDate", description="The inclusive usage start date for usage details filter.")
