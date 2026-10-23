"""Generated model for OrgAssociatedInvoiceResponse. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.associated_invoice import AssociatedInvoice

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgAssociatedInvoiceResponse(BaseModel):
    """Response containing associated invoices for an organization."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    associated_invoices: list[AssociatedInvoice] | None = Field(default=None, alias="associatedInvoices", description="List of invoices associated with the organization for the specified period.")
    month: str | None = Field(default=None, description="Two-digit number that represents the month of the associated invoices.")
    year: str | None = Field(default=None, description="Four-digit number that represents the year of the associated invoices.")
