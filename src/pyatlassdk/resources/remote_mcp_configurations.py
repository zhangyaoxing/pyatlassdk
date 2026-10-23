"""Generated resource for RemoteMCPConfigurations. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.create_group_mcp_config_request import CreateGroupMcpConfigRequest
from pyatlassdk.models.create_org_mcp_config_request import CreateOrgMcpConfigRequest
from pyatlassdk.models.group_mcp_config_response import GroupMcpConfigResponse
from pyatlassdk.models.group_mcp_config_update_request import GroupMcpConfigUpdateRequest
from pyatlassdk.models.org_mcp_config_response import OrgMcpConfigResponse
from pyatlassdk.models.org_mcp_config_update_request import OrgMcpConfigUpdateRequest
from pyatlassdk.models.paginated_group_mcp_config_view import PaginatedGroupMcpConfigView
from pyatlassdk.models.paginated_mcp_config_secret_view import PaginatedMcpConfigSecretView
from pyatlassdk.models.paginated_org_mcp_config_view import PaginatedOrgMcpConfigView
from pyatlassdk.models.service_account_secret import ServiceAccountSecret
from pyatlassdk.models.service_account_secret_request import ServiceAccountSecretRequest

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class RemoteMCPConfigurations:
    """Returns and manages Remote MCP configurations for organizations and projects."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_mcp_configs(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedGroupMcpConfigView:
        """
        Return All MCP Configurations for One Project

        Returns all MCP configurations associated with the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs"
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
            response_model=PaginatedGroupMcpConfigView,
        )

    def create_group_mcp_config(
        self,
        group_id: str,
        body: CreateGroupMcpConfigRequest,
    ) -> GroupMcpConfigResponse:
        """
        Create One MCP Configuration for One Project

        Creates an MCP configuration for the specified project. Returns the configuration ID and ingress credentials.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            body: MCP configuration to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=GroupMcpConfigResponse,
        )

    def delete_group_mcp_config(
        self,
        group_id: str,
        mcp_config_id: str,
        *,
        cascading: bool | None = None,
    ) -> Any:
        """
        Delete One MCP Configuration for One Project

        Deletes the MCP configuration with the specified ID for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration to delete.
            cascading: Flag that indicates whether to delete the MCP configuration even if it has active secrets. If false and active secrets exist, the request returns an error. Defaults to false.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}"
        params = {
            "cascading": cascading,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_mcp_config(
        self,
        group_id: str,
        mcp_config_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupMcpConfigResponse:
        """
        Return One MCP Configuration for One Project

        Returns the MCP configuration with the specified ID for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupMcpConfigResponse,
        )

    def update_group_mcp_config(
        self,
        group_id: str,
        mcp_config_id: str,
        body: GroupMcpConfigUpdateRequest,
        *,
        pretty: bool | None = None,
    ) -> GroupMcpConfigResponse:
        """
        Update One MCP Configuration for One Project

        Updates the specified MCP configuration for the project. Supports partial updates: only provided fields are changed.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration to update.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: MCP configuration fields to update.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}"
        params = {
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=GroupMcpConfigResponse,
        )

    def list_group_mcp_config_secrets(
        self,
        group_id: str,
        mcp_config_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedMcpConfigSecretView:
        """
        Return All Secrets for One Project MCP Configuration

        Returns metadata for all secrets on the ingress service account of the specified project-level MCP configuration. Secret values are never returned.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets"
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
            response_model=PaginatedMcpConfigSecretView,
        )

    def create_group_mcp_config_secret(
        self,
        group_id: str,
        mcp_config_id: str,
        body: ServiceAccountSecretRequest,
    ) -> ServiceAccountSecret:
        """
        Create One Secret for One Project MCP Configuration

        Creates a new secret on the ingress service account of the specified project-level MCP configuration. The plain-text secret value is returned only in this response and is never shown again.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration.
            body: Secret creation request.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=ServiceAccountSecret,
        )

    def delete_group_mcp_config_secret(
        self,
        group_id: str,
        mcp_config_id: str,
        secret_id: str,
    ) -> Any:
        """
        Delete One Secret for One Project MCP Configuration

        Deletes the specified secret from the ingress service account of the specified project-level MCP configuration.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration.
            secret_id: Unique 24-hexadecimal digit string that identifies the secret.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=Any,
        )

    def get_group_mcp_config_secret(
        self,
        group_id: str,
        mcp_config_id: str,
        secret_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ServiceAccountSecret:
        """
        Return One Secret for One Project MCP Configuration

        Returns metadata for the specified secret on the ingress service account of a project-level MCP configuration. The secret value is never returned.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            mcp_config_id: Unique identifier of the MCP configuration.
            secret_id: Unique 24-hexadecimal digit string that identifies the secret.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ServiceAccountSecret,
        )

    def list_org_mcp_configs(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOrgMcpConfigView:
        """
        Return All MCP Configurations for One Organization

        Returns all MCP configurations associated with the specified organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs"
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
            response_model=PaginatedOrgMcpConfigView,
        )

    def create_org_mcp_config(
        self,
        org_id: str,
        body: CreateOrgMcpConfigRequest,
    ) -> OrgMcpConfigResponse:
        """
        Create One MCP Configuration for One Organization

        Creates an MCP configuration for the specified organization. Returns the configuration ID and ingress credentials.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            body: MCP configuration to create.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=OrgMcpConfigResponse,
        )

    def delete_org_mcp_config(
        self,
        mcp_config_id: str,
        org_id: str,
        *,
        cascading: bool | None = None,
    ) -> Any:
        """
        Delete One MCP Configuration for One Organization

        Deletes the MCP configuration with the specified ID for the specified organization.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration to delete.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            cascading: Flag that indicates whether to delete the MCP configuration even if it has active secrets. If false and active secrets exist, the request returns an error. Defaults to false.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}"
        params = {
            "cascading": cascading,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_org_mcp_config(
        self,
        mcp_config_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgMcpConfigResponse:
        """
        Return One MCP Configuration for One Organization

        Returns the MCP configuration with the specified ID for the specified organization.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgMcpConfigResponse,
        )

    def update_org_mcp_config(
        self,
        mcp_config_id: str,
        org_id: str,
        body: OrgMcpConfigUpdateRequest,
        *,
        pretty: bool | None = None,
    ) -> OrgMcpConfigResponse:
        """
        Update One MCP Configuration for One Organization

        Updates the specified MCP configuration for the organization. Supports partial updates: only provided fields are changed.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration to update.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: MCP configuration fields to update.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}"
        params = {
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrgMcpConfigResponse,
        )

    def list_org_mcp_config_secrets(
        self,
        mcp_config_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedMcpConfigSecretView:
        """
        Return All Secrets for One Organization MCP Configuration

        Returns metadata for all secrets on the ingress service account of the specified organization-level MCP configuration. Secret values are never returned.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets"
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
            response_model=PaginatedMcpConfigSecretView,
        )

    def create_org_mcp_config_secret(
        self,
        mcp_config_id: str,
        org_id: str,
        body: ServiceAccountSecretRequest,
    ) -> ServiceAccountSecret:
        """
        Create One Secret for One Organization MCP Configuration

        Creates a new secret on the ingress service account of the specified organization-level MCP configuration. The plain-text secret value is returned only in this response and is never shown again.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            body: Secret creation request.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=ServiceAccountSecret,
        )

    def delete_org_mcp_config_secret(
        self,
        mcp_config_id: str,
        org_id: str,
        secret_id: str,
    ) -> Any:
        """
        Delete One Secret for One Organization MCP Configuration

        Deletes the specified secret from the ingress service account of the specified organization-level MCP configuration.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            secret_id: Unique 24-hexadecimal digit string that identifies the secret.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=Any,
        )

    def get_org_mcp_config_secret(
        self,
        mcp_config_id: str,
        org_id: str,
        secret_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ServiceAccountSecret:
        """
        Return One Secret for One Organization MCP Configuration

        Returns metadata for the specified secret on the ingress service account of an organization-level MCP configuration. The secret value is never returned.

        Args:
            mcp_config_id: Unique identifier of the MCP configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            secret_id: Unique 24-hexadecimal digit string that identifies the secret.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/mcpConfigs/{quote(str(mcp_config_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ServiceAccountSecret,
        )
