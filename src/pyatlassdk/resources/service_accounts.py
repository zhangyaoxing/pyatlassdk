"""Generated resource for ServiceAccounts. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.group_service_account import GroupServiceAccount
from pyatlassdk.models.group_service_account_request import GroupServiceAccountRequest
from pyatlassdk.models.group_service_account_role_assignment import GroupServiceAccountRoleAssignment
from pyatlassdk.models.group_service_account_update_request import GroupServiceAccountUpdateRequest
from pyatlassdk.models.org_service_account import OrgServiceAccount
from pyatlassdk.models.org_service_account_request import OrgServiceAccountRequest
from pyatlassdk.models.org_service_account_update_request import OrgServiceAccountUpdateRequest
from pyatlassdk.models.paginated_group_service_accounts import PaginatedGroupServiceAccounts
from pyatlassdk.models.paginated_org_service_accounts import PaginatedOrgServiceAccounts
from pyatlassdk.models.paginated_service_account_group import PaginatedServiceAccountGroup
from pyatlassdk.models.paginated_service_account_ip_access_entry_view import PaginatedServiceAccountIPAccessEntryView
from pyatlassdk.models.service_account_ip_access_list_entry import ServiceAccountIPAccessListEntry
from pyatlassdk.models.service_account_secret import ServiceAccountSecret
from pyatlassdk.models.service_account_secret_request import ServiceAccountSecretRequest

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ServiceAccounts:
    """Endpoints for managing Service Accounts and secrets. Service Accounts are used for programmatic access to the Atlas Admin API through the OAuth 2.0 Client Credentials flow."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_service_accounts(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_system_managed: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedGroupServiceAccounts:
        """
        Return All Project Service Accounts

        Returns all Service Accounts for the specified Project. By default, system-managed Service Accounts are excluded. Set `includeSystemManaged=true` to include them.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_system_managed: Flag that indicates whether system-managed Service Accounts (such as those used for MCP ingress/egress integrations) are included in the response. When false, only user-managed Service Accounts are returned.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts"
        params = {
            "envelope": envelope,
            "includeSystemManaged": include_system_managed,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedGroupServiceAccounts,
        )

    def create_group_service_account(
        self,
        group_id: str,
        body: GroupServiceAccountRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupServiceAccount:
        """
        Create One Project Service Account

        Creates one Service Account for the specified Project. The Service Account will automatically be added as an Organization Member to the Organization that the specified Project is a part of.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details of the new Service Account.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupServiceAccount,
        )

    def delete_group_service_account(
        self,
        client_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Project Service Account

        Removes the specified Service Account from the specified project. The Service Account will still be a part of the Organization it was created in, and the credentials will remain active until expired or manually revoked.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}"
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

    def get_group_service_account(
        self,
        client_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupServiceAccount:
        """
        Return One Project Service Account

        Returns one Service Account in the specified Project.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupServiceAccount,
        )

    def update_group_service_account(
        self,
        client_id: str,
        group_id: str,
        body: GroupServiceAccountUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupServiceAccount:
        """
        Update One Project Service Account

        Updates one Service Account in the specified Project.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The new details for the Service Account.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=GroupServiceAccount,
        )

    def list_group_service_account_access_list(
        self,
        client_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedServiceAccountIPAccessEntryView:
        """
        Return All Access List Entries for One Project Service Account

        Returns all access list entries that you configured for the specified Service Account for the project.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/accessList"
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
            response_model=PaginatedServiceAccountIPAccessEntryView,
        )

    def create_group_service_account_access_list(
        self,
        client_id: str,
        group_id: str,
        body: list[ServiceAccountIPAccessListEntry],
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedServiceAccountIPAccessEntryView:
        """
        Add Access List Entries for One Project Service Account

        Add Access List Entries for the specified Service Account for the project. Resources require all API requests to originate from IP addresses on the API access list.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: A list of access list entries to add to the access list of the specified Service Account for the project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/accessList"
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
            response_model=PaginatedServiceAccountIPAccessEntryView,
        )

    def delete_group_service_account_access_list_entry(
        self,
        client_id: str,
        group_id: str,
        ip_address: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Access List Entry from One Project Service Account

        Removes the specified access list entry from the specified Service Account for the project. A Service Account cannot remove its own IP address from its access list.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            ip_address: One IP address or multiple IP addresses represented as one CIDR block. When specifying a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/accessList/{quote(str(ip_address), safe='')}"
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

    def create_group_service_account_secret(
        self,
        client_id: str,
        group_id: str,
        body: ServiceAccountSecretRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ServiceAccountSecret:
        """
        Create One Project Service Account Secret

        Create a secret for the specified Service Account in the specified Project.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details for the new secret.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/secrets"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ServiceAccountSecret,
        )

    def delete_group_service_account_secret(
        self,
        client_id: str,
        group_id: str,
        secret_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Project Service Account Secret

        Deletes the specified Service Account secret.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            secret_id: Unique 24-hexadecimal digit string that identifies the secret.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
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

    def invite_group_service_account(
        self,
        client_id: str,
        group_id: str,
        body: GroupServiceAccountRoleAssignment,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupServiceAccount:
        """
        Assign One Service Account to One Project

        Assigns the specified Service Account to the specified Project.

        Args:
            client_id: The Client ID of the Service Account.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The Project permissions for the Service Account in the specified Project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}:invite"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupServiceAccount,
        )

    def list_org_service_accounts(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_system_managed: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOrgServiceAccounts:
        """
        Return All Organization Service Accounts

        Returns all Service Accounts for the specified Organization. By default, system-managed Service Accounts are excluded. Set `includeSystemManaged=true` to include them.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_system_managed: Flag that indicates whether system-managed Service Accounts (such as those used for MCP ingress/egress integrations) are included in the response. When false, only user-managed Service Accounts are returned.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts"
        params = {
            "envelope": envelope,
            "includeSystemManaged": include_system_managed,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedOrgServiceAccounts,
        )

    def create_org_service_account(
        self,
        org_id: str,
        body: OrgServiceAccountRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgServiceAccount:
        """
        Create One Organization Service Account

        Creates one Service Account for the specified Organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details of the new Service Account.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgServiceAccount,
        )

    def delete_org_service_account(
        self,
        client_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Organization Service Account

        Deletes the specified Service Account.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}"
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

    def get_org_service_account(
        self,
        client_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgServiceAccount:
        """
        Return One Organization Service Account

        Returns the specified Service Account.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgServiceAccount,
        )

    def update_org_service_account(
        self,
        client_id: str,
        org_id: str,
        body: OrgServiceAccountUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgServiceAccount:
        """
        Update One Organization Service Account

        Updates the specified Service Account in the specified Organization.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The new details for the Service Account.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrgServiceAccount,
        )

    def list_org_service_account_access_list(
        self,
        client_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedServiceAccountIPAccessEntryView:
        """
        Return All Access List Entries for One Organization Service Account

        Returns all access list entries that you configured for the specified Service Account for the organization.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/accessList"
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
            response_model=PaginatedServiceAccountIPAccessEntryView,
        )

    def create_org_service_account_access_list(
        self,
        client_id: str,
        org_id: str,
        body: list[ServiceAccountIPAccessListEntry],
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedServiceAccountIPAccessEntryView:
        """
        Add Access List Entries for One Organization Service Account

        Add Access List Entries for the specified Service Account for the organization. Resources require all API requests to originate from IP addresses on the API access list.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: A list of access list entries to add to the access list of the specified Service Account for the organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/accessList"
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
            response_model=PaginatedServiceAccountIPAccessEntryView,
        )

    def delete_org_service_account_access_list_entry(
        self,
        client_id: str,
        ip_address: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Access List Entry from One Organization Service Account

        Removes the specified access list entry from the specified Service Account for the organization. A Service Account cannot remove its own IP address from its access list.

        Args:
            client_id: The Client ID of the Service Account.
            ip_address: One IP address or multiple IP addresses represented as one CIDR block. When specifying a CIDR block with a subnet mask, such as 192.0.2.0/24, use the URL-encoded value %2F for the forward slash /.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/accessList/{quote(str(ip_address), safe='')}"
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

    def get_org_service_account_groups(
        self,
        client_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedServiceAccountGroup:
        """
        Return All Service Account Project Assignments

        Returns a list of all projects the specified Service Account is a part of.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/groups"
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
            response_model=PaginatedServiceAccountGroup,
        )

    def create_org_service_account_secret(
        self,
        client_id: str,
        org_id: str,
        body: ServiceAccountSecretRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ServiceAccountSecret:
        """
        Create One Organization Service Account Secret

        Create a secret for the specified Service Account.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details for the new secret.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/secrets"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ServiceAccountSecret,
        )

    def delete_org_service_account_secret(
        self,
        client_id: str,
        org_id: str,
        secret_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Organization Service Account Secret

        Deletes the specified Service Account secret.

        Args:
            client_id: The Client ID of the Service Account.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            secret_id: Unique 24-hexadecimal digit string that identifies the secret.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/serviceAccounts/{quote(str(client_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
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
