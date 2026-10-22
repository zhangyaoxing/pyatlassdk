"""Generated model for EventSeverity. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class EventSeverity(str, Enum):
    """Severity of the event."""
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
