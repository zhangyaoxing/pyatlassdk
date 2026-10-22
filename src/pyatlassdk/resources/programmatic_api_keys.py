"""Generated resource for ProgrammaticAPIKeys. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.api_key_user_details import ApiKeyUserDetails
from pyatlassdk.models.create_atlas_organization_api_key import CreateAtlasOrganizationApiKey
from pyatlassdk.models.create_atlas_project_api_key import CreateAtlasProjectApiKey
from pyatlassdk.models.paginated_api_api_user_view import PaginatedApiApiUserView
from pyatlassdk.models.paginated_api_user_access_list_response_view import PaginatedApiUserAccessListResponseView
from pyatlassdk.models.update_atlas_organization_api_key import UpdateAtlasOrganizationApiKey
from pyatlassdk.models.update_atlas_project_api_key import UpdateAtlasProjectApiKey
from pyatlassdk.models.user_access_list_request import UserAccessListRequest
from pyatlassdk.models.user_access_list_response import UserAccessListResponse
from pyatlassdk.models.user_access_role_assignment import UserAccessRoleAssignment

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ProgrammaticAPIKeys:
    """Returns, adds, edits, and removes access tokens to use the MongoDB Cloud API. MongoDB Cloud applies these keys to organizations. These resources can return, assign, or revoke use of these keys within a specified project."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_api_keys(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiApiUserView:
        """
        Return All Organization API Keys Assigned to One Project

        Returns all organization API keys that you assigned to the specified project. Users with the Project Owner role in the project associated with the API key can use the organization API key to access the resources.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/apiKeys"
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
            response_model=PaginatedApiApiUserView,
        )

    def create_group_api_key(
        self,
        group_id: str,
        body: CreateAtlasProjectApiKey,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiKeyUserDetails:
        """
        Create and Assign One Organization API Key to One Project

        Creates and assigns the specified organization API key to the specified project. Users with the Project Owner role in the project associated with the API key can use the organization API key to access the resources.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization API key to be created and assigned to the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/apiKeys"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ApiKeyUserDetails,
        )

    def remove_group_api_key(
        self,
        api_user_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Unassign One Organization API Key from One Project

        Removes one organization API key from the specified project.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key that you want to unassign from one project.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}"
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

    def update_group_api_key_roles(
        self,
        api_user_id: str,
        group_id: str,
        body: UpdateAtlasProjectApiKey,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> ApiKeyUserDetails:
        """
        Update Organization API Key Roles for One Project

        Updates the roles of the organization API key that you specify for the project that you specify. You must specify at least one valid role for the project. The application removes any roles that you do not include in this request if they were previously set in the organization API key that you specify for the project.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key that you want to unassign from one project.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization API Key to be updated. This request requires a minimum of one of the two body parameters.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ApiKeyUserDetails,
        )

    def add_group_api_key(
        self,
        api_user_id: str,
        group_id: str,
        body: list[UserAccessRoleAssignment],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Assign One Organization API Key to One Project

        Assigns the specified organization API key to the specified project. Users with the Project Owner role in the project associated with the API key can then use the organization API key to access the resources.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key that you want to assign to one project.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization API key to be assigned to the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}"
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

    def list_org_api_keys(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiApiUserView:
        """
        Return All Organization API Keys

        Returns all organization API keys for the specified organization. The organization API keys grant programmatic access to an organization. You can't use the API key to log into MongoDB Cloud through the console.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys"
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
            response_model=PaginatedApiApiUserView,
        )

    def create_org_api_key(
        self,
        org_id: str,
        body: CreateAtlasOrganizationApiKey,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiKeyUserDetails:
        """
        Create One Organization API Key

        Creates one API key for the specified organization. An organization API key grants programmatic access to an organization. You can't use the API key to log into the console.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization API Key to be created.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ApiKeyUserDetails,
        )

    def delete_org_api_key(
        self,
        api_user_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Organization API Key

        Removes one organization API key from the specified organization. When you remove an API key from an organization, MongoDB Cloud also removes that key from any projects that use that key.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}"
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

    def get_org_api_key(
        self,
        api_user_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiKeyUserDetails:
        """
        Return One Organization API Key

        Returns one organization API key. The organization API keys grant programmatic access to an organization. You can't use the API key to log into MongoDB Cloud through the user interface.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key that you want to update.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiKeyUserDetails,
        )

    def update_org_api_key(
        self,
        api_user_id: str,
        org_id: str,
        body: UpdateAtlasOrganizationApiKey,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiKeyUserDetails:
        """
        Update One Organization API Key

        Updates one organization API key in the specified organization. The organization API keys  grant programmatic access to an organization.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key you want to update.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization API key to be updated. This request requires a minimum of one of the two body parameters.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ApiKeyUserDetails,
        )

    def list_org_api_key_access_list_entries(
        self,
        api_user_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiUserAccessListResponseView:
        """
        Return All Access List Entries for One Organization API Key

        Returns all access list entries that you configured for the specified organization API key.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key for which you want to return access list entries.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}/accessList"
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
            response_model=PaginatedApiUserAccessListResponseView,
        )

    def create_org_api_key_access_list_entry(
        self,
        api_user_id: str,
        org_id: str,
        body: list[UserAccessListRequest],
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiUserAccessListResponseView:
        """
        Create One Access List Entry for One Organization API Key

        Creates the access list entries for the specified organization API key. Resources require all API requests originate from IP addresses on the API access list.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key for which you want to create a new access list entry.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Access list entries to be created for the specified organization API key.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}/accessList"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedApiUserAccessListResponseView,
        )

    def delete_org_api_key_access_list_entry(
        self,
        api_user_id: str,
        ip_address: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Access List Entry for One Organization API Key

        Removes the specified access list entry from the specified organization API key. Resources require all API requests originate from the IP addresses on the API access list. In addition, you cannot remove the requesting IP address from the requesting organization API key.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key for which you want to remove access list entries.
            ip_address: One IP address or multiple IP addresses represented as one CIDR block to limit requests to API resources in the specified organization. When adding a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}/accessList/{quote(str(ip_address), safe='')}"
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

    def get_org_api_key_access_list_entry(
        self,
        api_user_id: str,
        ip_address: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserAccessListResponse:
        """
        Return One Access List Entry for One Organization API Key

        Returns one access list entry for the specified organization API key. Resources require  all API requests originate from IP addresses on the API access list.

        Args:
            api_user_id: Unique 24-hexadecimal digit string that identifies this organization API key for which you want to return access list entries.
            ip_address: One IP address or multiple IP addresses represented as one CIDR block to limit requests to API resources in the specified organization. When adding a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/apiKeys/{quote(str(api_user_id), safe='')}/accessList/{quote(str(ip_address), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=UserAccessListResponse,
        )
