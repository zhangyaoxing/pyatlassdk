"""Generated model for InvoiceLineItem. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.invoice_line_item_tags import InvoiceLineItemTags

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class InvoiceLineItem(BaseModel):
    """One service included in this invoice."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "GCP", "AZURE", "ATLAS"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Code identifying the cloud provider this line item's usage is attributed to. Values map as follows: AWS is Amazon Web Services, GCP is Google Cloud, AZURE is Microsoft Azure, and ATLAS is other Atlas usage not tied to a specific cloud provider.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster that incurred the charge.")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    discount_cents: int | None = Field(default=None, alias="discountCents", description="Sum by which MongoDB discounted this line item. MongoDB Cloud expresses this value in cents (100ths of one US Dollar). The resource returns this parameter when a discount applies.")
    end_date: datetime | None = Field(default=None, alias="endDate", description="Date and time when when MongoDB Cloud finished charging for this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project associated to this line item.")
    group_name: str | None = Field(default=None, alias="groupName", description="Human-readable label that identifies the project.")
    note: str | None = Field(default=None, description="Comment that applies to this line item.")
    percent_discount: float | None = Field(default=None, alias="percentDiscount", description="Percentage by which MongoDB discounted this line item. The resource returns this parameter when a discount applies.")
    quantity: float | None = Field(default=None, description="Number of units included for the line item. These can be expressions of storage (GB), time (hours), or other units.")
    sku: str | None = Field(default=None, description="Human-readable description of the service that this line item provided. This Stock Keeping Unit (SKU) could be the instance type, a support charge, advanced security, or another service.")
    start_date: datetime | None = Field(default=None, alias="startDate", description="Date and time when MongoDB Cloud began charging for this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    stitch_app_name: str | None = Field(default=None, alias="stitchAppName", description="Human-readable label that identifies the Atlas App Services application associated with this line item.")
    tags: InvoiceLineItemTags | None = Field(default=None, description="A map of key-value pairs corresponding to the tags associated with the line item resource.")
    tier_lower_bound: float | None = Field(default=None, alias="tierLowerBound", description="Lower bound for usage amount range in current SKU tier. \n\n**NOTE**: `lineItems[n].tierLowerBound` appears only if your `lineItems[n].sku` is tiered.")
    tier_upper_bound: float | None = Field(default=None, alias="tierUpperBound", description="Upper bound for usage amount range in current SKU tier. \n\n**NOTE**: `lineItems[n].tierUpperBound` appears only if your `lineItems[n].sku` is tiered.")
    total_price_cents: int | None = Field(default=None, alias="totalPriceCents", description="Sum of the cost set for this line item. MongoDB Cloud expresses this value in cents (100ths of one US Dollar) and calculates this value as `unitPriceDollars` * `quantity` * 100.")
    unit: str | None = Field(default=None, description="Element used to express what **quantity** this line item measures. This value can be elements of time, storage capacity, and the like.")
    unit_price_dollars: float | None = Field(default=None, alias="unitPriceDollars", description="Value per **unit** for this line item expressed in US Dollars.")
