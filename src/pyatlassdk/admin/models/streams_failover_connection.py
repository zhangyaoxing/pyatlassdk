"""Generated model for StreamsFailoverConnection. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.streams_failover_cluster_connection import StreamsFailoverClusterConnection
from pyatlassdk.admin.models.streams_failover_kafka_connection import StreamsFailoverKafkaConnection

StreamsFailoverConnection: TypeAlias = StreamsFailoverClusterConnection | StreamsFailoverKafkaConnection
