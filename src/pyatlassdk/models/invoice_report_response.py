"""Generated model for InvoiceReportResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class InvoiceReportResponse(BaseModel):
    """Status and details of a previously requested invoice report."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    download_url: str | None = Field(default=None, alias="downloadUrl", description="URL to download the report. Present only when the report has succeeded.")
    expires_at: datetime | None = Field(default=None, alias="expiresAt", description="Time at which the download URL expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Present only when the report has succeeded.")
    failure_reason: str | None = Field(default=None, alias="failureReason", description="Reason the report failed. Present only when the report has failed.")
    format_spec_version: str | None = Field(default=None, alias="formatSpecVersion", description="Version of the report format specification.")
    invoice_id: str = Field(alias="invoiceId", description="Unique 24-hexadecimal digit string that identifies the invoice.")
    report_format: Annotated[Literal["CSV"], BeforeValidator(upper_case)] = Field(alias="reportFormat", description="Format of the generated report.")
    report_id: str = Field(alias="reportId", description="Unique 24-hexadecimal digit string that identifies the report.")
    report_type: Annotated[Literal["FOCUS"], BeforeValidator(upper_case)] = Field(alias="reportType", description="Type of the generated report.")
    state: Annotated[Literal["PENDING", "RUNNING", "SUCCEEDED", "FAILED"], BeforeValidator(upper_case)] = Field(description="Current state of the report generation.")
