"""Generated model for DataMetricUnits. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class DataMetricUnits(str, Enum):
    """Element used to express the quantity. This can be an element of time, storage capacity, and the like."""
    BITS = "BITS"
    KILOBITS = "KILOBITS"
    MEGABITS = "MEGABITS"
    GIGABITS = "GIGABITS"
    BYTES = "BYTES"
    KILOBYTES = "KILOBYTES"
    MEGABYTES = "MEGABYTES"
    GIGABYTES = "GIGABYTES"
    TERABYTES = "TERABYTES"
    PETABYTES = "PETABYTES"
