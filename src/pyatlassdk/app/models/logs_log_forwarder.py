"""Generated model for LogsLogForwarder. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from pyatlassdk.app._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsLogForwarder(BaseModel):
    """Common fields shared by all log types."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="A unique ID for the log entry.\n")
    co_id: str | None = Field(default=None, description="A correlation ID for the request that issued the logged\noperation.\n")
    domain_id: str | None = Field(default=None, description="The domain ID.\n")
    app_id: str | None = Field(default=None, description="The App's internal client ID value.\n")
    group_id: str | None = Field(default=None, description="The App's Atlas Project ID value.\n")
    request_url: str | None = Field(default=None, description="The URL that the incoming request was sent to.\n")
    request_method: str | None = Field(default=None, description="The HTTP method used by the incoming request.\n")
    started: str | None = Field(default=None, description="An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp for the start of the logged operation.\n")
    completed: str | None = Field(default=None, description="An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp for the completion of the logged operation.\n")
    function_call_location: str | None = Field(default=None, description="The global region where the function was executed.\n")
    function_call_provider_region: str | None = Field(default=None, description="The cloud provider deployment region where the function was\nexecuted.\n")
    function_call: dict[str, Any] | None = None
    function_id: str | None = None
    function_name: str | None = None
    messages: list[str] | None = Field(default=None, description="A list of logs or other messages associated with the operation.\n")
    mem_time_usage: float | None = Field(default=None, description="The total billable memory used by the request.\n")
    type: Annotated[Literal["LOG_FORWARDER"], BeforeValidator(upper_case)] | None = None
    event_subscription_id: str | None = Field(default=None, description="The underlying log event subscription's unique objectId hex.\n")
    event_subscription_name: str | None = Field(default=None, description="The underlying log event subscription's name.\n")
    log_forwarder_id: str | None = Field(default=None, description="The log forwarder's unique objectId hex.\n")
    log_forwarder_name: str | None = Field(default=None, description="The log forwarder's name.\n")
    failed_to_forward_log_ids: list[str] | None = Field(default=None, description="An array of log ``_id`` values for any logs that were not successfully forwarded.\n")
    data_source_id: str | None = Field(default=None, description="The ID of the forwarded log data source.\n")
    data_source_name: str | None = Field(default=None, description="The name of the forwarded log data source.\n")
    data_source_namespace: str | None = Field(default=None, description="The `database.collection` namespace of the forwarded log collection.\n")
