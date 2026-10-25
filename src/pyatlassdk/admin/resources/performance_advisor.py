"""Generated resource for PerformanceAdvisor. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.enveloped_drop_index_suggestions_response import EnvelopedDropIndexSuggestionsResponse
from pyatlassdk.admin.models.enveloped_performance_advisor_response import EnvelopedPerformanceAdvisorResponse
from pyatlassdk.admin.models.enveloped_schema_advisor_response import EnvelopedSchemaAdvisorResponse
from pyatlassdk.admin.models.namespaces import Namespaces
from pyatlassdk.admin.models.performance_advisor_response import PerformanceAdvisorResponse
from pyatlassdk.admin.models.performance_advisor_slow_query_list import PerformanceAdvisorSlowQueryList

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class PerformanceAdvisor:
    """Returns suggested indexes and slow query data for a database deployment. Also enables or disables MongoDB Cloud-managed slow operation thresholds. To view field values in a sample query, you must have the Project Data Access Read Only role or higher. Otherwise, MongoDB Cloud returns redacted data rather than the field values."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_group_cluster_performance_advisor_drop_index_suggestions(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> EnvelopedDropIndexSuggestionsResponse:
        """
        Return All Suggested Indexes to Drop

        Returns the indexes that the Performance Advisor suggests to drop. The Performance Advisor suggests dropping unused, redundant, and hidden indexes to improve write performance and increase storage space.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/performanceAdvisor/dropIndexSuggestions"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EnvelopedDropIndexSuggestionsResponse,
            accept="application/vnd.atlas.2024-08-05+json",
        )

    def list_group_cluster_performance_advisor_schema_advice(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> EnvelopedSchemaAdvisorResponse:
        """
        Return Schema Advice

        Returns the schema suggestions that the Performance Advisor detects. The Performance Advisor provides holistic schema recommendations for your cluster by sampling documents in your most active collections and collections with slow-running queries.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/performanceAdvisor/schemaAdvice"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EnvelopedSchemaAdvisorResponse,
            accept="application/vnd.atlas.2024-08-05+json",
        )

    def list_group_cluster_performance_advisor_suggested_indexes(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        namespaces: list[str] | None = None,
        process_ids: list[str] | None = None,
        since: int | None = None,
        until: int | None = None,
    ) -> EnvelopedPerformanceAdvisorResponse:
        """
        Return All Suggested Indexes

        Returns the indexes that the Performance Advisor suggests. The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            namespaces: Namespaces from which to retrieve suggested indexes. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
            process_ids: Process IDs from which to retrieve suggested indexes. A `processId` is a combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests. To include multiple `processIds`, pass the parameter multiple times delimited with an ampersand (`&`) between each `processId`.
            since: Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you don't specify the **until** parameter, the endpoint returns data covering from the **since** value and the current time. - If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
            until: Date and time up until which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you specify the **until** parameter, you must specify the **since** parameter. - If you specify neither the **since** nor the **until** parameters, the endpoint returns data from the previous 24 hours.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/performanceAdvisor/suggestedIndexes"
        params = {
            "envelope": envelope,
            "namespaces": namespaces,
            "processIds": process_ids,
            "since": since,
            "until": until,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EnvelopedPerformanceAdvisorResponse,
            accept="application/vnd.atlas.2024-08-05+json",
        )

    def get_group_managed_slow_ms(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> bool:
        """
        Return Managed Slow Operation Threshold Status

        Get whether the Managed Slow MS feature is enabled.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/managedSlowMs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=bool,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def disable_group_managed_slow_ms(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Disable Managed Slow Operation Threshold

        Disables the slow operation threshold that MongoDB Cloud calculated for the specified project. The threshold determines which operations the Performance Advisor and Query Profiler considers slow. When enabled, MongoDB Cloud uses the average execution time for operations on your cluster to determine slow-running queries. As a result, the threshold is more pertinent to your cluster workload. The slow operation threshold is enabled by default for dedicated clusters (M10+). When disabled, MongoDB Cloud considers any operation that takes longer than 100 milliseconds to be slow.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/managedSlowMs/disable"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def enable_group_managed_slow_ms(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Enable Managed Slow Operation Threshold

        Enables MongoDB Cloud to use its slow operation threshold for the specified project. The threshold determines which operations the Performance Advisor and Query Profiler considers slow. When enabled, MongoDB Cloud uses the average execution time for operations on your cluster to determine slow-running queries. As a result, the threshold is more pertinent to your cluster workload. The slow operation threshold is enabled by default for dedicated clusters (M10+). When disabled, MongoDB Cloud considers any operation that takes longer than 100 milliseconds to be slow.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/managedSlowMs/enable"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_process_performance_advisor_namespaces(
        self,
        group_id: str,
        process_id: str,
        *,
        duration: int | None = None,
        envelope: bool | None = None,
        pretty: bool | None = None,
        since: int | None = None,
    ) -> Namespaces:
        """
        Return All Namespaces for One Host

        Returns up to 20 namespaces for collections experiencing slow queries on the specified host. If you specify a secondary member of a replica set that hasn't received any database read operations, the endpoint doesn't return any namespaces.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            duration: Length of time expressed during which the query finds suggested indexes among the managed namespaces in the cluster. This parameter expresses its value in milliseconds. - If you don't specify the **since** parameter, the endpoint returns data covering the duration before the current time. - If you specify neither the **duration** nor **since** parameters, the endpoint returns data from the previous 24 hours.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            since: Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you don't specify the **duration** parameter, the endpoint returns data covering from the **since** value and the current time. - If you specify neither the **duration** nor the **since** parameters, the endpoint returns data from the previous 24 hours.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/performanceAdvisor/namespaces"
        params = {
            "duration": duration,
            "envelope": envelope,
            "pretty": pretty,
            "since": since,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=Namespaces,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_process_performance_advisor_slow_query_logs(
        self,
        group_id: str,
        process_id: str,
        *,
        duration: int | None = None,
        envelope: bool | None = None,
        include_metrics: bool | None = None,
        include_op_type: bool | None = None,
        include_replica_state: bool | None = None,
        n_logs: int | None = None,
        namespaces: list[str] | None = None,
        pretty: bool | None = None,
        since: int | None = None,
    ) -> PerformanceAdvisorSlowQueryList:
        """
        Return Slow Queries

        Returns log lines for slow queries that the Performance Advisor and Query Profiler identified. The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance. MongoDB Cloud bases the threshold for slow queries on the average time of operations on your cluster. This enables workload-relevant recommendations.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            duration: Length of time expressed during which the query finds slow queries among the managed namespaces in the cluster. This parameter expresses its value in milliseconds. - If you don't specify the **since** parameter, the endpoint returns data covering the duration before the current time. - If you specify neither the **duration** nor **since** parameters, the endpoint returns data from the previous 24 hours.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_metrics: Whether or not to include metrics extracted from the slow query log as separate fields.
            include_op_type: Whether or not to include the operation type (read/write/command) extracted from the slow query log as a separate field.
            include_replica_state: Whether or not to include the replica state of the host when the slow query log was generated as a separate field.
            n_logs: Maximum number of lines from the log to return.
            namespaces: Namespaces from which to retrieve slow queries. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            since: Date and time from which the query retrieves the slow queries. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you don't specify the **duration** parameter, the endpoint returns data covering from the **since** value and the current time. - If you specify neither the **duration** nor the **since** parameters, the endpoint returns data from the previous 24 hours.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/performanceAdvisor/slowQueryLogs"
        params = {
            "duration": duration,
            "envelope": envelope,
            "includeMetrics": include_metrics,
            "includeOpType": include_op_type,
            "includeReplicaState": include_replica_state,
            "nLogs": n_logs,
            "namespaces": namespaces,
            "pretty": pretty,
            "since": since,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PerformanceAdvisorSlowQueryList,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_process_performance_advisor_suggested_indexes(
        self,
        group_id: str,
        process_id: str,
        *,
        duration: int | None = None,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        n_examples: int | None = None,
        n_indexes: int | None = None,
        namespaces: list[str] | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        since: int | None = None,
    ) -> PerformanceAdvisorResponse:
        """
        Return All Suggested Indexes

        Returns the indexes that the Performance Advisor suggests. The Performance Advisor monitors queries that MongoDB considers slow and suggests new indexes to improve query performance.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of host and port that serves the MongoDB process. The host must be the hostname, FQDN, IPv4 address, or IPv6 address of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            duration: Length of time expressed during which the query finds suggested indexes among the managed namespaces in the cluster. This parameter expresses its value in milliseconds. - If you don't specify the **since** parameter, the endpoint returns data covering the duration before the current time. - If you specify neither the **duration** nor **since** parameters, the endpoint returns data from the previous 24 hours.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            n_examples: Maximum number of example queries that benefit from the suggested index.
            n_indexes: Number that indicates the maximum indexes to suggest.
            namespaces: Namespaces from which to retrieve suggested indexes. A namespace consists of one database and one collection resource written as `.`: `<database>.<collection>`. To include multiple namespaces, pass the parameter multiple times delimited with an ampersand (`&`) between each namespace. Omit this parameter to return results for all namespaces.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            since: Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of milliseconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). - If you don't specify the **duration** parameter, the endpoint returns data covering from the **since** value and the current time. - If you specify neither the **duration** nor the **since** parameters, the endpoint returns data from the previous 24 hours.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/performanceAdvisor/suggestedIndexes"
        params = {
            "duration": duration,
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "nExamples": n_examples,
            "nIndexes": n_indexes,
            "namespaces": namespaces,
            "pageNum": page_num,
            "pretty": pretty,
            "since": since,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PerformanceAdvisorResponse,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_serverless_performance_advisor_auto_indexing(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> bool:
        """
        Return Serverless Auto-Indexing Status

        Get whether the Serverless Auto Indexing feature is enabled. This endpoint returns a value for Flex clusters that were created with the Create Serverless Instance endpoint or Flex clusters that were migrated from Serverless instances. However, the value returned is not indicative of the Auto Indexing state as Auto Indexing is unavailable for Flex clusters. This endpoint will be sunset on January 22, 2026.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/serverless/{quote(str(cluster_name), safe='')}/performanceAdvisor/autoIndexing"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=bool,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def set_group_serverless_performance_advisor_auto_indexing(
        self,
        cluster_name: str,
        group_id: str,
        *,
        enable: bool,
        pretty: bool | None = None,
    ) -> Any:
        """
        Set Serverless Auto-Indexing Status

        Set whether the Serverless Auto Indexing feature is enabled. This endpoint sets a value for Flex clusters that were created with the Create Serverless Instance endpoint or Flex clusters that were migrated from Serverless instances. However, the value returned is not indicative of the Auto Indexing state as Auto Indexing is unavailable for Flex clusters. This endpoint will be sunset on January 22, 2026.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            enable: Value that we want to set for the Serverless Auto Indexing toggle.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/serverless/{quote(str(cluster_name), safe='')}/performanceAdvisor/autoIndexing"
        params = {
            "enable": enable,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )
