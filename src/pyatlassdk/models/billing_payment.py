"""Generated model for BillingPayment. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class BillingPayment(BaseModel):
    """Funds transferred to MongoDB to cover the specified service in this invoice."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    amount_billed_cents: int | None = Field(default=None, alias="amountBilledCents", description="Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    amount_paid_cents: int | None = Field(default=None, alias="amountPaidCents", description="Sum that the specified organization paid toward the associated invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    created: datetime | None = Field(default=None, description="Date and time when the customer made this payment attempt. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    currency: str | None = Field(default=None, description="The currency in which payment was paid. This parameter expresses its value in 3-letter ISO 4217 currency code.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this payment toward the associated invoice.")
    sales_tax_cents: int | None = Field(default=None, alias="salesTaxCents", description="Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    status_name: Literal["NEW", "FORGIVEN", "FAILED", "PAID", "PARTIAL_PAID", "CANCELLED", "INVOICED", "FAILED_AUTHENTICATION", "PROCESSING", "PENDING_REVERSAL", "REFUNDED"] | None = Field(default=None, alias="statusName", description="Phase of payment processing for the associated invoice when you made this request. These phases include:\n\n- `CANCELLED`: Customer or MongoDB cancelled the payment.\n- `ERROR`: Issue arose when attempting to complete payment.\n- `FAILED`: MongoDB tried to charge the credit card without success.\n- `FAILED_AUTHENTICATION`: Strong Customer Authentication has failed. Confirm that your payment method is authenticated.\n- `FORGIVEN`: Customer initiated payment which MongoDB later forgave.\n- `INVOICED`: MongoDB issued an invoice that included this line item.\n- `NEW`: Customer provided a method of payment, but MongoDB hasn't tried to charge the credit card.\n- `PAID`: Customer submitted a successful payment.\n- `PARTIAL_PAID`: Customer paid for part of this line item.")
    subtotal_cents: int | None = Field(default=None, alias="subtotalCents", description="Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    unit_price: str | None = Field(default=None, alias="unitPrice", description="The unit price applied to `amountBilledCents` to compute total payment amount. This value is represented as a decimal string.")
    updated: datetime | None = Field(default=None, description="Date and time when the customer made an update to this payment attempt. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
