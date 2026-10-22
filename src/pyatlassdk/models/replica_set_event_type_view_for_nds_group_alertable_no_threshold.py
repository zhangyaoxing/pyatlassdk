"""Generated model for ReplicaSetEventTypeViewForNdsGroupAlertableNoThreshold. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class ReplicaSetEventTypeViewForNdsGroupAlertableNoThreshold(str, Enum):
    """Event type that triggers an alert."""
    NO_PRIMARY = "NO_PRIMARY"
    PRIMARY_ELECTED = "PRIMARY_ELECTED"
