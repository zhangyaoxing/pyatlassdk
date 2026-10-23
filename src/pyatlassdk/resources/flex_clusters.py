"""Generated resource for FlexClusters. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.atlas_tenant_cluster_upgrade_request20240805 import AtlasTenantClusterUpgradeRequest20240805
from pyatlassdk.models.flex_cluster_description20241113 import FlexClusterDescription20241113
from pyatlassdk.models.flex_cluster_description_create20241113 import FlexClusterDescriptionCreate20241113
from pyatlassdk.models.flex_cluster_description_update20241113 import FlexClusterDescriptionUpdate20241113
from pyatlassdk.models.paginated_flex_clusters20241113 import PaginatedFlexClusters20241113

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class FlexClusters:
    """Returns, adds, edits, and removes flex clusters."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_flex_clusters(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedFlexClusters20241113:
        """
        Return All Flex Clusters from One Project

        Returns details for all flex clusters in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters"
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
            response_model=PaginatedFlexClusters20241113,
        )

    def create_group_flex_cluster(
        self,
        group_id: str,
        body: FlexClusterDescriptionCreate20241113,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexClusterDescription20241113:
        """
        Create One Flex Cluster in One Project

        Creates one flex cluster in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Create One Flex Cluster in One Project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=FlexClusterDescription20241113,
        )

    def delete_group_flex_cluster(
        self,
        group_id: str,
        name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Flex Cluster from One Project

        Removes one flex cluster from the specified project. The flex cluster must have termination protection disabled in order to be deleted.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}"
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

    def get_group_flex_cluster(
        self,
        group_id: str,
        name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexClusterDescription20241113:
        """
        Return One Flex Cluster from One Project

        Returns details for one flex cluster in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=FlexClusterDescription20241113,
        )

    def update_group_flex_cluster(
        self,
        group_id: str,
        name: str,
        body: FlexClusterDescriptionUpdate20241113,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexClusterDescription20241113:
        """
        Update One Flex Cluster in One Project

        Updates one flex cluster in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the flex cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Update One Flex Cluster in One Project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters/{quote(str(name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=FlexClusterDescription20241113,
        )

    def tenant_group_flex_cluster_upgrade(
        self,
        group_id: str,
        body: AtlasTenantClusterUpgradeRequest20240805,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> FlexClusterDescription20241113:
        """
        Upgrade One Flex Cluster

        Upgrades a flex cluster to a dedicated cluster (M10+) in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details of the flex cluster upgrade in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/flexClusters:tenantUpgrade"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=FlexClusterDescription20241113,
        )
