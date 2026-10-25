"""Generated model for ReplicaSetEventTypeViewForNdsGroupAlertable. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class ReplicaSetEventTypeViewForNdsGroupAlertable(CaseInsensitiveEnum):
    """Incident that triggered this alert."""
    REPLICATION_OPLOG_WINDOW_RUNNING_OUT = "REPLICATION_OPLOG_WINDOW_RUNNING_OUT"
    NO_PRIMARY = "NO_PRIMARY"
    PRIMARY_ELECTED = "PRIMARY_ELECTED"
    TOO_MANY_ELECTIONS = "TOO_MANY_ELECTIONS"
    TOO_FEW_HEALTHY_MEMBERS = "TOO_FEW_HEALTHY_MEMBERS"
    TOO_MANY_UNHEALTHY_MEMBERS = "TOO_MANY_UNHEALTHY_MEMBERS"
