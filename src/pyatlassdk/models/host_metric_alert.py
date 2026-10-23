"""Generated model for HostMetricAlert. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.host_metric_event_type_view_alertable import HostMetricEventTypeViewAlertable
from pyatlassdk.models.host_metric_value import HostMetricValue
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostMetricAlert(BaseModel):
    """Host Metric Alert notifies about changes of measurements or metrics for mongod host."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    acknowledged_until: datetime | None = Field(default=None, alias="acknowledgedUntil", description="Date and time until which this alert has been acknowledged. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter if a MongoDB User previously acknowledged this alert.\n\n- To acknowledge this alert forever, set the parameter value to 100 years in the future.\n\n- To unacknowledge a previously acknowledged alert, do not set this parameter value.")
    acknowledgement_comment: str | None = Field(default=None, alias="acknowledgementComment", description="Comment that a MongoDB Cloud user submitted when acknowledging the alert.")
    acknowledging_username: str | None = Field(default=None, alias="acknowledgingUsername", description="MongoDB Cloud username of the person who acknowledged the alert. The response returns this parameter if a MongoDB Cloud user previously acknowledged this alert.")
    alert_config_id: str = Field(alias="alertConfigId", description="Unique 24-hexadecimal digit string that identifies the alert configuration that sets this alert.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster to which this alert applies. This resource returns this parameter for alerts of events impacting backups, replica sets, or sharded clusters.")
    created: datetime = Field(description="Date and time when MongoDB Cloud created this alert. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    current_value: HostMetricValue | None = Field(default=None, alias="currentValue")
    event_type_name: HostMetricEventTypeViewAlertable = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert.")
    hostname_and_port: str | None = Field(default=None, alias="hostnameAndPort", description="Hostname and port of the host to which this alert applies. The resource returns this parameter for alerts of events impacting hosts or replica sets.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies this alert.")
    last_notified: datetime | None = Field(default=None, alias="lastNotified", description="Date and time that any notifications were last sent for this alert. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter if MongoDB Cloud has sent notifications for this alert.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    metric_name: str | None = Field(default=None, alias="metricName", description="Name of the metric against which Atlas checks the configured `metricThreshold.threshold`.\n\nTo learn more about the available metrics, see <a href=\"https://www.mongodb.com/docs/atlas/reference/alert-host-metrics/#std-label-measurement-types\" target=\"_blank\">Host Metrics</a>.\n\n**NOTE**: If you set `eventTypeName` to `OUTSIDE_SERVERLESS_METRIC_THRESHOLD`, you can specify only metrics available for serverless. To learn more, see <a href=\"https://dochub.mongodb.org/core/alert-config-serverless-measurements\" target=\"_blank\">Serverless Measurements</a>.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal character string that identifies the organization that owns the project to which this alert applies.")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Name of the replica set to which this alert applies. The response returns this parameter for alerts of events impacting backups, hosts, or replica sets.")
    resolved: datetime | None = Field(default=None, description="Date and time that this alert changed to `\"status\" : \"CLOSED\"`. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter once `\"status\" : \"CLOSED\"`.")
    severity: Annotated[Literal["INFO", "WARNING", "ERROR", "CRITICAL"], BeforeValidator(upper_case)] | None = Field(default=None, description="Severity of the event.")
    status: Annotated[Literal["CANCELLED", "CLOSED", "OPEN", "TRACKING"], BeforeValidator(upper_case)] = Field(description="State of this alert at the time you requested its details. TRACKING indicates the alert condition exists but has not persisted for the minimum notification delay. OPEN indicates the alert condition currently exists. CLOSED indicates the alert condition has been resolved.")
    updated: datetime = Field(description="Date and time when someone last updated this alert. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
