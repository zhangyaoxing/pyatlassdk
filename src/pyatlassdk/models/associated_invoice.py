"""Generated model for AssociatedInvoice. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AssociatedInvoice(BaseModel):
    """An invoice associated with an organization."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    invoice_id: str | None = Field(default=None, alias="invoiceId", description="Unique 24-hexadecimal digit identifier for an invoice.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit identifier for an organization.")
