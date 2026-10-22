"""Generated model for StreamProcessorEventTypeViewAlertableNoThreshold. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class StreamProcessorEventTypeViewAlertableNoThreshold(str, Enum):
    """Event type that triggers an alert."""
    STREAM_PROCESSOR_STATE_IS_FAILED = "STREAM_PROCESSOR_STATE_IS_FAILED"
    STREAM_PROCESSOR_AUTOSCALE_INITIATED = "STREAM_PROCESSOR_AUTOSCALE_INITIATED"
