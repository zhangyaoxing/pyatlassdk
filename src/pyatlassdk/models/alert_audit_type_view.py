"""Generated model for AlertAuditTypeView. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class AlertAuditTypeView(str, Enum):
    """Unique identifier of event type."""
    ALERT_ACKNOWLEDGED_AUDIT = "ALERT_ACKNOWLEDGED_AUDIT"
    ALERT_UNACKNOWLEDGED_AUDIT = "ALERT_UNACKNOWLEDGED_AUDIT"
