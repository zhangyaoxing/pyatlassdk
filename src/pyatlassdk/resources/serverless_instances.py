"""Generated resource for ServerlessInstances. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.paginated_serverless_instance_description_view import PaginatedServerlessInstanceDescriptionView
from pyatlassdk.models.serverless_instance_description import ServerlessInstanceDescription

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ServerlessInstances:
    """Returns, adds, edits, and removes serverless instances."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_serverless_instances(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedServerlessInstanceDescriptionView:
        """
        Return All Serverless Instances in One Project

        Returns details for all serverless instances in the specified project.

        This endpoint also lists Flex clusters that were created using the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or former Serverless instances that have been migrated to Flex clusters, until January 15, 2026 after which this endpoint will begin returning an empty list. The endpoint will be removed entirely on January 15, 2027. Continuous backups are not supported and `serverlessContinuousBackupEnabled` will not take effect on these clusters. Please use the List Flex Clusters endpoint instead.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serverless"
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
            response_model=PaginatedServerlessInstanceDescriptionView,
        )

    def get_group_serverless_instance(
        self,
        group_id: str,
        name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ServerlessInstanceDescription:
        """
        Return One Serverless Instance from One Project

        Returns details for one serverless instance in the specified project.

        This API can also be used on Flex clusters that were created with the [Create Serverless Instance](https://www.mongodb.com/docs/atlas/reference/api-resources-spec/v2/#tag/Serverless-Instances/operation/createServerlessInstance) endpoint or Flex clusters that were migrated from Serverless instances. Continuous backups are not supported and `serverlessContinuousBackupEnabled` will not take effect on these clusters. This endpoint will be sunset on January 15, 2027. Please use the Get Flex Cluster endpoint instead.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            name: Human-readable label that identifies the serverless instance.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serverless/{quote(str(name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ServerlessInstanceDescription,
        )
