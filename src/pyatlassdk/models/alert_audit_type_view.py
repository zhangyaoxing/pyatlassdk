"""Generated model for AlertAuditTypeView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class AlertAuditTypeView(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    ALERT_ACKNOWLEDGED_AUDIT = "ALERT_ACKNOWLEDGED_AUDIT"
    ALERT_UNACKNOWLEDGED_AUDIT = "ALERT_UNACKNOWLEDGED_AUDIT"
