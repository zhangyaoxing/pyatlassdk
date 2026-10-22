"""Generated model for HostMetricEvent. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.host_metric_event_type_view import HostMetricEventTypeView
from pyatlassdk.models.host_metric_value import HostMetricValue
from pyatlassdk.models.link import Link
from pyatlassdk.models.principal import Principal
from pyatlassdk.models.raw import Raw

from pydantic import BaseModel, ConfigDict, Field

class HostMetricEvent(BaseModel):
    """Host Metric Event reflects different measurements and metrics about mongod host."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key_id: str | None = Field(default=None, alias="apiKeyId", description="Unique 24-hexadecimal digit string that identifies the API Key that triggered the event. If this resource returns this parameter, it doesn't return the `userId` parameter.")
    created: datetime = Field(description="Date and time when this event occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    current_value: HostMetricValue | None = Field(default=None, alias="currentValue")
    delegate_principal: Principal | None = Field(default=None, alias="delegatePrincipal")
    desk_location: str | None = Field(default=None, alias="deskLocation", description="Desk location of MongoDB employee associated with the event.")
    employee_identifier: str | None = Field(default=None, alias="employeeIdentifier", description="Identifier of MongoDB employee associated with the event.")
    event_type_name: HostMetricEventTypeView = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The `eventId` identifies the specific event.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the event.")
    is_global_admin: bool | None = Field(default=None, alias="isGlobalAdmin", description="Flag that indicates whether a MongoDB employee triggered the specified event.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    metric_name: str | None = Field(default=None, alias="metricName", description="Human-readable label of the metric associated with the `alertId`. This field may change type of `currentValue` field.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    port: int | None = Field(default=None, description="IANA port on which the MongoDB process listens for requests.")
    public_key: str | None = Field(default=None, alias="publicKey", description="Public part of the API key that triggered the event. If this resource returns this parameter, it doesn't return the **username** parameter.")
    raw: Raw | None = None
    remote_address: str | None = Field(default=None, alias="remoteAddress", description="IPv4 or IPv6 address from which the user triggered this event.")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Human-readable label of the replica set associated with the event.")
    shard_name: str | None = Field(default=None, alias="shardName", description="Human-readable label of the shard associated with the event.")
    user_id: str | None = Field(default=None, alias="userId", description="Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn't return the `apiKeyId` parameter.")
    username: str | None = Field(default=None, description="Email address for the user who triggered this event. If this resource returns this parameter, it doesn't return the `publicApiKey` parameter.")
