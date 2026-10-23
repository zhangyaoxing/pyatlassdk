"""Generated resource for FlexSnapshots. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.flex_backup_restore_job20241113 import FlexBackupRestoreJob20241113
from pyatlassdk.models.flex_backup_snapshot20241113 import FlexBackupSnapshot20241113
from pyatlassdk.models.flex_backup_snapshot_download_create20241113 import FlexBackupSnapshotDownloadCreate20241113
from pyatlassdk.models.paginated_api_atlas_flex_backup_snapshot20241113_view import PaginatedApiAtlasFlexBackupSnapshot20241113View

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class FlexSnapshots:
    """Returns and requests to download flex database deployment snapshots."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def download_group_flex_cluster_backup(
        self,
        group_id: str,
        name: str,
        body: FlexBackupSnapshotDownloadCreate20241113,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexBackupRestoreJob20241113:
        """
        Download One Flex Cluster Snapshot

        Requests one snapshot for the specified flex cluster. This resource returns a `snapshotURL` that you can use to download the snapshot. This `snapshotURL` remains active for four hours after you make the request.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Snapshot to be downloaded.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}/backup/download"
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
            accept="application/vnd.atlas.2024-11-13+json",
            content_type="application/vnd.atlas.2024-11-13+json",
        )

    def list_group_flex_cluster_backup_snapshots(
        self,
        group_id: str,
        name: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasFlexBackupSnapshot20241113View:
        """
        Return All Snapshots for One Flex Cluster

        Returns all snapshots of one flex cluster from the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}/backup/snapshots"
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
            response_model=PaginatedApiAtlasFlexBackupSnapshot20241113View,
            accept="application/vnd.atlas.2024-11-13+json",
        )

    def get_group_flex_cluster_backup_snapshot(
        self,
        group_id: str,
        name: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
    ) -> FlexBackupSnapshot20241113:
        """
        Return One Snapshot for One Flex Cluster

        Returns one snapshot of one flex cluster from the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=FlexBackupSnapshot20241113,
            accept="application/vnd.atlas.2024-11-13+json",
        )
