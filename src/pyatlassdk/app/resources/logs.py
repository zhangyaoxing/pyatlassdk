"""Generated resource for Logs. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Logs:
    """
    Access your application's [logs](https://www.mongodb.com/docs/atlas/app-services/logs/).

    ## Pagination with the Logging API

    The Logging endpoint returns up to 100 log entries per page. If the
    query matches more than 100 entries, the result will be
    [paginated](https://en.wikipedia.org/wiki/Pagination). Such a result
    will contain two pieces of information that you will need to request the
    next page of entries for the same query: the `nextEndDate` and
    `nextSkip` fields.

    Paginated results always contain the `nextEndDate` field. A paginated
    result will also contain the `nextSkip` field if the timestamp of the
    first entry on the next page is identical to the timestamp of the last
    entry on the current page.

    To request the first page of up to 100 log entries, use the endpoint as
    usual:

    ```sh
    curl --request GET \\
      --header 'Authorization: Bearer <access_token>' \\
      'https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/logs'
    ```

    To request the next page of up to 100 log entries, pass the values of
    `nextEndDate` and `nextSkip` as the `end_date` and `skip` parameters,
    respectively:

    ```sh
    curl --request GET \\
      --header 'Authorization: Bearer <access_token>' \\
      'https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/logs?end_date={nextEndDate of previous response}&skip={nextSkip of previous response}'
    ```

    Repeat this step to get more pages until the response does not have a
    `nextEndDate` field. This signifies that you have reached the last page.

    For more information, see [GET /groups/{groupId}/apps/{appId}/logs](#section/adminGetLogs).
    """

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_logs(
        self,
        app_id: str,
        group_id: str,
        *,
        co_id: str | None = None,
        end_date: str | None = None,
        errors_only: bool | None = None,
        limit: int | None = None,
        skip: int | None = None,
        start_date: str | None = None,
        type: Literal["TRIGGER_FAILURE", "TRIGGER_ERROR_HANDLER", "DB_TRIGGER", "AUTH_TRIGGER", "SCHEDULED_TRIGGER", "FUNCTION", "SERVICE_FUNCTION", "STREAM_FUNCTION", "SERVICE_STREAM_FUNCTION", "AUTH", "WEBHOOK", "ENDPOINT", "PUSH", "API", "API_KEY", "GRAPHQL", "SYNC_CONNECTION_START", "SYNC_CONNECTION_END", "SYNC_SESSION_START", "SYNC_SESSION_END", "SYNC_CLIENT_WRITE", "SYNC_ERROR", "SYNC_OTHER", "SCHEMA_ADDITIVE_CHANGE", "SCHEMA_GENERATION", "SCHEMA_VALIDATION", "LOG_FORWARDER"] | None = None,
        user_id: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve App Services logs

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            co_id: Return only log messages associated with the given request Correlation ID.
            end_date: The date and time in ISO 8601 at which to cease returning results, inclusive.
            errors_only: The value of this field does not matter. If included in the request, this endpoint only returns error logs (even if the value is set to `false`). If this field is excluded from the request, this endpoint only returns non-error logs.
            limit: The maximum number of log entries to include in the response. If the query matches more than this many logs, it returns documents in ascending order by date until the limit is reached.
            skip: The offset number of matching log entries to skip before including them in the response.
            start_date: The date and time in ISO 8601 at which to begin returning results, exclusive.
            type: The kind of log you would like to retrieve.
            user_id: Return only log messages associated with the given `user_id`.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/logs"
        params = {
            "co_id": co_id,
            "end_date": end_date,
            "errors_only": errors_only,
            "limit": limit,
            "skip": skip,
            "start_date": start_date,
            "type": type,
            "user_id": user_id,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=dict[str, Any],
        )
