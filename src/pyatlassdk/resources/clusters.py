"""Generated resource for Clusters. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.adaptive_settings_response import AdaptiveSettingsResponse
from pyatlassdk.models.adaptive_settings_update_request import AdaptiveSettingsUpdateRequest
from pyatlassdk.models.cluster_description20240805 import ClusterDescription20240805
from pyatlassdk.models.cluster_description_auto_scaling_mode_configuration import ClusterDescriptionAutoScalingModeConfiguration
from pyatlassdk.models.cluster_description_process_args20240805 import ClusterDescriptionProcessArgs20240805
from pyatlassdk.models.cluster_status import ClusterStatus
from pyatlassdk.models.employee_access_grant_view import EmployeeAccessGrantView
from pyatlassdk.models.legacy_atlas_cluster import LegacyAtlasCluster
from pyatlassdk.models.legacy_atlas_tenant_cluster_upgrade_request import LegacyAtlasTenantClusterUpgradeRequest
from pyatlassdk.models.paginated_api_atlas_provider_regions_view import PaginatedApiAtlasProviderRegionsView
from pyatlassdk.models.paginated_cluster_description20240805 import PaginatedClusterDescription20240805
from pyatlassdk.models.paginated_org_group_view import PaginatedOrgGroupView
from pyatlassdk.models.pin_fcv_view import PinFCVView
from pyatlassdk.models.sample_dataset_status import SampleDatasetStatus
from pyatlassdk.models.serverless_instance_description import ServerlessInstanceDescription

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class Clusters:
    """Returns, adds, edits, and removes database deployments. Changes to cluster configurations can affect costs. This resource requires your Project ID."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_cluster_details(
        self,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOrgGroupView:
        """
        Return All Authorized Clusters in All Projects

        Returns the details for all clusters in all projects to which you have access. Clusters contain a group of hosts that maintain the same data set. The response does not include multi-cloud clusters.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/api/atlas/v2/clusters"
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
            response_model=PaginatedOrgGroupView,
        )

    def list_group_clusters(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        include_deleted_with_retained_backups: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedClusterDescription20240805:
        """
        Return All Clusters in One Project

        Returns the details for all clusters in the specific project to which you have access. Clusters contain a group of hosts that maintain the same data set. The response includes clusters with asymmetrically-sized shards. This feature is not  available for serverless clusters.

        This endpoint can also be used on Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) endpoint or former M2/M5 clusters that have been migrated to Flex clusters until January 2026. Please use the List Flex Clusters endpoint for Flex clusters instead. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            include_deleted_with_retained_backups: Flag that indicates whether to return Clusters with retain backups.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "includeDeletedWithRetainedBackups": include_deleted_with_retained_backups,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedClusterDescription20240805,
        )

    def create_group_cluster(
        self,
        group_id: str,
        body: ClusterDescription20240805,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterDescription20240805:
        """
        Create One Cluster in One Project

        Creates one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. This resource can create clusters with asymmetrically-sized shards. Each project supports up to 25 database deployments. This feature is not available for serverless clusters.

        Please note that using an `instanceSize` of M2 or M5 will create a Flex cluster instead. Support for the `instanceSize` of M2 or M5 will be discontinued in January 2026. We recommend using the Create Flex Cluster API for such configurations moving forward. Deprecated versions: v2-{2024-08-05}, v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Cluster to create in this project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ClusterDescription20240805,
        )

    def list_group_cluster_provider_regions(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        providers: list[str] | None = None,
        tier: str | None = None,
    ) -> PaginatedApiAtlasProviderRegionsView:
        """
        Return All Cloud Provider Regions

        Returns the list of regions available for the specified cloud provider at the specified tier.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            providers: Cloud providers whose regions to retrieve. When you specify multiple providers, the response can return only tiers and regions that support multi-cloud clusters.
            tier: Cluster tier for which to retrieve the regions.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/provider/regions"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "providers": providers,
            "tier": tier,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiAtlasProviderRegionsView,
        )

    def upgrade_group_cluster_tenant_upgrade(
        self,
        group_id: str,
        body: LegacyAtlasTenantClusterUpgradeRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LegacyAtlasCluster:
        """
        Upgrade One Shared-Tier Cluster

        Upgrades a shared-tier cluster to a Flex or Dedicated (M10+) cluster in the specified project. Each project supports up to 25 clusters. 

        This endpoint can also be used to upgrade Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) API or former M2/M5 clusters that have been migrated to Flex clusters, using `instanceSizeName` to “M2” or “M5” until January 2026. This functionality will be available until January 22, 2026, after which it will only be available for M0 clusters. Please use the Upgrade Flex Cluster endpoint instead.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details of the shared-tier cluster upgrade in the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/tenantUpgrade"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=LegacyAtlasCluster,
        )

    def upgrade_group_cluster_tenant_upgrade_to_serverless(
        self,
        group_id: str,
        body: ServerlessInstanceDescription,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ServerlessInstanceDescription:
        """
        Upgrade One Shared-Tier Cluster to One Serverless Instance

        This endpoint has been deprecated as of February 2025 as we no longer support the creation of new serverless instances. Please use the Upgrade Flex Cluster endpoint to upgrade Flex clusters.

         Upgrades a shared-tier cluster to a serverless instance in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details of the shared-tier cluster upgrade in the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/tenantUpgradeToServerless"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ServerlessInstanceDescription,
        )

    def delete_group_cluster(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        retain_backups: bool | None = None,
    ) -> Any:
        """
        Remove One Cluster from One Project

        Removes one cluster from the specified project. The cluster must have termination protection disabled in order to be deleted. This feature is not available for serverless clusters.

        This endpoint can also be used on Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) endpoint or former M2/M5 clusters that have been migrated to Flex clusters until January 2026. Please use the Delete Flex Cluster endpoint for Flex clusters instead. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            retain_backups: Flag that indicates whether to retain backup snapshots for the deleted dedicated cluster.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "retainBackups": retain_backups,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_cluster(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterDescription20240805:
        """
        Return One Cluster from One Project

        Returns the details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. The response includes clusters with asymmetrically-sized shards. This feature is not available for serverless clusters.

        This endpoint can also be used on Flex clusters that were created using the [Create Cluster](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Clusters/operation/createCluster) endpoint or former M2/M5 clusters that have been migrated to Flex clusters until January 2026. Please use the Get Flex Cluster endpoint for Flex clusters instead. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ClusterDescription20240805,
        )

    def update_group_cluster(
        self,
        cluster_name: str,
        group_id: str,
        body: ClusterDescription20240805,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterDescription20240805:
        """
        Update One Cluster in One Project

        Updates the details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. This resource can update clusters with asymmetrically-sized shards. To update a cluster's termination protection, the requesting Service Account or API Key must have the Project Owner role. For all other updates, the requesting Service Account or API Key must have the Project Cluster Manager role, the Project Cluster Resilience Tester role, or the Project Replica Set Manager role. You can't modify a paused cluster (`paused : true`). You must call this endpoint to set `paused : false`. After this endpoint responds with `paused : false`, you can call it again with the changes you want to make to the cluster. This feature is not available for serverless clusters. Deprecated versions: v2-{2024-08-05}, v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Cluster to update in the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ClusterDescription20240805,
        )

    def get_group_cluster_adaptive_settings(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AdaptiveSettingsResponse:
        """
        Return Adaptive Settings for One Cluster

        Returns the Adaptive Settings for the specified cluster, including client-provided overrides and the effective settings derived from those overrides and Atlas-managed defaults. To use this resource, the requesting Service Account or API Key must have the Project Read Only role.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/adaptiveSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AdaptiveSettingsResponse,
        )

    def update_group_cluster_adaptive_settings(
        self,
        cluster_name: str,
        group_id: str,
        body: AdaptiveSettingsUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AdaptiveSettingsResponse:
        """
        Update Adaptive Settings for One Cluster

        Updates the client-provided Adaptive Settings overrides for the specified cluster and returns the resulting Adaptive Settings, including the effective settings derived from those overrides and Atlas-managed defaults. To use this resource, the requesting Service Account or API Key must have the Project Owner role.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Adaptive Settings overrides to apply to the specified cluster. The supplied `adaptiveSettingsOverrides` map fully replaces the existing overrides: any override omitted from the map returns to its Atlas-managed default. Omitting the `adaptiveSettingsOverrides` field entirely preserves the existing overrides, an empty map clears all overrides, and `null` resets the field and omits it from responses until it is set again.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/adaptiveSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AdaptiveSettingsResponse,
        )

    def auto_group_cluster_scaling_configuration(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterDescriptionAutoScalingModeConfiguration:
        """
        Return Auto Scaling Configuration for One Sharded Cluster

        Returns the internal configuration of AutoScaling for sharded clusters. This endpoint can be used for diagnostic purposes to ensure that sharded clusters updated from older APIs have gained support for AutoScaling each shard independently.

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/autoScalingConfiguration"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ClusterDescriptionAutoScalingModeConfiguration,
        )

    def get_group_cluster_process_args(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterDescriptionProcessArgs20240805:
        """
        Return Advanced Configuration Options for One Cluster

        Returns the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings. This feature isn't available for `M0` free clusters, `M2` and `M5` shared-tier clusters, flex clusters, or serverless clusters. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/processArgs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ClusterDescriptionProcessArgs20240805,
        )

    def update_group_cluster_process_args(
        self,
        cluster_name: str,
        group_id: str,
        body: ClusterDescriptionProcessArgs20240805,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterDescriptionProcessArgs20240805:
        """
        Update Advanced Configuration Options for One Cluster

        Updates the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings. This feature isn't available for `M0` free clusters, `M2` and `M5` shared-tier clusters, flex clusters, or serverless clusters. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Advanced configuration details to add for one cluster in the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/processArgs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ClusterDescriptionProcessArgs20240805,
        )

    def restart_group_cluster_primaries(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Test Failover for One Cluster

        Starts a failover test for the specified cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. A failover test checks how MongoDB Cloud handles the failure of the cluster's primary node. During the test, MongoDB Cloud shuts down the primary node and elects a new primary. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/restartPrimaries"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_cluster_status(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterStatus:
        """
        Return Status of All Cluster Operations

        Returns the status of all changes that you made to the specified cluster in the specified project. Use this resource to check the progress MongoDB Cloud has made in processing your changes. The response does not include the deployment of new dedicated clusters.

        Args:
            cluster_name: Human-readable label that identifies the cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/status"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ClusterStatus,
        )

    def grant_group_cluster_mongo_db_employee_access(
        self,
        cluster_name: str,
        group_id: str,
        body: EmployeeAccessGrantView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Grant MongoDB Employee Cluster Access for One Cluster

        Grants MongoDB employee cluster access for the given duration and at the specified level for one cluster.

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Grant access level and expiration.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}:grantMongoDBEmployeeAccess"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Any,
        )

    def pin_group_cluster_feature_compatibility_version(
        self,
        cluster_name: str,
        group_id: str,
        *,
        body: PinFCVView | None = None,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Pin Feature Compatibility Version for One Cluster in One Project

        Pins the Feature Compatibility Version (FCV) to the current MongoDB version and sets the pin expiration date. If an FCV pin already exists for the cluster, calling this method will only update the expiration date of the existing pin and will not re-pin the FCV.

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Optional request parameters for tuning FCV pinning configuration.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}:pinFeatureCompatibilityVersion"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Any,
        )

    def revoke_group_cluster_mongo_db_employee_access(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Revoke MongoDB Employee Cluster Access for One Cluster

        Revokes a previously granted MongoDB employee cluster access.

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}:revokeMongoDBEmployeeAccess"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
        )

    def unpin_group_cluster_feature_compatibility_version(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Unpin Feature Compatibility Version for One Cluster in One Project

        Unpins the current fixed Feature Compatibility Version (FCV). This feature is not available for clusters on rapid release.

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}:unpinFeatureCompatibilityVersion"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
        )

    def request_group_sample_dataset_load(
        self,
        group_id: str,
        name: str,
        *,
        envelope: bool | None = None,
    ) -> SampleDatasetStatus:
        """
        Load Sample Dataset into One Cluster

        Requests loading the MongoDB sample dataset into the specified cluster.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the cluster into which you load the sample dataset.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/sampleDatasetLoad/{quote(str(name), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=SampleDatasetStatus,
        )

    def get_group_sample_dataset_load(
        self,
        group_id: str,
        sample_dataset_id: str,
        *,
        envelope: bool | None = None,
    ) -> SampleDatasetStatus:
        """
        Return Status of Sample Dataset Load for One Cluster

        Checks the progress of loading the sample dataset into one cluster.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            sample_dataset_id: Unique 24-hexadecimal digit string that identifies the loaded sample dataset.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/sampleDatasetLoad/{quote(str(sample_dataset_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=SampleDatasetStatus,
        )
