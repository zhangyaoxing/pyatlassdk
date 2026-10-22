"""Generated resource for FlexRestoreJobs. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.flex_backup_restore_job20241113 import FlexBackupRestoreJob20241113
from pyatlassdk.models.flex_backup_restore_job_create20241113 import FlexBackupRestoreJobCreate20241113
from pyatlassdk.models.paginated_api_atlas_flex_backup_restore_job20241113_view import PaginatedApiAtlasFlexBackupRestoreJob20241113View

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class FlexRestoreJobs:
    """Returns and adds restore jobs for flex database deployments."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_flex_cluster_backup_restore_jobs(
        self,
        group_id: str,
        name: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasFlexBackupRestoreJob20241113View:
        """
        Return All Restore Jobs for One Flex Cluster

        Returns all restore jobs for one flex cluster from the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}/backup/restoreJobs"
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
            response_model=PaginatedApiAtlasFlexBackupRestoreJob20241113View,
        )

    def create_group_flex_cluster_backup_restore_job(
        self,
        group_id: str,
        name: str,
        body: FlexBackupRestoreJobCreate20241113,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexBackupRestoreJob20241113:
        """
        Create One Restore Job for One Flex Cluster

        Restores one snapshot of one flex cluster from the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster whose snapshot you want to restore.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Restores one snapshot of one flex cluster from the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}/backup/restoreJobs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=FlexBackupRestoreJob20241113,
        )

    def get_group_flex_cluster_backup_restore_job(
        self,
        group_id: str,
        name: str,
        restore_job_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexBackupRestoreJob20241113:
        """
        Return One Restore Job for One Flex Cluster

        Returns one restore job for one flex cluster from the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            restore_job_id: Unique 24-hexadecimal digit string that identifies the restore job to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}/backup/restoreJobs/{quote(str(restore_job_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=FlexBackupRestoreJob20241113,
        )
