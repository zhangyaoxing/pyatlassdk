"""Generated resource for LegacyBackup. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.api_atlas_checkpoint_view import ApiAtlasCheckpointView
from pyatlassdk.models.api_atlas_snapshot_schedule_view import ApiAtlasSnapshotScheduleView
from pyatlassdk.models.backup_restore_job import BackupRestoreJob
from pyatlassdk.models.backup_snapshot import BackupSnapshot
from pyatlassdk.models.paginated_api_atlas_checkpoint_view import PaginatedApiAtlasCheckpointView
from pyatlassdk.models.paginated_restore_job_view import PaginatedRestoreJobView
from pyatlassdk.models.paginated_snapshot_view import PaginatedSnapshotView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class LegacyBackup:
    """Manages Legacy Backup snapshots, restore jobs, schedules and checkpoints."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_cluster_backup_checkpoints(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasCheckpointView:
        """
        Return All Legacy Backup Checkpoints

        Returns all legacy backup checkpoints for one cluster in the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster that contains the checkpoints that you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backupCheckpoints"
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
            response_model=PaginatedApiAtlasCheckpointView,
        )

    def get_group_cluster_backup_checkpoint(
        self,
        checkpoint_id: str,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasCheckpointView:
        """
        Return One Legacy Backup Checkpoint

        Returns one legacy backup checkpoint for one cluster in the specified project.

        Args:
            checkpoint_id: Unique 24-hexadecimal digit string that identifies the checkpoint.
            cluster_name: Human-readable label that identifies the cluster that contains the checkpoints that you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backupCheckpoints/{quote(str(checkpoint_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiAtlasCheckpointView,
        )

    def list_group_cluster_restore_jobs(
        self,
        cluster_name: str,
        group_id: str,
        *,
        batch_id: str | None = None,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedRestoreJobView:
        """
        Return All Legacy Backup Restore Jobs

        Returns all legacy backup restore jobs for one cluster in the specified project.

         Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation. If you use the `BATCH-ID` query parameter, you can retrieve all restore jobs in the specified batch. When creating a restore job for a sharded cluster, MongoDB Cloud creates a separate job for each shard, plus another for the config server. Each of those jobs are part of a batch. However, a batch can't include a restore job for a replica set.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the snapshot you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            batch_id: Unique 24-hexadecimal digit string that identifies the batch of restore jobs to return. Timestamp in ISO 8601 date and time format in UTC when creating a restore job for a sharded cluster, Application creates a separate job for each shard, plus another for the config host. Each of these jobs comprise one batch. A restore job for a replica set can't be part of a batch.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/restoreJobs"
        params = {
            "batchId": batch_id,
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
            response_model=PaginatedRestoreJobView,
        )

    def create_group_cluster_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        body: BackupRestoreJob,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedRestoreJobView:
        """
        Create One Legacy Backup Restore Job

        Restores one legacy backup for one cluster in the specified project. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation. This endpoint doesn't support creating checkpoint restore jobs for sharded clusters, or creating restore jobs for queryable backup snapshots. If you create an automated restore job by specifying `delivery.methodName` of `AUTOMATED_RESTORE` in your request body, MongoDB Cloud removes all existing data on the target cluster prior to the restore.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the snapshot you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Legacy backup to restore to one cluster in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/restoreJobs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedRestoreJobView,
        )

    def get_group_cluster_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        job_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BackupRestoreJob:
        """
        Return One Legacy Backup Restore Job

        Returns one legacy backup restore job for one cluster in the specified project.

         Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the snapshot you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            job_id: Unique 24-hexadecimal digit string that identifies the restore job.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/restoreJobs/{quote(str(job_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=BackupRestoreJob,
        )

    def get_group_cluster_snapshot_schedule(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasSnapshotScheduleView:
        """
        Return One Snapshot Schedule

        Returns the snapshot schedule for one cluster in the specified project.

         Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the snapshot you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/snapshotSchedule"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiAtlasSnapshotScheduleView,
        )

    def update_group_cluster_snapshot_schedule(
        self,
        cluster_name: str,
        group_id: str,
        body: ApiAtlasSnapshotScheduleView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasSnapshotScheduleView:
        """
        Update Snapshot Schedule for One Cluster

        Updates the snapshot schedule for one cluster in the specified project.

         Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the snapshot you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Update the snapshot schedule for one cluster in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/snapshotSchedule"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ApiAtlasSnapshotScheduleView,
        )

    def list_group_cluster_snapshots(
        self,
        cluster_name: str,
        group_id: str,
        *,
        completed: Literal["all", "true", "false"] | None = None,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedSnapshotView:
        """
        Return All Legacy Backup Snapshots

        Returns all legacy backup snapshots for one cluster in the specified project. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            completed: Human-readable label that specifies whether to return only completed, incomplete, or all snapshots. By default, MongoDB Cloud only returns completed snapshots.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/snapshots"
        params = {
            "completed": completed,
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
            response_model=PaginatedSnapshotView,
        )

    def delete_group_cluster_snapshot(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Legacy Backup Snapshot

        Removes one legacy backup snapshot for one cluster in the specified project. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/snapshots/{quote(str(snapshot_id), safe='')}"
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

    def get_group_cluster_snapshot(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BackupSnapshot:
        """
        Return One Legacy Backup Snapshot

        Returns one legacy backup snapshot for one cluster in the specified project. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/snapshots/{quote(str(snapshot_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=BackupSnapshot,
        )

    def update_group_cluster_snapshot(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        body: BackupSnapshot,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BackupSnapshot:
        """
        Update Expiration Date for One Legacy Backup Snapshot

        Changes the expiration date for one legacy backup snapshot for one cluster in the specified project. Effective 23 March 2020, all new clusters can use only Cloud Backups. When you upgrade to 4.2, your backup system upgrades to cloud backup if it is currently set to legacy backup. After this upgrade, all your existing legacy backup snapshots remain available. They expire over time in accordance with your retention policy. Your backup policy resets to the default schedule. If you had a custom backup policy in place with legacy backups, you must re-create it with the procedure outlined in the Cloud Backup documentation.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Changes One Legacy Backup Snapshot Expiration.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/snapshots/{quote(str(snapshot_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=BackupSnapshot,
        )
