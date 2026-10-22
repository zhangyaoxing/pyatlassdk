"""Generated model for CpsBackupEventTypeViewForNdsGroupAlertableWithThreshold. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class CpsBackupEventTypeViewForNdsGroupAlertableWithThreshold(str, Enum):
    """Event type that triggers an alert."""
    CPS_SNAPSHOT_BEHIND = "CPS_SNAPSHOT_BEHIND"
    CPS_PREV_SNAPSHOT_OLD = "CPS_PREV_SNAPSHOT_OLD"
    CPS_OPLOG_BEHIND = "CPS_OPLOG_BEHIND"
