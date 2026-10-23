"""Generated resource for QueryShapeInsights. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.paginated_query_shapes import PaginatedQueryShapes
from pyatlassdk.models.query_shape_response import QueryShapeResponse
from pyatlassdk.models.query_shape_update_request import QueryShapeUpdateRequest
from pyatlassdk.models.query_stats_details_response import QueryStatsDetailsResponse
from pyatlassdk.models.query_stats_summary_list_response import QueryStatsSummaryListResponse

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class QueryShapeInsights:
    """Operations for QueryShapeInsights."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_cluster_query_shape_insight_summaries(
        self,
        cluster_name: str,
        group_id: str,
        *,
        commands: list[Literal["find", "distinct", "aggregate", "count", "insert", "update", "delete"]] | None = None,
        envelope: bool | None = None,
        n_summaries: int | None = None,
        namespaces: list[str] | None = None,
        pretty: bool | None = None,
        process_ids: list[str] | None = None,
        query_shape_hashes: list[str] | None = None,
        series: list[Literal["TOTAL_EXECUTION_TIME", "AVG_EXECUTION_TIME", "EXECUTION_COUNT", "KEYS_EXAMINED", "DOCS_EXAMINED", "DOCS_RETURNED", "TOTAL_TIME_TO_RESPONSE", "AVG_TIME_TO_RESPONSE", "BYTES_READ", "CPU_TIME", "KEYS_EXAMINED_RETURNED", "DOCS_EXAMINED_RETURNED", "LAST_EXECUTION_TIME", "P50_EXECUTION_TIME", "P90_EXECUTION_TIME", "P99_EXECUTION_TIME", "DOCS_MATCHED", "DOCS_MODIFIED", "DOCS_UPSERTED", "DOCS_DELETED", "DOCS_INSERTED", "KEYS_INSERTED", "KEYS_DELETED"]] | None = None,
        since: int | None = None,
        until: int | None = None,
    ) -> QueryStatsSummaryListResponse:
        """
        Return Query Statistic Summaries

        Returns a list of query shape statistics summaries for a given cluster. Query shape statistics provide performance insights about MongoDB queries, helping users identify problematic query patterns and potential optimizations.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            commands: Retrieve query shape statistics matching specified MongoDB commands. To include multiple commands, pass the parameter multiple times delimited with an ampersand (`&`) between each command. The currently supported parameters are: find, distinct, aggregate, count, insert, update, and delete. The insert, update, and delete commands return results only for clusters running MongoDB 9.0 or later with write query shape statistics enabled for the project. Omit this parameter to return results for all supported commands.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            n_summaries: Maximum number of query statistic summaries to return.
            namespaces: Namespaces from which to retrieve query shape statistics. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            process_ids: Process IDs from which to retrieve query shape statistics. A `processId` is a combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests. To include multiple `processId`, pass the parameter multiple times delimited with an ampersand (`&`) between each `processId`.
            query_shape_hashes: A list of SHA256 hashes of desired query shapes, output by MongoDB commands like `$queryStats` and $explain or slow query logs. To include multiple series, pass the parameter multiple times delimited with an ampersand (`&`) between each series. Omit this parameter to return results for all available series.
            series: Query shape statistics data series to retrieve. A series represents a specific metric about query execution. To include multiple series, pass the parameter multiple times delimited with an ampersand (`&`) between each series. Omit this parameter to return results for all available series. The `P50_EXECUTION_TIME`, `P90_EXECUTION_TIME`, and `P99_EXECUTION_TIME` series are deprecated as the values they report may be inaccurate. They will be removed in a future release.
            since: Date and time from which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you don't specify the **until** parameter, the endpoint returns data covering from the **since** value and the current time. - If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
            until: Date and time up until which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you specify the **until** parameter, you must specify the **since** parameter. - If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/queryShapeInsights/summaries"
        params = {
            "commands": commands,
            "envelope": envelope,
            "nSummaries": n_summaries,
            "namespaces": namespaces,
            "pretty": pretty,
            "processIds": process_ids,
            "queryShapeHashes": query_shape_hashes,
            "series": series,
            "since": since,
            "until": until,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=QueryStatsSummaryListResponse,
        )

    def get_group_cluster_query_shape_insight_details(
        self,
        cluster_name: str,
        group_id: str,
        query_shape_hash: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        process_ids: list[str] | None = None,
        since: int | None = None,
        until: int | None = None,
    ) -> QueryStatsDetailsResponse:
        """
        Return Query Shape Details

        Returns the metadata and statistics summary for a given query shape hash.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            query_shape_hash: A SHA256 hash of a query shape, output by MongoDB commands like `$queryStats` and `$explain` or slow query logs.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            process_ids: Process IDs from which to retrieve query shape statistics. A `processId` is a combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests. To include multiple `processIds`, pass the parameter multiple times delimited with an ampersand (`&`) between each `processId`.
            since: Date and time from which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you don't specify the **until** parameter, the endpoint returns data covering from the **since** value and the current time. - If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
            until: Date and time up until which to retrieve query shape statistics. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you specify the **until** parameter, you must specify the **since** parameter. - If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/queryShapeInsights/{quote(str(query_shape_hash), safe='')}/details"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "processIds": process_ids,
            "since": since,
            "until": until,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=QueryStatsDetailsResponse,
        )

    def list_group_cluster_query_shapes(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        status: Literal["REJECTED"] | None = None,
    ) -> PaginatedQueryShapes:
        """
        Return All Query Shapes

        Returns a list of query shapes for one cluster. Query shapes may be filtered by their status; at present, this endpoint supports only the REJECTED status.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            status: The status of query shapes to retrieve. Only REJECTED status is supported. If omitted, defaults to REJECTED.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/queryShapes"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "status": status,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedQueryShapes,
        )

    def get_group_cluster_query_shape(
        self,
        cluster_name: str,
        group_id: str,
        query_shape_hash: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> QueryShapeResponse:
        """
        Return One Query Shape

        Returns the details for a single query shape. This endpoint only returns query shapes with REJECTED status. If the specified query shape hash does not correspond to a rejected query shape, a 404 Not Found error is returned.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            query_shape_hash: A SHA256 hash of a query shape, output by MongoDB commands like `$queryStats` and `$explain` or slow query logs.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/queryShapes/{quote(str(query_shape_hash), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=QueryShapeResponse,
        )

    def update_group_cluster_query_shape(
        self,
        cluster_name: str,
        group_id: str,
        query_shape_hash: str,
        body: QueryShapeUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> QueryShapeResponse:
        """
        Update Query Shape Rejection Status

        Updates the rejection status of a query shape. Use this endpoint to reject a query shape (preventing it from executing on the cluster) or to unreject a previously rejected query shape (allowing it to execute again). This operation is idempotent: rejecting an already rejected query shape or unrejecting an already unrejected query shape will return 200 OK.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            query_shape_hash: A SHA256 hash of a query shape, output by MongoDB commands like `$queryStats` and `$explain` or slow query logs.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The desired rejection status for the query shape. Provide REJECTED to block the query shape from executing, or UNREJECTED to allow it to execute.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/queryShapes/{quote(str(query_shape_hash), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=QueryShapeResponse,
        )
