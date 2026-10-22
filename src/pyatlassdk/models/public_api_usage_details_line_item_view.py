"""Generated model for PublicApiUsageDetailsLineItemView. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.additional_data import AdditionalData

from pydantic import BaseModel, ConfigDict, Field

class PublicApiUsageDetailsLineItemView(BaseModel):
    """Generated model for PublicApiUsageDetailsLineItemView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    additional_data: AdditionalData | None = Field(default=None, alias="additionalData")
    bill_date: datetime | None = Field(default=None, alias="billDate", description="Billing date of the line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    cloud_provider: Literal["AWS", "GCP", "AZURE", "ATLAS"] | None = Field(default=None, alias="cloudProvider", description="Code identifying the cloud provider this line item's usage is attributed to. Values map as follows: AWS is Amazon Web Services, GCP is Google Cloud, AZURE is Microsoft Azure, and ATLAS is other Atlas usage not tied to a specific cloud provider.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Cluster associated with the line item.")
    description: str | None = Field(default=None, description="Description of the line item, which can include SKU name and other identifying information.")
    group_id: str | None = Field(default=None, alias="groupId", description="Group id associated with the line item.")
    quantity: float | None = Field(default=None, description="Quantity of line item in units associated with SKU.")
    total_price_cents: int | None = Field(default=None, alias="totalPriceCents", description="Price * quantity in applicable units, expressed as an integral number of cents.")
    unit_price_dollars: float | None = Field(default=None, alias="unitPriceDollars", description="Price in units associated with the SKU for the line item.")
    usage_date: datetime | None = Field(default=None, alias="usageDate", description="Usage date of the line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
