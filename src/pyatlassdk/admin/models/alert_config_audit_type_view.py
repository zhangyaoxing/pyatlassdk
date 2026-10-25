"""Generated model for AlertConfigAuditTypeView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class AlertConfigAuditTypeView(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    ALERT_CONFIG_DISABLED_AUDIT = "ALERT_CONFIG_DISABLED_AUDIT"
    ALERT_CONFIG_ENABLED_AUDIT = "ALERT_CONFIG_ENABLED_AUDIT"
    ALERT_CONFIG_ADDED_AUDIT = "ALERT_CONFIG_ADDED_AUDIT"
    ALERT_CONFIG_DELETED_AUDIT = "ALERT_CONFIG_DELETED_AUDIT"
    ALERT_CONFIG_CHANGED_AUDIT = "ALERT_CONFIG_CHANGED_AUDIT"
