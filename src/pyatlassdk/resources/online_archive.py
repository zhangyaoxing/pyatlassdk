"""Generated resource for OnlineArchive. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.backup_online_archive import BackupOnlineArchive
from pyatlassdk.models.backup_online_archive_create import BackupOnlineArchiveCreate
from pyatlassdk.models.paginated_online_archive_view import PaginatedOnlineArchiveView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class OnlineArchive:
    """Returns, adds, edits, or removes an online archive."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_cluster_online_archives(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOnlineArchiveView:
        """
        Return All Online Archives for One Cluster

        Returns details of all online archives. This archive stores data from one cluster within one project.

        Args:
            cluster_name: Human-readable label that identifies the cluster that contains the collection for which you want to return the online archives.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/onlineArchives"
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
            response_model=PaginatedOnlineArchiveView,
        )

    def create_group_cluster_online_archive(
        self,
        cluster_name: str,
        group_id: str,
        body: BackupOnlineArchiveCreate,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BackupOnlineArchive:
        """
        Create One Online Archive

        Creates one online archive. This archive stores data from one cluster within one project.

        Args:
            cluster_name: Human-readable label that identifies the cluster that contains the collection for which you want to create one online archive.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one online archive.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/onlineArchives"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=BackupOnlineArchive,
        )

    def download_group_cluster_online_archive_query_logs(
        self,
        cluster_name: str,
        group_id: str,
        *,
        archive_only: bool | None = None,
        end_date: int | None = None,
        envelope: bool | None = None,
        start_date: int | None = None,
    ) -> str:
        """
        Download Online Archive Query Logs

        Downloads query logs for the specified online archive. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`.

        Args:
            cluster_name: Human-readable label that identifies the cluster that contains the collection for which you want to return the query logs from one online archive.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            archive_only: Flag that indicates whether to download logs for queries against your online archive only or both your online archive and cluster.
            end_date: Date and time that specifies the end point for the range of log messages to return. This resource expresses this value in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            start_date: Date and time that specifies the starting point for the range of log messages to return. This resource expresses this value in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/onlineArchives/queryLogs.gz"
        params = {
            "archiveOnly": archive_only,
            "endDate": end_date,
            "envelope": envelope,
            "startDate": start_date,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=str,
        )

    def delete_group_cluster_online_archive(
        self,
        archive_id: str,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Online Archive

        Removes one online archive. This archive stores data from one cluster within one project.

        Args:
            archive_id: Unique 24-hexadecimal digit string that identifies the online archive to delete.
            cluster_name: Human-readable label that identifies the cluster that contains the collection from which you want to remove an online archive.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/onlineArchives/{quote(str(archive_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_cluster_online_archive(
        self,
        archive_id: str,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BackupOnlineArchive:
        """
        Return One Online Archive

        Returns one online archive for one cluster. This archive stores data from one cluster within one project.

        Args:
            archive_id: Unique 24-hexadecimal digit string that identifies the online archive to return.
            cluster_name: Human-readable label that identifies the cluster that contains the specified collection from which Application created the online archive.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/onlineArchives/{quote(str(archive_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=BackupOnlineArchive,
        )

    def update_group_cluster_online_archive(
        self,
        archive_id: str,
        cluster_name: str,
        group_id: str,
        body: BackupOnlineArchive,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BackupOnlineArchive:
        """
        Update One Online Archive

        Updates, pauses, or resumes one online archive. This archive stores data from one cluster within one project.

        Args:
            archive_id: Unique 24-hexadecimal digit string that identifies the online archive to update.
            cluster_name: Human-readable label that identifies the cluster that contains the specified collection from which Application created the online archive.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates, pauses, or resumes one online archive.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/onlineArchives/{quote(str(archive_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=BackupOnlineArchive,
        )
