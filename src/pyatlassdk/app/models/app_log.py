"""Generated model for AppLog. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.logs_api import LogsAPI
from pyatlassdk.app.models.logs_api_key import LogsAPIKey
from pyatlassdk.app.models.logs_auth import LogsAuth
from pyatlassdk.app.models.logs_auth_event_trigger import LogsAuthEventTrigger
from pyatlassdk.app.models.logs_db_event_trigger import LogsDBEventTrigger
from pyatlassdk.app.models.logs_endpoint import LogsEndpoint
from pyatlassdk.app.models.logs_function import LogsFunction
from pyatlassdk.app.models.logs_graph_ql import LogsGraphQL
from pyatlassdk.app.models.logs_incoming_webhook import LogsIncomingWebhook
from pyatlassdk.app.models.logs_log_forwarder import LogsLogForwarder
from pyatlassdk.app.models.logs_push import LogsPush
from pyatlassdk.app.models.logs_scheduled_event_trigger import LogsScheduledEventTrigger
from pyatlassdk.app.models.logs_schema_additive_change import LogsSchemaAdditiveChange
from pyatlassdk.app.models.logs_schema_generation import LogsSchemaGeneration
from pyatlassdk.app.models.logs_schema_validation import LogsSchemaValidation
from pyatlassdk.app.models.logs_service_function import LogsServiceFunction
from pyatlassdk.app.models.logs_service_stream_function import LogsServiceStreamFunction
from pyatlassdk.app.models.logs_stream_function import LogsStreamFunction
from pyatlassdk.app.models.logs_sync_client_write import LogsSyncClientWrite
from pyatlassdk.app.models.logs_sync_connection_end import LogsSyncConnectionEnd
from pyatlassdk.app.models.logs_sync_connection_start import LogsSyncConnectionStart
from pyatlassdk.app.models.logs_sync_error import LogsSyncError
from pyatlassdk.app.models.logs_sync_other import LogsSyncOther
from pyatlassdk.app.models.logs_sync_session_end import LogsSyncSessionEnd
from pyatlassdk.app.models.logs_sync_session_start import LogsSyncSessionStart
from pyatlassdk.app.models.logs_trigger_error_handler import LogsTriggerErrorHandler
from pyatlassdk.app.models.logs_trigger_failure import LogsTriggerFailure

AppLog: TypeAlias = LogsAPI | LogsAPIKey | LogsTriggerFailure | LogsTriggerErrorHandler | LogsDBEventTrigger | LogsAuthEventTrigger | LogsScheduledEventTrigger | LogsFunction | LogsServiceFunction | LogsStreamFunction | LogsServiceStreamFunction | LogsAuth | LogsIncomingWebhook | LogsEndpoint | LogsPush | LogsGraphQL | LogsSyncConnectionStart | LogsSyncConnectionEnd | LogsSyncSessionStart | LogsSyncSessionEnd | LogsSyncClientWrite | LogsSyncError | LogsSyncOther | LogsSchemaAdditiveChange | LogsSchemaGeneration | LogsSchemaValidation | LogsLogForwarder
