"""Generated model for AppServiceMetricThreshold. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.data_metric_threshold_view import DataMetricThresholdView
from pyatlassdk.models.raw_metric_threshold_view import RawMetricThresholdView
from pyatlassdk.models.time_metric_threshold_view import TimeMetricThresholdView

AppServiceMetricThreshold: TypeAlias = RawMetricThresholdView | DataMetricThresholdView | TimeMetricThresholdView
