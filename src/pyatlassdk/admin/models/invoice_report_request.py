"""Generated model for InvoiceReportRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class InvoiceReportRequest(BaseModel):
    """Generated model for InvoiceReportRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    format_spec_version: str | None = Field(default=None, alias="formatSpecVersion", description="Version of the report format specification.")
    report_format: Annotated[Literal["CSV"], BeforeValidator(upper_case)] = Field(alias="reportFormat", description="Format of the report.")
    report_type: Annotated[Literal["FOCUS"], BeforeValidator(upper_case)] = Field(alias="reportType", description="Type of report to generate.")
