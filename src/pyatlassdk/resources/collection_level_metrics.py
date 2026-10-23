"""Generated resource for CollectionLevelMetrics. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from datetime import datetime
from urllib.parse import quote
from pyatlassdk.models.coll_stats_latency_namespace_metrics import CollStatsLatencyNamespaceMetrics
from pyatlassdk.models.coll_stats_ranked_namespaces_view import CollStatsRankedNamespacesView
from pyatlassdk.models.measurements_coll_stats_latency_cluster import MeasurementsCollStatsLatencyCluster
from pyatlassdk.models.measurements_coll_stats_latency_host import MeasurementsCollStatsLatencyHost
from pyatlassdk.models.namespaces_request import NamespacesRequest
from pyatlassdk.models.pinned_namespaces import PinnedNamespaces

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class CollectionLevelMetrics:
    """Returns, adds, and edits pinned namespaces for the specified cluster or process. Also returns collection level latency metric data."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_cluster_coll_stat_pinned_namespaces(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> PinnedNamespaces:
        """
        Return Pinned Namespaces

        Returns a list of given cluster's pinned namespaces, a set of namespaces manually selected by users to collect query latency metrics on.

        Args:
            cluster_name: Human-readable label that identifies the cluster to retrieve pinned namespaces for.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collStats/pinned"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PinnedNamespaces,
        )

    def update_group_cluster_coll_stat_pinned_namespaces(
        self,
        cluster_name: str,
        group_id: str,
        body: NamespacesRequest,
        *,
        envelope: bool | None = None,
    ) -> PinnedNamespaces:
        """
        Add Pinned Namespaces

        Add provided list of namespaces to existing pinned namespaces list for collection-level latency metrics collection for the given Group and Cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster to pin namespaces to.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: List of namespace strings (combination of database and collection name) to pin for query latency metric collection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collStats/pinned"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=PinnedNamespaces,
        )

    def pin_group_cluster_coll_stat_pinned_namespaces(
        self,
        cluster_name: str,
        group_id: str,
        body: NamespacesRequest,
        *,
        envelope: bool | None = None,
    ) -> PinnedNamespaces:
        """
        Pin Namespaces

        Pin provided list of namespaces for collection-level latency metrics collection for the given Group and Cluster. This initializes a pinned namespaces list or replaces any existing pinned namespaces list for the Group and Cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster to pin namespaces to.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: List of namespace strings (combination of database and collection name) to pin for query latency metric collection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collStats/pinned"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=PinnedNamespaces,
        )

    def unpin_group_cluster_coll_stat_unpin_namespaces(
        self,
        cluster_name: str,
        group_id: str,
        body: NamespacesRequest,
        *,
        envelope: bool | None = None,
    ) -> PinnedNamespaces:
        """
        Unpin Namespaces

        Unpin provided list of namespaces for collection-level latency metrics collection for the given Group and Cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster to unpin namespaces from.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: List of namespace strings (combination of database and collection name) to pin for query latency metric collection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collStats/unpin"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=PinnedNamespaces,
        )

    def get_group_cluster_coll_stat_namespaces(
        self,
        cluster_name: str,
        cluster_view: Literal["PRIMARY", "SECONDARY", "INDIVIDUAL_PROCESS"],
        group_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        period: str | None = None,
        start: datetime | None = None,
    ) -> CollStatsRankedNamespacesView:
        """
        Return Ranked Namespaces from One Cluster

        Return the subset of namespaces from the given cluster sorted by highest total execution time (descending) within the given time window.

        Args:
            cluster_name: Human-readable label that identifies the cluster to pin namespaces to.
            cluster_view: Human-readable label that identifies the cluster topology to retrieve metrics for.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/{quote(str(cluster_view), safe='')}/collStats/namespaces"
        params = {
            "end": end,
            "envelope": envelope,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CollStatsRankedNamespacesView,
        )

    def list_group_cluster_coll_stat_measurements(
        self,
        cluster_name: str,
        cluster_view: Literal["PRIMARY", "SECONDARY", "INDIVIDUAL_PROCESS"],
        collection_name: str,
        database_name: str,
        group_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        metrics: list[Literal["READS_OPS", "READS_LATENCY", "AVERAGE_READS_LATENCY", "READS_P50_VALUE", "READS_P95_VALUE", "READS_P99_VALUE", "WRITES_OPS", "WRITES_LATENCY", "AVERAGE_WRITES_LATENCY", "WRITES_P50_VALUE", "WRITES_P95_VALUE", "WRITES_P99_VALUE", "COMMANDS_OPS", "COMMANDS_LATENCY", "AVERAGE_COMMANDS_LATENCY", "COMMANDS_P50_VALUE", "COMMANDS_P95_VALUE", "COMMANDS_P99_VALUE", "TOTAL_OPS", "TOTAL_LATENCY", "AVERAGE_TOTAL_OPS_LATENCY", "TOTAL_OPS_P50_VALUE", "TOTAL_OPS_P95_VALUE", "TOTAL_OPS_P99_VALUE"]] | None = None,
        period: str | None = None,
        start: datetime | None = None,
    ) -> MeasurementsCollStatsLatencyCluster:
        """
        Return Cluster-Level Query Latency

        Get a list of the Coll Stats Latency cluster-level measurements for the given namespace.

        Args:
            cluster_name: Human-readable label that identifies the cluster to retrieve metrics for.
            cluster_view: Human-readable label that identifies the cluster topology to retrieve metrics for.
            collection_name: Human-readable label that identifies the collection.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            metrics: List that contains the metrics that you want to retrieve for the associated data series. If you don't set this parameter, this resource returns data series for all Coll Stats Latency metrics.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/{quote(str(cluster_view), safe='')}/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/collStats/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "metrics": metrics,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MeasurementsCollStatsLatencyCluster,
        )

    def list_group_coll_stat_metrics(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> CollStatsLatencyNamespaceMetrics:
        """
        Return All Metric Names

        Returns all available Coll Stats Latency metric names and their respective units for the specified project at the time of request.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/collStats/metrics"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CollStatsLatencyNamespaceMetrics,
        )

    def get_group_process_coll_stat_namespaces(
        self,
        group_id: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        period: str | None = None,
        start: datetime | None = None,
    ) -> CollStatsRankedNamespacesView:
        """
        Return Ranked Namespaces from One Host

        Return the subset of namespaces from the given process ranked by highest total execution time (descending) within the given time window.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/collStats/namespaces"
        params = {
            "end": end,
            "envelope": envelope,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CollStatsRankedNamespacesView,
        )

    def list_group_process_coll_stat_measurements(
        self,
        collection_name: str,
        database_name: str,
        group_id: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        metrics: list[Literal["READS_OPS", "READS_LATENCY", "AVERAGE_READS_LATENCY", "READS_P50_VALUE", "READS_P95_VALUE", "READS_P99_VALUE", "WRITES_OPS", "WRITES_LATENCY", "AVERAGE_WRITES_LATENCY", "WRITES_P50_VALUE", "WRITES_P95_VALUE", "WRITES_P99_VALUE", "COMMANDS_OPS", "COMMANDS_LATENCY", "AVERAGE_COMMANDS_LATENCY", "COMMANDS_P50_VALUE", "COMMANDS_P95_VALUE", "COMMANDS_P99_VALUE", "TOTAL_OPS", "TOTAL_LATENCY", "AVERAGE_TOTAL_OPS_LATENCY", "TOTAL_OPS_P50_VALUE", "TOTAL_OPS_P95_VALUE", "TOTAL_OPS_P99_VALUE"]] | None = None,
        period: str | None = None,
        start: datetime | None = None,
    ) -> MeasurementsCollStatsLatencyHost:
        """
        Return Host-Level Query Latency

        Get a list of the Coll Stats Latency process-level measurements for the given namespace.

        Args:
            collection_name: Human-readable label that identifies the collection.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            metrics: List that contains the metrics that you want to retrieve for the associated data series. If you don't set this parameter, this resource returns data series for all Coll Stats Latency metrics.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/collStats/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "metrics": metrics,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MeasurementsCollStatsLatencyHost,
        )
