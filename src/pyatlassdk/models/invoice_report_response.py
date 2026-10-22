"""Generated model for InvoiceReportResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class InvoiceReportResponse(BaseModel):
    """Status and details of a previously requested invoice report."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    download_url: str | None = Field(default=None, alias="downloadUrl", description="URL to download the report. Present only when the report has succeeded.")
    expires_at: datetime | None = Field(default=None, alias="expiresAt", description="Time at which the download URL expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Present only when the report has succeeded.")
    failure_reason: str | None = Field(default=None, alias="failureReason", description="Reason the report failed. Present only when the report has failed.")
    format_spec_version: str | None = Field(default=None, alias="formatSpecVersion", description="Version of the report format specification.")
    invoice_id: str = Field(alias="invoiceId", description="Unique 24-hexadecimal digit string that identifies the invoice.")
    report_format: Literal["CSV"] = Field(alias="reportFormat", description="Format of the generated report.")
    report_id: str = Field(alias="reportId", description="Unique 24-hexadecimal digit string that identifies the report.")
    report_type: Literal["FOCUS"] = Field(alias="reportType", description="Type of the generated report.")
    state: Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED"] = Field(description="Current state of the report generation.")
