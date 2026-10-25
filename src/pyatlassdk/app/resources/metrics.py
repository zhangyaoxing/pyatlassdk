"""Generated resource for Metrics. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Metrics:
    """View Atlas App Services metrics."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_metrics(
        self,
        app_id: str,
        group_id: str,
        *,
        end: str,
        granularity: str,
        metrics: Literal["ACTIVE_OPEN_SYNC_SESSIONS", "AUTH_EGRESS_BYTES", "AUTH_FAILED_REQUESTS", "AUTH_RESPONSE_MS", "AUTH_SUCCESSFUL_LOGIN", "AUTH_SUCCESSFUL_REQUESTS", "AUTH_TOTAL_USERS", "ENDPOINTS_COMPUTE_MS", "ENDPOINTS_EGRESS_BYTES", "ENDPOINTS_FAILED_REQUEST", "ENDPOINTS_RESPONSE_MS", "ENDPOINTS_SUCCESSFUL_REQUESTS", "GRAPHQL_RESPONSE_MS", "GRAPHQL_COMPUTE_MS", "GRAPHQL_EGRESS_BYTES", "GRAPHQL_FAILED_REQUESTS", "GRAPHQL_SUCCESSFUL_REQUESTS", "LF_RESPONSE_MS", "OVERALL_COMPUTE_MS", "OVERALL_EGRESS_BYTES", "OVERALL_FAILED_REQUESTS", "OVERALL_SUCCESSFUL_REQUESTS", "OVERALL_SYNC_MINUTES", "SDK_COMPUTE_MS", "SDK_EGRESS_BYTES", "SDK_FAILED_REQUESTS", "SDK_FNS_RESPONSE_MS", "SDK_MQL_COMPUTE_MS", "SDK_MQL_EGRESS_BYTES", "SDK_MQL_FAILED_REQUESTS", "SDK_MQL_RESPONSE_MS", "SDK_MQL_SUCCESSFUL_REQUESTS", "SDK_SUCCESSFUL_REQUESTS", "SYNC_CLIENT_BOOTSTRAP_MS", "SYNC_CLIENT_UPLOADS_INVALID", "SYNC_CURRENT_OPLOG_LAG_MS_SUM", "SYNC_EGRESS_BYTES", "SYNC_FAILED_REQUESTS", "SYNC_HISTORY_WRITE_MS", "SYNC_MINUTES", "SYNC_NUM_INTEGRATION_ATTEMPTS", "SYNC_NUM_UNSYNCABLE_DOC", "SYNC_OT_MS", "SYNC_SESSIONS_ENDED", "SYNC_SESSIONS_STARTED", "SYNC_SUCCESSFUL_REQUESTS", "SYNC_UPLOAD_PROPS_MS", "TRIGGERS_COMPUTE_MS", "TRIGGERS_CURRENT_OPLOG_LAG_MS_SUM", "TRIGGERS_EGRESS_BYTES", "TRIGGERS_FAILED_REQUESTS", "TRIGGERS_RESPONSE_MS", "TRIGGERS_SUCCESSFUL_REQUESTS"] | None = None,
        start: str,
    ) -> dict[str, Any]:
        """
        Retrieve App Services metrics

        Retrieves a variety of metrics, including: Compute Time, Data Transfer,
        Sync Minutes, Requests Succeeded, Requests Failed. For a complete list
        of available metrics, see [App
        Services Metrics Reference](https://mongodb.com/docs/atlas/app-services/reference/metrics).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            end: The ISO-8601 date and time of the end of the query period (e.g. "2022-12-27T14:01:01Z").
            granularity: Specifies the granularity of the query period as an [ISO-8601 duration value](https://en.wikipedia.org/wiki/ISO_8601#Durations). Examples include "P31D" (31 day), "PT1H" (1 hour), and "PT5M" (5 minutes).
            metrics: The name of the metric to filter by. For detailed information on the available metrics and their units, see [App Services Metrics Reference](https://mongodb.com/docs/atlas/app-services/reference/metrics).
            start: The ISO-8601 date and time of the start of the query period (e.g. "2022-10-27T14:01:01Z").
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/metrics"
        params = {
            "end": end,
            "granularity": granularity,
            "metrics": metrics,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=dict[str, Any],
        )
