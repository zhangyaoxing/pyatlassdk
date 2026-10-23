"""Generated resource for AccessTracking. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.mongo_db_access_logs_list import MongoDBAccessLogsList

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class AccessTracking:
    """Returns access logs for authentication attempts made to Atlas database deployments."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_db_access_history_cluster(
        self,
        cluster_name: str,
        group_id: str,
        *,
        auth_result: bool | None = None,
        end: int | None = None,
        envelope: bool | None = None,
        ip_address: str | None = None,
        n_logs: int | None = None,
        pretty: bool | None = None,
        start: int | None = None,
    ) -> MongoDBAccessLogsList:
        """
        Return Database Access History for One Cluster by Cluster Name

        Returns the access logs of one cluster identified by the cluster's name. Access logs contain a list of authentication requests made against your cluster. You can't use this feature on tenant-tier clusters (M0, M2, M5).

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            auth_result: Flag that indicates whether the response returns the successful authentication attempts only.
            end: Date and time when to stop retrieving database history. If you specify **end**, you must also specify **start**. This parameter uses UNIX epoch time in milliseconds.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            ip_address: One Internet Protocol address that attempted to authenticate with the database.
            n_logs: Maximum number of lines from the log to return.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            start: Date and time when MongoDB Cloud begins retrieving database history. If you specify **start**, you must also specify **end**. This parameter uses UNIX epoch time in milliseconds.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dbAccessHistory/clusters/{quote(str(cluster_name), safe='')}"
        params = {
            "authResult": auth_result,
            "end": end,
            "envelope": envelope,
            "ipAddress": ip_address,
            "nLogs": n_logs,
            "pretty": pretty,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MongoDBAccessLogsList,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_db_access_history_process(
        self,
        group_id: str,
        hostname: str,
        *,
        auth_result: bool | None = None,
        end: int | None = None,
        envelope: bool | None = None,
        ip_address: str | None = None,
        n_logs: int | None = None,
        pretty: bool | None = None,
        start: int | None = None,
    ) -> MongoDBAccessLogsList:
        """
        Return Database Access History for One Cluster by Hostname

        Returns the access logs of one cluster identified by the cluster's hostname. Access logs contain a list of authentication requests made against your clusters. You can't use this feature on tenant-tier clusters (M0, M2, M5).

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            hostname: Fully qualified domain name or IP address of the MongoDB host that stores the log files that you want to download.
            auth_result: Flag that indicates whether the response returns the successful authentication attempts only.
            end: Date and time when to stop retrieving database history. If you specify **end**, you must also specify **start**. This parameter uses UNIX epoch time in milliseconds.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            ip_address: One Internet Protocol address that attempted to authenticate with the database.
            n_logs: Maximum number of lines from the log to return.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            start: Date and time when MongoDB Cloud begins retrieving database history. If you specify **start**, you must also specify **end**. This parameter uses UNIX epoch time in milliseconds.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dbAccessHistory/processes/{quote(str(hostname), safe='')}"
        params = {
            "authResult": auth_result,
            "end": end,
            "envelope": envelope,
            "ipAddress": ip_address,
            "nLogs": n_logs,
            "pretty": pretty,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MongoDBAccessLogsList,
            accept="application/vnd.atlas.2023-01-01+json",
        )
