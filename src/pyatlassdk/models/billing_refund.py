"""Generated model for BillingRefund. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class BillingRefund(BaseModel):
    """One payment that MongoDB returned to the organization for this invoice."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    amount_cents: int | None = Field(default=None, alias="amountCents", description="Sum of the funds returned to the specified organization expressed in cents (100th of US Dollar).")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created this refund. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    payment_id: str | None = Field(default=None, alias="paymentId", description="Unique 24-hexadecimal digit string that identifies the payment that the organization had made.")
    reason: str | None = Field(default=None, description="Justification that MongoDB accepted to return funds to the organization.")
