"""Generated model for ReplicaSetEventTypeViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class ReplicaSetEventTypeViewForNdsGroup(str, Enum):
    """Unique identifier of event type."""
    PRIMARY_ELECTED = "PRIMARY_ELECTED"
    REPLICATION_OPLOG_WINDOW_HEALTHY = "REPLICATION_OPLOG_WINDOW_HEALTHY"
    REPLICATION_OPLOG_WINDOW_RUNNING_OUT = "REPLICATION_OPLOG_WINDOW_RUNNING_OUT"
    ONE_PRIMARY = "ONE_PRIMARY"
    NO_PRIMARY = "NO_PRIMARY"
    TOO_MANY_ELECTIONS = "TOO_MANY_ELECTIONS"
    TOO_FEW_HEALTHY_MEMBERS = "TOO_FEW_HEALTHY_MEMBERS"
    TOO_MANY_UNHEALTHY_MEMBERS = "TOO_MANY_UNHEALTHY_MEMBERS"
