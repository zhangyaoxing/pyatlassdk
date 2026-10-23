"""Generated resource for MonitoringAndLogs. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from datetime import datetime
from urllib.parse import quote
from pyatlassdk.models.api_host_view_atlas import ApiHostViewAtlas
from pyatlassdk.models.api_measurements_general_view_atlas import ApiMeasurementsGeneralViewAtlas
from pyatlassdk.models.cloud_search_metrics import CloudSearchMetrics
from pyatlassdk.models.measurement_disk_partition import MeasurementDiskPartition
from pyatlassdk.models.measurements_indexes import MeasurementsIndexes
from pyatlassdk.models.measurements_non_index import MeasurementsNonIndex
from pyatlassdk.models.mesurements_database import MesurementsDatabase
from pyatlassdk.models.paginated_database_view import PaginatedDatabaseView
from pyatlassdk.models.paginated_disk_partition_view import PaginatedDiskPartitionView
from pyatlassdk.models.paginated_host_view_atlas import PaginatedHostViewAtlas

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class MonitoringAndLogs:
    """Returns database deployment monitoring and logging data."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def download_group_cluster_log(
        self,
        group_id: str,
        host_name: str,
        log_name: Literal["mongodb", "mongos", "mongodb-audit-log", "mongos-audit-log"],
        *,
        end_date: int | None = None,
        envelope: bool | None = None,
        start_date: int | None = None,
    ) -> str:
        """
        Download Logs for One Cluster Host in One Project

        Returns a compressed (.gz) log file that contains a range of log messages for the specified host for the specified project. MongoDB updates process and audit logs from the cluster backend infrastructure every five minutes. Logs are stored in chunks approximately five minutes in length, but this duration may vary. If you poll the API for log files, we recommend polling every five minutes even though consecutive polls could contain some overlapping logs. This feature isn't available for `M0` free clusters, `M2`, `M5`, flex, or serverless clusters. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            host_name: Human-readable label that identifies the host that stores the log files that you want to download.
            log_name: Human-readable label that identifies the log file that you want to return. To return audit logs, enable *Database Auditing* for the specified project.
            end_date: Specifies the date and time for the ending point of the range of log messages to retrieve, in the number of seconds that have elapsed since the UNIX epoch. This value will default to 24 hours after the start date. If the start date is also unspecified, the value will default to the time of the request.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            start_date: Specifies the date and time for the starting point of the range of log messages to retrieve, in the number of seconds that have elapsed since the UNIX epoch. This value will default to 24 hours prior to the end date. If the end date is also unspecified, the value will default to 24 hours prior to the time of the request.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(host_name), safe='')}/logs/{quote(str(log_name), safe='')}.gz"
        params = {
            "endDate": end_date,
            "envelope": envelope,
            "startDate": start_date,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=str,
            accept="application/vnd.atlas.2023-02-01+gzip",
        )

    def list_group_host_fts_metrics(
        self,
        group_id: str,
        process_id: str,
        *,
        envelope: bool | None = None,
    ) -> CloudSearchMetrics:
        """
        Return All Atlas Search Metric Types for One Process

        Returns all Atlas Search metric types available for one process in the specified project. You must have the Project Read Only or higher role to view the Atlas Search metric types.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/hosts/{quote(str(process_id), safe='')}/fts/metrics"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CloudSearchMetrics,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_host_fts_metric_index_measurements(
        self,
        collection_name: str,
        database_name: str,
        group_id: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        granularity: str,
        metrics: list[Literal["INDEX_SIZE_ON_DISK", "NUMBER_OF_DELETES", "NUMBER_OF_ERROR_QUERIES", "NUMBER_OF_GETMORE_COMMANDS", "NUMBER_OF_INDEX_FIELDS", "NUMBER_OF_INSERTS", "NUMBER_OF_SUCCESS_QUERIES", "NUMBER_OF_UPDATES", "REPLICATION_LAG", "TOTAL_NUMBER_OF_QUERIES"]],
        period: str | None = None,
        start: datetime | None = None,
    ) -> MeasurementsIndexes:
        """
        Return All Atlas Search Index Metrics for One Namespace

        Returns the Atlas Search index metrics within the specified time range for one namespace in the specified process.

        Args:
            collection_name: Human-readable label that identifies the collection.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            granularity: Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
            metrics: List that contains the measurements that MongoDB Atlas reports for the associated data series.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/hosts/{quote(str(process_id), safe='')}/fts/metrics/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "granularity": granularity,
            "metrics": metrics,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MeasurementsIndexes,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_host_fts_metric_index_measurements(
        self,
        collection_name: str,
        database_name: str,
        group_id: str,
        index_name: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        granularity: str,
        metrics: list[Literal["INDEX_SIZE_ON_DISK", "NUMBER_OF_DELETES", "NUMBER_OF_ERROR_QUERIES", "NUMBER_OF_GETMORE_COMMANDS", "NUMBER_OF_INDEX_FIELDS", "NUMBER_OF_INSERTS", "NUMBER_OF_SUCCESS_QUERIES", "NUMBER_OF_UPDATES", "REPLICATION_LAG", "TOTAL_NUMBER_OF_QUERIES"]],
        period: str | None = None,
        start: datetime | None = None,
    ) -> MeasurementsIndexes:
        """
        Return Atlas Search Metrics for One Index in One Namespace

        Returns the Atlas Search metrics data series within the provided time range for one namespace and index name on the specified process. You must have the Project Read Only or higher role to view the Atlas Search metric types.

        Args:
            collection_name: Human-readable label that identifies the collection.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_name: Human-readable label that identifies the index.
            process_id: Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            granularity: Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
            metrics: List that contains the measurements that MongoDB Atlas reports for the associated data series.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/hosts/{quote(str(process_id), safe='')}/fts/metrics/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/{quote(str(index_name), safe='')}/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "granularity": granularity,
            "metrics": metrics,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MeasurementsIndexes,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_host_fts_metric_measurements(
        self,
        group_id: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        granularity: str,
        metrics: list[Literal["FTS_DISK_USAGE", "FTS_PROCESS_CPU_KERNEL", "FTS_PROCESS_CPU_USER", "FTS_PROCESS_NORMALIZED_CPU_KERNEL", "FTS_PROCESS_NORMALIZED_CPU_USER", "FTS_PROCESS_RESIDENT_MEMORY", "FTS_PROCESS_SHARED_MEMORY", "FTS_PROCESS_VIRTUAL_MEMORY", "JVM_CURRENT_MEMORY", "JVM_MAX_MEMORY", "PAGE_FAULTS"]],
        period: str | None = None,
        start: datetime | None = None,
    ) -> MeasurementsNonIndex:
        """
        Return Atlas Search Hardware and Status Metrics

        Returns the Atlas Search hardware and status data series within the provided time range for one process in the specified project. You must have the Project Read Only or higher role to view the Atlas Search metric types.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and IANA port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (mongod or mongos). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            granularity: Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
            metrics: List that contains the metrics that you want MongoDB Atlas to report for the associated data series. If you don't set this parameter, this resource returns all hardware and status metrics for the associated data series.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/hosts/{quote(str(process_id), safe='')}/fts/metrics/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "granularity": granularity,
            "metrics": metrics,
            "period": period,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MeasurementsNonIndex,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_processes(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedHostViewAtlas:
        """
        Return All MongoDB Processes in One Project

        Returns details of all processes for the specified project. A MongoDB process can be either a `mongod` or `mongos`.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedHostViewAtlas,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_process(
        self,
        group_id: str,
        process_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiHostViewAtlas:
        """
        Return One MongoDB Process by ID

        Returns the processes for the specified host for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiHostViewAtlas,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_process_databases(
        self,
        group_id: str,
        process_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedDatabaseView:
        """
        Return Available Databases for One MongoDB Process

        Returns the list of databases running on the specified host for the specified project. `M0` free clusters, `M2`, `M5`, serverless, and Flex clusters have some operational limits. The MongoDB Cloud process must be a `mongod`.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod`). The port must be the IANA port on which the MongoDB process listens for requests.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/databases"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedDatabaseView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_process_database(
        self,
        database_name: str,
        group_id: str,
        process_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> MesurementsDatabase:
        """
        Return One Database for One MongoDB Process

        Returns one database running on the specified host for the specified project.

        Args:
            database_name: Human-readable label that identifies the database that the specified MongoDB process serves.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/databases/{quote(str(database_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MesurementsDatabase,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_process_database_measurements(
        self,
        database_name: str,
        group_id: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        granularity: str,
        m: list[Literal["DATABASE_AVERAGE_OBJECT_SIZE", "DATABASE_COLLECTION_COUNT", "DATABASE_DATA_SIZE", "DATABASE_STORAGE_SIZE", "DATABASE_INDEX_SIZE", "DATABASE_INDEX_COUNT", "DATABASE_EXTENT_COUNT", "DATABASE_OBJECT_COUNT", "DATABASE_VIEW_COUNT"]] | None = None,
        period: str | None = None,
        pretty: bool | None = None,
        start: datetime | None = None,
    ) -> ApiMeasurementsGeneralViewAtlas:
        """
        Return Measurements for One Database in One MongoDB Process

        Returns the measurements of one database for the specified host for the specified project. Returns the database's on-disk storage space based on the MongoDB `dbStats` command output. To calculate some metric series, Atlas takes the rate between every two adjacent points. For these metric series, the first data point has a null value because Atlas can't calculate a rate for the first data point given the query time range. Atlas retrieves database metrics every 20 minutes but reduces frequency when necessary to optimize database performance.

        Args:
            database_name: Human-readable label that identifies the database that the specified MongoDB process serves.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            granularity: Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
            m: One or more types of measurement to request for this MongoDB process. If omitted, the resource returns all measurements. To specify multiple values for `m`, repeat the `m` parameter for each value. Specify measurements that apply to the specified host. MongoDB Cloud returns an error if you specified any invalid measurements.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/databases/{quote(str(database_name), safe='')}/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "granularity": granularity,
            "m": m,
            "period": period,
            "pretty": pretty,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiMeasurementsGeneralViewAtlas,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_process_disks(
        self,
        group_id: str,
        process_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedDiskPartitionView:
        """
        Return Available Disks for One MongoDB Process

        Returns the list of disks or partitions for the specified host for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/disks"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedDiskPartitionView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_process_disk(
        self,
        group_id: str,
        partition_name: str,
        process_id: str,
        *,
        envelope: bool | None = None,
    ) -> MeasurementDiskPartition:
        """
        Return Measurements for One Disk

        Returns measurement details for one disk or partition for the specified host for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            partition_name: Human-readable label of the disk or partition to which the measurements apply.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/disks/{quote(str(partition_name), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MeasurementDiskPartition,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_process_disk_measurements(
        self,
        group_id: str,
        partition_name: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        granularity: str,
        m: list[Literal["DISK_PARTITION_IOPS_READ", "MAX_DISK_PARTITION_IOPS_READ", "DISK_PARTITION_IOPS_WRITE", "MAX_DISK_PARTITION_IOPS_WRITE", "DISK_PARTITION_IOPS_TOTAL", "MAX_DISK_PARTITION_IOPS_TOTAL", "DISK_PARTITION_LATENCY_READ", "MAX_DISK_PARTITION_LATENCY_READ", "DISK_PARTITION_LATENCY_WRITE", "MAX_DISK_PARTITION_LATENCY_WRITE", "DISK_PARTITION_SPACE_FREE", "MAX_DISK_PARTITION_SPACE_FREE", "DISK_PARTITION_SPACE_USED", "MAX_DISK_PARTITION_SPACE_USED", "DISK_PARTITION_SPACE_PERCENT_FREE", "MAX_DISK_PARTITION_SPACE_PERCENT_FREE", "DISK_PARTITION_SPACE_PERCENT_USED", "MAX_DISK_PARTITION_SPACE_PERCENT_USED", "DISK_PARTITION_THROUGHPUT_READ", "DISK_PARTITION_THROUGHPUT_WRITE", "DISK_QUEUE_DEPTH"]] | None = None,
        period: str | None = None,
        pretty: bool | None = None,
        start: datetime | None = None,
    ) -> ApiMeasurementsGeneralViewAtlas:
        """
        Return Measurements of One Disk for One MongoDB Process

        Returns the measurements of one disk or partition for the specified host for the specified project. Returned value can be one of the following:
        - Throughput of I/O operations for the disk partition used for the MongoDB process
        - Percentage of time during which requests the partition issued and serviced
        - Latency per operation type of the disk partition used for the MongoDB process
        - Amount of free and used disk space on the disk partition used for the MongoDB process.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            partition_name: Human-readable label of the disk or partition to which the measurements apply.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            granularity: Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
            m: One or more types of measurement to request for this MongoDB process. If omitted, the resource returns all measurements. To specify multiple values for `m`, repeat the `m` parameter for each value. Specify measurements that apply to the specified host. MongoDB Cloud returns an error if you specified any invalid measurements.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/disks/{quote(str(partition_name), safe='')}/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "granularity": granularity,
            "m": m,
            "period": period,
            "pretty": pretty,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiMeasurementsGeneralViewAtlas,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_process_measurements(
        self,
        group_id: str,
        process_id: str,
        *,
        end: datetime | None = None,
        envelope: bool | None = None,
        granularity: str,
        m: list[Literal["ASSERT_MSG", "ASSERT_REGULAR", "ASSERT_USER", "ASSERT_WARNING", "BACKGROUND_FLUSH_AVG", "CACHE_BYTES_READ_INTO", "CACHE_BYTES_WRITTEN_FROM", "CACHE_DIRTY_BYTES", "CACHE_USED_BYTES", "CACHE_FILL_RATIO", "DIRTY_FILL_RATIO", "COMPUTED_MEMORY", "CONNECTIONS", "CURSORS_TOTAL_OPEN", "CURSORS_TOTAL_TIMED_OUT", "DB_DATA_SIZE_TOTAL", "DB_STORAGE_TOTAL", "DOCUMENT_METRICS_DELETED", "DOCUMENT_METRICS_INSERTED", "DOCUMENT_METRICS_RETURNED", "DOCUMENT_METRICS_UPDATED", "EXTRA_INFO_PAGE_FAULTS", "FTS_DISK_UTILIZATION", "FTS_MEMORY_MAPPED", "FTS_MEMORY_RESIDENT", "FTS_MEMORY_VIRTUAL", "FTS_PROCESS_CPU_KERNEL", "FTS_PROCESS_CPU_USER", "FTS_PROCESS_NORMALIZED_CPU_KERNEL", "FTS_PROCESS_NORMALIZED_CPU_USER", "GLOBAL_ACCESSES_NOT_IN_MEMORY", "GLOBAL_LOCK_CURRENT_QUEUE_READERS", "GLOBAL_LOCK_CURRENT_QUEUE_TOTAL", "GLOBAL_LOCK_CURRENT_QUEUE_WRITERS", "GLOBAL_PAGE_FAULT_EXCEPTIONS_THROWN", "INDEX_COUNTERS_BTREE_ACCESSES", "INDEX_COUNTERS_BTREE_HITS", "INDEX_COUNTERS_BTREE_MISS_RATIO", "INDEX_COUNTERS_BTREE_MISSES", "JOURNALING_COMMITS_IN_WRITE_LOCK", "JOURNALING_MB", "JOURNALING_WRITE_DATA_FILES_MB", "MAX_PROCESS_CPU_CHILDREN_KERNEL", "MAX_PROCESS_CPU_CHILDREN_USER", "MAX_PROCESS_CPU_KERNEL", "MAX_PROCESS_CPU_USER", "MAX_PROCESS_NORMALIZED_CPU_CHILDREN_KERNEL", "MAX_PROCESS_NORMALIZED_CPU_CHILDREN_USER", "MAX_PROCESS_NORMALIZED_CPU_KERNEL", "MAX_PROCESS_NORMALIZED_CPU_USER", "MAX_SWAP_USAGE_FREE", "MAX_SWAP_USAGE_USED", "MAX_SYSTEM_CPU_GUEST", "MAX_SYSTEM_CPU_IOWAIT", "MAX_SYSTEM_CPU_IRQ", "MAX_SYSTEM_CPU_KERNEL", "MAX_SYSTEM_CPU_SOFTIRQ", "MAX_SYSTEM_CPU_STEAL", "MAX_SYSTEM_CPU_USER", "MAX_SYSTEM_MEMORY_AVAILABLE", "MAX_SYSTEM_MEMORY_FREE", "MAX_SYSTEM_MEMORY_USED", "MAX_SYSTEM_NETWORK_IN", "MAX_SYSTEM_NETWORK_OUT", "MAX_SYSTEM_NORMALIZED_CPU_GUEST", "MAX_SYSTEM_NORMALIZED_CPU_IOWAIT", "MAX_SYSTEM_NORMALIZED_CPU_IRQ", "MAX_SYSTEM_NORMALIZED_CPU_KERNEL", "MAX_SYSTEM_NORMALIZED_CPU_NICE", "MAX_SYSTEM_NORMALIZED_CPU_SOFTIRQ", "MAX_SYSTEM_NORMALIZED_CPU_STEAL", "MAX_SYSTEM_NORMALIZED_CPU_USER", "MEMORY_MAPPED", "MEMORY_RESIDENT", "MEMORY_VIRTUAL", "NETWORK_BYTES_IN", "NETWORK_BYTES_OUT", "NETWORK_NUM_REQUESTS", "OP_EXECUTION_TIME_COMMANDS", "OP_EXECUTION_TIME_READS", "OP_EXECUTION_TIME_WRITES", "OPCOUNTER_CMD", "OPCOUNTER_DELETE", "OPCOUNTER_TTL_DELETED", "OPCOUNTER_GETMORE", "OPCOUNTER_INSERT", "OPCOUNTER_QUERY", "OPCOUNTER_REPL_CMD", "OPCOUNTER_REPL_DELETE", "OPCOUNTER_REPL_INSERT", "OPCOUNTER_REPL_UPDATE", "OPCOUNTER_UPDATE", "OPERATIONS_SCAN_AND_ORDER", "OPERATIONS_QUERIES_KILLED", "OPLOG_MASTER_LAG_TIME_DIFF", "OPLOG_MASTER_TIME", "OPLOG_RATE_GB_PER_HOUR", "OPLOG_SLAVE_LAG_MASTER_TIME", "OPLOG_REPLICATION_LAG_TIME", "PROCESS_CPU_CHILDREN_KERNEL", "PROCESS_CPU_CHILDREN_USER", "PROCESS_CPU_KERNEL", "PROCESS_CPU_USER", "PROCESS_NORMALIZED_CPU_CHILDREN_KERNEL", "PROCESS_NORMALIZED_CPU_CHILDREN_USER", "PROCESS_NORMALIZED_CPU_KERNEL", "PROCESS_NORMALIZED_CPU_USER", "QUERY_EXECUTOR_SCANNED", "QUERY_EXECUTOR_SCANNED_OBJECTS", "QUERY_TARGETING_SCANNED_OBJECTS_PER_RETURNED", "QUERY_TARGETING_SCANNED_PER_RETURNED", "RESTARTS_IN_LAST_HOUR", "SWAP_USAGE_FREE", "SWAP_USAGE_USED", "SYSTEM_CPU_GUEST", "SYSTEM_CPU_IOWAIT", "SYSTEM_CPU_IRQ", "SYSTEM_CPU_KERNEL", "SYSTEM_CPU_NICE", "SYSTEM_CPU_SOFTIRQ", "SYSTEM_CPU_STEAL", "SYSTEM_CPU_USER", "SYSTEM_MEMORY_AVAILABLE", "SYSTEM_MEMORY_FREE", "SYSTEM_MEMORY_USED", "SYSTEM_NETWORK_IN", "SYSTEM_NETWORK_OUT", "SYSTEM_NORMALIZED_CPU_GUEST", "SYSTEM_NORMALIZED_CPU_IOWAIT", "SYSTEM_NORMALIZED_CPU_IRQ", "SYSTEM_NORMALIZED_CPU_KERNEL", "SYSTEM_NORMALIZED_CPU_NICE", "SYSTEM_NORMALIZED_CPU_SOFTIRQ", "SYSTEM_NORMALIZED_CPU_STEAL", "SYSTEM_NORMALIZED_CPU_USER", "TICKETS_AVAILABLE_READS", "TICKETS_AVAILABLE_WRITE", "OPERATION_THROTTLING_REJECTED_OPERATIONS", "QUERY_SPILL_TO_DISK_DURING_SORT", "STORAGE_READ_IOPS", "STORAGE_WRITE_IOPS", "STORAGE_READ_LATENCY", "STORAGE_WRITE_LATENCY", "STORAGE_BYTES_READ", "STORAGE_BYTES_WRITTEN", "STORAGE_THROUGHPUT_UTILIZATION", "STORAGE_SPACE_USED", "STORAGE_SPACE_FREE", "STORAGE_SPACE_PERCENT_FREE", "STORAGE_SPACE_PERCENT_USED", "CATALOG_ACTIVE_COLLECTIONS_AND_INDEXES", "QUERY_SPILL_FILE_SPILLED_SIZE", "AVG_MAJORITY_WRITE_CONCERN_WRITE_TIME", "TRANSACTIONS_CURRENT_ACTIVE", "TRANSACTIONS_CURRENT_INACTIVE", "TRANSACTIONS_CURRENT_OPEN", "TRANSACTIONS_ABORTED", "TRANSACTIONS_COMMITTED", "TRANSACTIONS_STARTED", "CACHE_PRESSURE_PERCENTAGE", "INGRESS_QUEUE_WAIT_TIME", "CONNECTION_RATE_LIMITING_OFFERED_CONNECTIONS", "CONNECTION_RATE_LIMITING_SUCCESSFUL_CONNECTIONS", "CONNECTION_RATE_LIMITING_REJECTED_CONNECTIONS", "CONNECTION_RATE_LIMITING_INTERRUPTED_IN_QUEUE", "CONNECTION_RATE_LIMITING_AVERAGE_TIME_QUEUED", "OPERATION_RATE_LIMITING_OFFERED_OPERATIONS", "OPERATION_RATE_LIMITING_SUCCESSFUL_OPERATIONS", "OPERATION_RATE_LIMITING_REJECTED_OPERATIONS", "OPERATION_RATE_LIMITING_QUEUED_OPERATIONS", "OPERATION_RATE_LIMITING_CURRENT_QUEUE_DEPTH", "OPERATION_RATE_LIMITING_QUEUE_TIME_AVG"]] | None = None,
        period: str | None = None,
        pretty: bool | None = None,
        start: datetime | None = None,
    ) -> ApiMeasurementsGeneralViewAtlas:
        """
        Return Measurements for One MongoDB Process

        Returns disk, partition, or host measurements per process for the specified host for the specified project. Returned value can be one of the following:
        - Throughput of I/O operations for the disk partition used for the MongoDB process
        - Percentage of time during which requests the partition issued and serviced
        - Latency per operation type of the disk partition used for the MongoDB process
        - Amount of free and used disk space on the disk partition used for the MongoDB process
        - Measurements for the host, such as CPU usage or number of I/O operations.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            process_id: Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.
            end: Date and time when MongoDB Cloud stops reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            granularity: Duration that specifies the interval at which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC.
            m: One or more types of measurement to request for this MongoDB process. If omitted, the resource returns all measurements. To specify multiple values for `m`, repeat the `m` parameter for each value. Specify measurements that apply to the specified host. MongoDB Cloud returns an error if you specified any invalid measurements.
            period: Duration over which Atlas reports the metrics. This parameter expresses its value in the ISO 8601 duration format in UTC. Include this parameter when you do not set **start** and **end**.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            start: Date and time when MongoDB Cloud begins reporting the metrics. This parameter expresses its value in the ISO 8601 timestamp format in UTC. Include this parameter when you do not set **period**.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/processes/{quote(str(process_id), safe='')}/measurements"
        params = {
            "end": end,
            "envelope": envelope,
            "granularity": granularity,
            "m": m,
            "period": period,
            "pretty": pretty,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiMeasurementsGeneralViewAtlas,
            accept="application/vnd.atlas.2023-01-01+json",
        )
