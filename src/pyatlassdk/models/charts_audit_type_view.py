"""Generated model for ChartsAuditTypeView. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class ChartsAuditTypeView(str, Enum):
    """Unique identifier of event type."""
    CHARTS_API_SUCCESS = "CHARTS_API_SUCCESS"
    CHARTS_API_FAILURE = "CHARTS_API_FAILURE"
    CHARTS_DASHBOARD_EXPORTED = "CHARTS_DASHBOARD_EXPORTED"
    CHARTS_DASHBOARD_EXPORT_FAILED = "CHARTS_DASHBOARD_EXPORT_FAILED"
    CHARTS_DASHBOARD_IMPORTED = "CHARTS_DASHBOARD_IMPORTED"
    CHARTS_DASHBOARD_IMPORT_FAILED = "CHARTS_DASHBOARD_IMPORT_FAILED"
