"""Generated model for StreamProcessorMetricThreshold. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.dlq_raw_metric_threshold_view import DLQRawMetricThresholdView
from pyatlassdk.models.kafka_raw_metric_threshold_view import KafkaRawMetricThresholdView
from pyatlassdk.models.raw_metric_threshold_view import RawMetricThresholdView
from pyatlassdk.models.time_metric_threshold_view import TimeMetricThresholdView

StreamProcessorMetricThreshold: TypeAlias = KafkaRawMetricThresholdView | TimeMetricThresholdView | DLQRawMetricThresholdView | RawMetricThresholdView
