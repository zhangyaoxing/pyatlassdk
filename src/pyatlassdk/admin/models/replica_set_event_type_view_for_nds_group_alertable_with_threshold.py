"""Generated model for ReplicaSetEventTypeViewForNdsGroupAlertableWithThreshold. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class ReplicaSetEventTypeViewForNdsGroupAlertableWithThreshold(CaseInsensitiveEnum):
    """Event type that triggers an alert."""
    TOO_MANY_ELECTIONS = "TOO_MANY_ELECTIONS"
    REPLICATION_OPLOG_WINDOW_RUNNING_OUT = "REPLICATION_OPLOG_WINDOW_RUNNING_OUT"
    TOO_FEW_HEALTHY_MEMBERS = "TOO_FEW_HEALTHY_MEMBERS"
    TOO_MANY_UNHEALTHY_MEMBERS = "TOO_MANY_UNHEALTHY_MEMBERS"
