"""Generated model for BillingInvoiceMetadata. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class BillingInvoiceMetadata(BaseModel):
    """Generated model for BillingInvoiceMetadata."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    amount_billed_cents: int | None = Field(default=None, alias="amountBilledCents", description="Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    amount_paid_cents: int | None = Field(default=None, alias="amountPaidCents", description="Sum that the specified organization paid toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created this invoice. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    credits_cents: int | None = Field(default=None, alias="creditsCents", description="Sum that MongoDB credited the specified organization toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    end_date: datetime | None = Field(default=None, alias="endDate", description="Date and time when MongoDB Cloud finished the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.")
    linked_invoices: list[BillingInvoiceMetadata] | None = Field(default=None, alias="linkedInvoices", description="List that contains the invoices for organizations linked to the paying organization.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization charged for services consumed from MongoDB Cloud.")
    sales_tax_cents: int | None = Field(default=None, alias="salesTaxCents", description="Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    start_date: datetime | None = Field(default=None, alias="startDate", description="Date and time when MongoDB Cloud began the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    starting_balance_cents: int | None = Field(default=None, alias="startingBalanceCents", description="Sum that the specified organization owed to MongoDB when MongoDB issued this invoice. This parameter expresses its value in US Dollars.")
    status_name: Literal["PENDING", "CLOSED", "FORGIVEN", "FAILED", "PAID", "FREE", "PREPAID", "INVOICED"] | None = Field(default=None, alias="statusName", description="Phase of payment processing in which this invoice exists when you made this request. Accepted phases include:\n\n- `CLOSED`: MongoDB finalized all charges in the billing cycle but has yet to charge the customer.\n- `FAILED`: MongoDB attempted to charge the provided credit card but charge for that amount failed.\n- `FORGIVEN`: Customer initiated payment which MongoDB later forgave.\n- `FREE`: All charges totalled zero so the customer won't be charged.\n- `INVOICED`: MongoDB handled these charges using elastic invoicing.\n- `PAID`: MongoDB succeeded in charging the provided credit card.\n- `PENDING`: Invoice includes charges for the current billing cycle.\n- `PREPAID`: Customer has a pre-paid plan so they won't be charged.")
    subtotal_cents: int | None = Field(default=None, alias="subtotalCents", description="Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    updated: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud last updated the value of this payment. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")

BillingInvoiceMetadata.model_rebuild()
