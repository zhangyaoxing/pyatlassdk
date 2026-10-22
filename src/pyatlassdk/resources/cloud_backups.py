"""Generated resource for CloudBackups. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.api_atlas_collection_restore_collection_state_response import ApiAtlasCollectionRestoreCollectionStateResponse
from pyatlassdk.models.api_atlas_collection_restore_job_request import ApiAtlasCollectionRestoreJobRequest
from pyatlassdk.models.api_atlas_collection_restore_job_response import ApiAtlasCollectionRestoreJobResponse
from pyatlassdk.models.backup_snapshot_retention import BackupSnapshotRetention
from pyatlassdk.models.data_protection_settings20231001 import DataProtectionSettings20231001
from pyatlassdk.models.disk_backup_collection_response import DiskBackupCollectionResponse
from pyatlassdk.models.disk_backup_database_response import DiskBackupDatabaseResponse
from pyatlassdk.models.disk_backup_export_job import DiskBackupExportJob
from pyatlassdk.models.disk_backup_export_job_request import DiskBackupExportJobRequest
from pyatlassdk.models.disk_backup_on_demand_snapshot_request import DiskBackupOnDemandSnapshotRequest
from pyatlassdk.models.disk_backup_replica_set import DiskBackupReplicaSet
from pyatlassdk.models.disk_backup_sharded_cluster_snapshot import DiskBackupShardedClusterSnapshot
from pyatlassdk.models.disk_backup_snapshot import DiskBackupSnapshot
from pyatlassdk.models.disk_backup_snapshot_aws_export_bucket_response import DiskBackupSnapshotAWSExportBucketResponse
from pyatlassdk.models.disk_backup_snapshot_export_bucket_request import DiskBackupSnapshotExportBucketRequest
from pyatlassdk.models.disk_backup_snapshot_export_bucket_response import DiskBackupSnapshotExportBucketResponse
from pyatlassdk.models.disk_backup_snapshot_restore_job import DiskBackupSnapshotRestoreJob
from pyatlassdk.models.disk_backup_snapshot_schedule20240805 import DiskBackupSnapshotSchedule20240805
from pyatlassdk.models.object_storage_private_endpoint_request import ObjectStoragePrivateEndpointRequest
from pyatlassdk.models.object_storage_private_endpoint_response import ObjectStoragePrivateEndpointResponse
from pyatlassdk.models.paginated_api_atlas_collection_restore_collection_state_view import PaginatedApiAtlasCollectionRestoreCollectionStateView
from pyatlassdk.models.paginated_api_atlas_collection_restore_job_view import PaginatedApiAtlasCollectionRestoreJobView
from pyatlassdk.models.paginated_api_atlas_disk_backup_collection_view import PaginatedApiAtlasDiskBackupCollectionView
from pyatlassdk.models.paginated_api_atlas_disk_backup_database_view import PaginatedApiAtlasDiskBackupDatabaseView
from pyatlassdk.models.paginated_api_atlas_disk_backup_export_job_view import PaginatedApiAtlasDiskBackupExportJobView
from pyatlassdk.models.paginated_api_atlas_object_storage_private_endpoint_response_view import PaginatedApiAtlasObjectStoragePrivateEndpointResponseView
from pyatlassdk.models.paginated_backup_snapshot_export_buckets_view import PaginatedBackupSnapshotExportBucketsView
from pyatlassdk.models.paginated_cloud_backup_replica_set_view import PaginatedCloudBackupReplicaSetView
from pyatlassdk.models.paginated_cloud_backup_restore_job_view import PaginatedCloudBackupRestoreJobView
from pyatlassdk.models.paginated_cloud_backup_sharded_cluster_snapshot_view import PaginatedCloudBackupShardedClusterSnapshotView
from pyatlassdk.models.update_require_private_networking_request_view import UpdateRequirePrivateNetworkingRequestView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class CloudBackups:
    """Manages Cloud Backup snapshots, snapshot export buckets, restore jobs, and schedules. This resource applies only to clusters that use Cloud Backups."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_backup_export_buckets(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedBackupSnapshotExportBucketsView:
        """
        Return All Snapshot Export Buckets

        Returns all Export Buckets associated with the specified Project. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/exportBuckets"
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
            response_model=PaginatedBackupSnapshotExportBucketsView,
        )

    def create_group_backup_export_bucket(
        self,
        group_id: str,
        body: DiskBackupSnapshotExportBucketRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshotExportBucketResponse:
        """
        Create One Snapshot Export Bucket

        Creates a Snapshot Export Bucket for an AWS S3 Bucket, Azure Blob Storage Container, or Google Cloud Storage Bucket. Once created, an snapshots can be exported to the Export Bucket and its referenced AWS S3 Bucket, Azure Blob Storage Container, or Google Cloud Storage Bucket. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Specifies the role and AWS S3 Bucket, Azure Blob Storage Container, or Google Cloud Storage Bucket that the Export Bucket should reference.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/exportBuckets"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupSnapshotExportBucketResponse,
        )

    def delete_group_backup_export_bucket(
        self,
        export_bucket_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Delete One Snapshot Export Bucket

        Deletes an Export Bucket. Auto export must be disabled on all clusters in this Project exporting to this Export Bucket before revoking access.

        Args:
            export_bucket_id: Unique 24-hexadecimal character string that identifies the Export Bucket.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/exportBuckets/{quote(str(export_bucket_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_backup_export_bucket(
        self,
        export_bucket_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> DiskBackupSnapshotExportBucketResponse:
        """
        Return One Snapshot Export Bucket

        Returns one Export Bucket associated with the specified Project. Deprecated versions: v2-{2023-01-01}

        Args:
            export_bucket_id: Unique 24-hexadecimal character string that identifies the Export Bucket.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/exportBuckets/{quote(str(export_bucket_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupSnapshotExportBucketResponse,
        )

    def update_group_backup_export_bucket(
        self,
        export_bucket_id: str,
        group_id: str,
        body: UpdateRequirePrivateNetworkingRequestView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshotAWSExportBucketResponse:
        """
        Update One Export Bucket Private Networking Settings

        Updates the private networking settings for one snapshot export bucket in the specified project.

        Args:
            export_bucket_id: Unique 24-hexadecimal character string that identifies the snapshot export bucket.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the private networking requirement for the snapshot export bucket.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/exportBuckets/{quote(str(export_bucket_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupSnapshotAWSExportBucketResponse,
        )

    def list_group_backup_private_endpoints(
        self,
        cloud_provider: Literal["AWS"],
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasObjectStoragePrivateEndpointResponseView:
        """
        Return Object Storage Private Endpoints for Cloud Backups for One Cloud Provider in One Project

        Returns the private endpoints of the specified cloud provider for object storage backup operations.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider for the private endpoints to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/{quote(str(cloud_provider), safe='')}/privateEndpoints"
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
            response_model=PaginatedApiAtlasObjectStoragePrivateEndpointResponseView,
        )

    def create_group_backup_private_endpoint(
        self,
        cloud_provider: Literal["AWS"],
        group_id: str,
        body: ObjectStoragePrivateEndpointRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ObjectStoragePrivateEndpointResponse:
        """
        Create One Object Storage Private Endpoint for Cloud Backups for One Cloud Provider in One Project

        Creates a private endpoint in the specified region for secure, private connectivity between Atlas and cloud provider object storage services for backup operations.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider for the private endpoint to create.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates a private endpoint in the specified region for object storage backup operations.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/{quote(str(cloud_provider), safe='')}/privateEndpoints"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ObjectStoragePrivateEndpointResponse,
        )

    def delete_group_backup_private_endpoint(
        self,
        cloud_provider: Literal["AWS"],
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Object Storage Private Endpoint for Cloud Backups for One Cloud Provider from One Project

        Deletes one private endpoint, identified by its ID, for object storage backup operations.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider of the private endpoint to delete.
            endpoint_id: Unique 24-hexadecimal digit string that identifies the private endpoint to delete.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/{quote(str(cloud_provider), safe='')}/privateEndpoints/{quote(str(endpoint_id), safe='')}"
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

    def get_group_backup_private_endpoint(
        self,
        cloud_provider: Literal["AWS"],
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ObjectStoragePrivateEndpointResponse:
        """
        Return One Object Storage Private Endpoint for Cloud Backups for One Cloud Provider in One Project

        Returns one private endpoint, identified by its ID, for object storage backup operations.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider of the private endpoint.
            endpoint_id: Unique 24-hexadecimal digit string that identifies the private endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backup/{quote(str(cloud_provider), safe='')}/privateEndpoints/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ObjectStoragePrivateEndpointResponse,
        )

    def disable_group_backup_compliance_policy(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Disable Backup Compliance Policy Settings

        Disables the Backup Compliance Policy settings with the specified project. As a prerequisite, a support ticket needs to be file first, instructions in https://www.mongodb.com/docs/atlas/backup/cloud-backup/backup-compliance-policy/.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backupCompliancePolicy"
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

    def get_group_backup_compliance_policy(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DataProtectionSettings20231001:
        """
        Return Backup Compliance Policy Settings

        Returns the Backup Compliance Policy settings with the specified project. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backupCompliancePolicy"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DataProtectionSettings20231001,
        )

    def update_group_backup_compliance_policy(
        self,
        group_id: str,
        body: DataProtectionSettings20231001,
        *,
        envelope: bool | None = None,
        overwrite_backup_policies: bool | None = None,
        pretty: bool | None = None,
    ) -> DataProtectionSettings20231001:
        """
        Update Backup Compliance Policy Settings

        Updates the Backup Compliance Policy settings for the specified project. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            overwrite_backup_policies: Flag that indicates whether to overwrite non complying backup policies with the new data protection settings or not.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The new Backup Compliance Policy settings.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/backupCompliancePolicy"
        params = {
            "envelope": envelope,
            "overwriteBackupPolicies": overwrite_backup_policies,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=DataProtectionSettings20231001,
        )

    def list_group_cluster_backup_exports(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasDiskBackupExportJobView:
        """
        Return All Snapshot Export Jobs

        Returns all Cloud Backup Snapshot Export Jobs associated with the specified Atlas cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/exports"
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
            response_model=PaginatedApiAtlasDiskBackupExportJobView,
        )

    def create_group_cluster_backup_export(
        self,
        cluster_name: str,
        group_id: str,
        body: DiskBackupExportJobRequest,
        *,
        envelope: bool | None = None,
    ) -> DiskBackupExportJob:
        """
        Create One Snapshot Export Job

        Exports one backup Snapshot for dedicated Atlas cluster using Cloud Backups to an Export Bucket.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Information about the Cloud Backup Snapshot Export Job to create.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/exports"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupExportJob,
        )

    def get_group_cluster_backup_export(
        self,
        cluster_name: str,
        export_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> DiskBackupExportJob:
        """
        Return One Snapshot Export Job

        Returns one Cloud Backup Snapshot Export Job associated with the specified Atlas cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            export_id: Unique 24-hexadecimal character string that identifies the Export Job.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/exports/{quote(str(export_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupExportJob,
        )

    def list_group_cluster_backup_restore_jobs(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedCloudBackupRestoreJobView:
        """
        Return All Restore Jobs for One Cluster

        Returns all cloud backup restore jobs for one cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the restore jobs you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/restoreJobs"
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
            response_model=PaginatedCloudBackupRestoreJobView,
        )

    def create_group_cluster_backup_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        body: DiskBackupSnapshotRestoreJob,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshotRestoreJob:
        """
        Create One Restore Job of One Cluster

        Restores one snapshot of one cluster from the specified project. Atlas takes on-demand snapshots immediately and scheduled snapshots at regular intervals. If an on-demand snapshot with a status of `queued` or `inProgress` exists, before taking another snapshot, wait until Atlas completes processing the previously taken on-demand snapshot.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Restores one snapshot of one cluster from the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/restoreJobs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupSnapshotRestoreJob,
        )

    def cancel_group_cluster_backup_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        restore_job_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Cancel One Restore Job for One Cluster

        Cancels one cloud backup restore job of one cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            restore_job_id: Unique 24-hexadecimal digit string that identifies the restore job to remove.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/restoreJobs/{quote(str(restore_job_id), safe='')}"
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

    def get_group_cluster_backup_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        restore_job_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshotRestoreJob:
        """
        Return One Restore Job for One Cluster

        Returns one cloud backup restore job for one cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the restore jobs you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            restore_job_id: Unique 24-hexadecimal digit string that identifies the restore job to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/restoreJobs/{quote(str(restore_job_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupSnapshotRestoreJob,
        )

    def delete_group_cluster_backup_schedule(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> DiskBackupSnapshotSchedule20240805:
        """
        Remove All Cloud Backup Schedules

        Removes all cloud backup schedules for the specified cluster. This schedule defines when MongoDB Cloud takes scheduled snapshots and how long it stores those snapshots. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/schedule"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=DiskBackupSnapshotSchedule20240805,
        )

    def get_group_cluster_backup_schedule(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshotSchedule20240805:
        """
        Return One Cloud Backup Schedule

        Returns the cloud backup schedule for the specified cluster within the specified project. This schedule defines when MongoDB Cloud takes scheduled snapshots and how long it stores those snapshots. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/schedule"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupSnapshotSchedule20240805,
        )

    def update_group_cluster_backup_schedule(
        self,
        cluster_name: str,
        group_id: str,
        body: DiskBackupSnapshotSchedule20240805,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshotSchedule20240805:
        """
        Update Cloud Backup Schedule for One Cluster

        Updates the cloud backup schedule for one cluster within the specified project. This schedule defines when MongoDB Cloud takes scheduled snapshots and how long it stores those snapshots. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the cloud backup schedule for one cluster within the specified project. **Note**: In the request body, provide only the fields that you want to update.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/schedule"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupSnapshotSchedule20240805,
        )

    def list_group_cluster_backup_snapshots(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        oplog_inc: int | None = None,
        oplog_ts: int | None = None,
        page_num: int | None = None,
        point_in_time_utc_seconds: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedCloudBackupReplicaSetView:
        """
        Return All Replica Set Cloud Backups

        Returns all snapshots of one cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            oplog_inc: Oplog operation number that represents the desired point in time. This is the second part of an Oplog timestamp. Must be used with `oplogTs`. Mutually exclusive with `pointInTimeUtcSeconds`.
            oplog_ts: Oplog timestamp that represents the desired point in time. This is the first part of an Oplog timestamp. Must be used with `oplogInc`. Mutually exclusive with `pointInTimeUtcSeconds`.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            point_in_time_utc_seconds: Desired point in time, expressed as the number of seconds that have elapsed since the UNIX epoch. If specified, returns the closest snapshot created before that point in time. Mutually exclusive with `oplogTs` and `oplogInc`.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "oplogInc": oplog_inc,
            "oplogTs": oplog_ts,
            "pageNum": page_num,
            "pointInTimeUtcSeconds": point_in_time_utc_seconds,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedCloudBackupReplicaSetView,
        )

    def take_group_cluster_backup_snapshots(
        self,
        cluster_name: str,
        group_id: str,
        body: DiskBackupOnDemandSnapshotRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupSnapshot:
        """
        Take One On-Demand Snapshot

        Takes one on-demand snapshot for the specified cluster. Atlas takes on-demand snapshots immediately and scheduled snapshots at regular intervals. If an on-demand snapshot with a status of `queued` or `inProgress` exists, before taking another snapshot, wait until Atlas completes processing the previously taken on-demand snapshot.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Takes one on-demand snapshot.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupSnapshot,
        )

    def delete_group_cluster_backup_snapshot_sharded_cluster(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Sharded Cluster Cloud Backup

        Removes one snapshot of one sharded cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/shardedCluster/{quote(str(snapshot_id), safe='')}"
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

    def get_group_cluster_backup_snapshot_sharded_cluster(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupShardedClusterSnapshot:
        """
        Return One Sharded Cluster Cloud Backup

        Returns one snapshot of one sharded cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/shardedCluster/{quote(str(snapshot_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupShardedClusterSnapshot,
        )

    def list_group_cluster_backup_snapshot_sharded_clusters(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedCloudBackupShardedClusterSnapshotView:
        """
        Return All Sharded Cluster Cloud Backups

        Returns all snapshots of one sharded cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/shardedClusters"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedCloudBackupShardedClusterSnapshotView,
        )

    def delete_group_cluster_backup_snapshot(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Replica Set Cloud Backup

        Removes the specified snapshot.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}"
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

    def get_group_cluster_backup_snapshot(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupReplicaSet:
        """
        Return One Replica Set Cloud Backup

        Returns one snapshot from the specified cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupReplicaSet,
        )

    def update_group_cluster_backup_snapshot(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        body: BackupSnapshotRetention,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupReplicaSet:
        """
        Update Expiration Date for One Cloud Backup

        Changes the expiration date for one cloud backup snapshot for one cluster in the specified project, the requesting Service Account or API Key must have the Project Backup Manager role.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Changes the expiration date for one cloud backup snapshot for one cluster in the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=DiskBackupReplicaSet,
        )

    def list_group_cluster_backup_snapshot_databases(
        self,
        cluster_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasDiskBackupDatabaseView:
        """
        Return Databases in One Snapshot

        Returns the list of databases that exist in the specified snapshot. Use this to discover namespaces before creating a collection restore job.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}/databases"
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
            response_model=PaginatedApiAtlasDiskBackupDatabaseView,
        )

    def get_group_cluster_backup_snapshot_database(
        self,
        cluster_name: str,
        database_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupDatabaseResponse:
        """
        Return One Database in One Snapshot

        Returns one database that exists in the specified snapshot. Use this to confirm a known database exists before referencing it in a collection restore job.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}/databases/{quote(str(database_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupDatabaseResponse,
        )

    def list_group_cluster_backup_snapshot_database_collections(
        self,
        cluster_name: str,
        database_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasDiskBackupCollectionView:
        """
        Return Collections in One Database in One Snapshot

        Returns the list of collections in the specified database that exist in the snapshot. Use this to discover namespaces before creating a collection restore job.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}/databases/{quote(str(database_name), safe='')}/collections"
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
            response_model=PaginatedApiAtlasDiskBackupCollectionView,
        )

    def get_group_cluster_backup_snapshot_database_collection(
        self,
        cluster_name: str,
        collection_name: str,
        database_name: str,
        group_id: str,
        snapshot_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DiskBackupCollectionResponse:
        """
        Return One Collection in One Database in One Snapshot

        Returns one collection that exists in the specified database in the snapshot. Use this to confirm a known collection exists before referencing it in a collection restore job.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            collection_name: Human-readable label that identifies the collection.
            database_name: Human-readable label that identifies the database.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            snapshot_id: Unique 24-hexadecimal digit string that identifies the desired snapshot.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/backup/snapshots/{quote(str(snapshot_id), safe='')}/databases/{quote(str(database_name), safe='')}/collections/{quote(str(collection_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DiskBackupCollectionResponse,
        )

    def list_group_cluster_collection_restore_jobs(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasCollectionRestoreJobView:
        """
        Return All Collection Restore Jobs for One Cluster

        Returns all collection restore jobs for one cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the collection restore jobs you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collectionRestoreJobs"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiAtlasCollectionRestoreJobView,
        )

    def create_group_cluster_collection_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        body: ApiAtlasCollectionRestoreJobRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasCollectionRestoreJobResponse:
        """
        Create One Collection Restore Job

        Creates one collection-level restore job for one cluster from the specified project. Collection-level restores allow restoring specific databases or collections from a snapshot or point-in-time.

        Args:
            cluster_name: Human-readable label that identifies the source cluster for the restore.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one collection-level restore job for one cluster from the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collectionRestoreJobs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ApiAtlasCollectionRestoreJobResponse,
        )

    def get_group_cluster_collection_restore_job(
        self,
        cluster_name: str,
        group_id: str,
        job_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasCollectionRestoreJobResponse:
        """
        Return One Collection Restore Job for One Cluster

        Returns one collection restore job for one cluster from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the collection restore jobs you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            job_id: Unique 24-hexadecimal digit string that identifies the collection restore job to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collectionRestoreJobs/{quote(str(job_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiAtlasCollectionRestoreJobResponse,
        )

    def list_group_cluster_collection_restore_job_collections(
        self,
        cluster_name: str,
        group_id: str,
        job_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        source_namespace: str | None = None,
        state: Literal["NOT_STARTED", "IN_PROGRESS", "FINALIZING", "NOT_FOUND", "UNSUPPORTED", "SUCCESSFUL", "ROLLBACK", "NOT_RESTORED", "FAILED"] | None = None,
        target_namespace: str | None = None,
    ) -> PaginatedApiAtlasCollectionRestoreCollectionStateView:
        """
        Return All Collection States for One Collection Restore Job

        Returns all collection-level restore states for one collection restore job from the specified project. Note: If the restore job is in the INITIALIZING state, this endpoint returns an empty list because collection-level states have not yet been created.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the collection restore job you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            job_id: Unique 24-hexadecimal digit string that identifies the collection restore job.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            source_namespace: Source namespace to filter by (e.g. `db.collection`).
            state: Collection-level state to filter by.
            target_namespace: Target namespace to filter by (e.g. `db.collection`).
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collectionRestoreJobs/{quote(str(job_id), safe='')}/collections"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "sourceNamespace": source_namespace,
            "state": state,
            "targetNamespace": target_namespace,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiAtlasCollectionRestoreCollectionStateView,
        )

    def get_group_cluster_collection_restore_job_collection(
        self,
        cluster_name: str,
        group_id: str,
        job_id: str,
        source_namespace: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasCollectionRestoreCollectionStateResponse:
        """
        Return One Collection State for One Collection Restore Job

        Returns one collection-level restore state for one collection restore job from the specified project.

        Args:
            cluster_name: Human-readable label that identifies the cluster with the collection restore job you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            job_id: Unique 24-hexadecimal digit string that identifies the collection restore job.
            source_namespace: Source namespace that identifies the collection to return (e.g. `db.collection`).
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/collectionRestoreJobs/{quote(str(job_id), safe='')}/collections/{quote(str(source_namespace), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiAtlasCollectionRestoreCollectionStateResponse,
        )
