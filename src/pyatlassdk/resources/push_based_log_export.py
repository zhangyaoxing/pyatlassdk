"""Generated resource for PushBasedLogExport. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.create_push_based_log_export_project_request import CreatePushBasedLogExportProjectRequest
from pyatlassdk.models.log_integration_request import LogIntegrationRequest
from pyatlassdk.models.log_integration_response import LogIntegrationResponse
from pyatlassdk.models.org_log_integration_request import OrgLogIntegrationRequest
from pyatlassdk.models.org_log_integration_response import OrgLogIntegrationResponse
from pyatlassdk.models.org_log_integration_update_request import OrgLogIntegrationUpdateRequest
from pyatlassdk.models.paginated_log_integration_response import PaginatedLogIntegrationResponse
from pyatlassdk.models.paginated_org_log_integration_response import PaginatedOrgLogIntegrationResponse
from pyatlassdk.models.push_based_log_export_project import PushBasedLogExportProject

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class PushBasedLogExport:
    """You can continually export mongod, mongos, and audit logs to an AWS S3 bucket. The new `/logIntegrations` API provides 1-minute log export on a best-effort basis. The existing `/pushBasedLogExport` API provides 5-minute log export and will be deprecated in the future. The log export integrations are managed at the project level."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_log_integrations(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        integration_type: str | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedLogIntegrationResponse:
        """
        Return All Active Log Integrations

        Returns all log integration configurations for the project. Optionally filter by integration type.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            integration_type: Optional filter by integration type (e.g., `S3_LOG_EXPORT`).
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/logIntegrations"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "integrationType": integration_type,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedLogIntegrationResponse,
        )

    def create_group_log_integration(
        self,
        group_id: str,
        body: LogIntegrationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LogIntegrationResponse:
        """
        Create One Log Integration

        Creates a new log integration configuration identified by a unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Log integration configuration to create.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/logIntegrations"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=LogIntegrationResponse,
        )

    def delete_group_log_integration(
        self,
        group_id: str,
        id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Log Integration

        Removes the configuration for one log integration identified by its unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            id: Unique identifier of the log integration configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/logIntegrations/{quote(str(id), safe='')}"
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

    def get_group_log_integration(
        self,
        group_id: str,
        id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LogIntegrationResponse:
        """
        Return One Log Integration

        Returns the configuration for one log integration identified by its unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            id: Unique identifier of the log integration configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/logIntegrations/{quote(str(id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=LogIntegrationResponse,
        )

    def update_group_log_integration(
        self,
        group_id: str,
        id: str,
        body: LogIntegrationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LogIntegrationResponse:
        """
        Update One Log Integration

        Updates the configuration for one log integration identified by its unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            id: Unique identifier of the log integration configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updated log integration configuration.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/logIntegrations/{quote(str(id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=LogIntegrationResponse,
        )

    def delete_group_push_based_log_export(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Disable Push-Based Log Export for One Project

        Disables the push-based log export feature by resetting the project level settings to its default configuration.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/pushBasedLogExport"
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

    def get_group_push_based_log_export(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PushBasedLogExportProject:
        """
        Return One Push-Based Log Export Configuration in One Project

        Fetches the current project level settings for the push-based log export feature.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/pushBasedLogExport"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PushBasedLogExportProject,
        )

    def update_group_push_based_log_export(
        self,
        group_id: str,
        body: PushBasedLogExportProject,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Update One Push-Based Log Export Configuration in One Project

        Updates the project level settings for the push-based log export feature.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The project configuration details. The S3 bucket name, IAM role ID, and prefix path fields are the only fields that may be specified. Fields left unspecified will not be modified.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/pushBasedLogExport"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=Any,
        )

    def create_group_push_based_log_export(
        self,
        group_id: str,
        body: CreatePushBasedLogExportProjectRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Create One Push-Based Log Export Configuration in One Project

        Configures the project level settings for the push-based log export feature.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The project configuration details. The S3 bucket name, IAM role ID, and prefix path fields are required.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/pushBasedLogExport"
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

    def list_org_log_integrations(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOrgLogIntegrationResponse:
        """
        Return All Organization Log Integrations

        Returns all log integration configurations for the organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/logIntegrations"
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
            response_model=PaginatedOrgLogIntegrationResponse,
        )

    def create_org_log_integration(
        self,
        org_id: str,
        body: OrgLogIntegrationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgLogIntegrationResponse:
        """
        Create One Organization Log Integration

        Creates a new organization-level log integration configuration identified by a unique ID.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Log integration configuration to create.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/logIntegrations"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgLogIntegrationResponse,
        )

    def delete_org_log_integration(
        self,
        log_integration_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Organization Log Integration

        Removes one organization-level log integration configuration identified by its unique ID.

        Args:
            log_integration_id: Unique identifier of the log integration configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/logIntegrations/{quote(str(log_integration_id), safe='')}"
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

    def get_org_log_integration(
        self,
        log_integration_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgLogIntegrationResponse:
        """
        Return One Organization Log Integration

        Returns the configuration for one organization-level log integration identified by its unique ID.

        Args:
            log_integration_id: Unique identifier of the log integration configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/logIntegrations/{quote(str(log_integration_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgLogIntegrationResponse,
        )

    def update_org_log_integration(
        self,
        log_integration_id: str,
        org_id: str,
        body: OrgLogIntegrationUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgLogIntegrationResponse:
        """
        Update One Organization Log Integration

        Updates one organization-level log integration configuration identified by its unique ID. Read endpoints redact header values; a redacted value sent back unchanged leaves the stored value in place, so supply a header value in full only when changing it.

        Args:
            log_integration_id: Unique identifier of the log integration configuration.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Log integration configuration to update.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/logIntegrations/{quote(str(log_integration_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=OrgLogIntegrationResponse,
        )
