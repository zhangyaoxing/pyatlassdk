"""Generated resource for Streams. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.account_details import AccountDetails
from pyatlassdk.admin.models.paginated_api_streams_connection_view import PaginatedApiStreamsConnectionView
from pyatlassdk.admin.models.paginated_api_streams_failover_connection import PaginatedApiStreamsFailoverConnection
from pyatlassdk.admin.models.paginated_api_streams_private_link_view import PaginatedApiStreamsPrivateLinkView
from pyatlassdk.admin.models.paginated_api_streams_stream_processor_with_stats_view import PaginatedApiStreamsStreamProcessorWithStatsView
from pyatlassdk.admin.models.paginated_api_streams_tenant_view import PaginatedApiStreamsTenantView
from pyatlassdk.admin.models.paginated_api_streams_vpc_peering_connection_view import PaginatedApiStreamsVPCPeeringConnectionView
from pyatlassdk.admin.models.paginated_streams_workspace_private_endpoint_response import PaginatedStreamsWorkspacePrivateEndpointResponse
from pyatlassdk.admin.models.streams_connection import StreamsConnection
from pyatlassdk.admin.models.streams_failover_connection import StreamsFailoverConnection
from pyatlassdk.admin.models.streams_modify_stream_processor import StreamsModifyStreamProcessor
from pyatlassdk.admin.models.streams_private_link_connection import StreamsPrivateLinkConnection
from pyatlassdk.admin.models.streams_private_link_connection_request import StreamsPrivateLinkConnectionRequest
from pyatlassdk.admin.models.streams_processor import StreamsProcessor
from pyatlassdk.admin.models.streams_processor_request import StreamsProcessorRequest
from pyatlassdk.admin.models.streams_processor_with_stats import StreamsProcessorWithStats
from pyatlassdk.admin.models.streams_start_stream_processor_with import StreamsStartStreamProcessorWith
from pyatlassdk.admin.models.streams_tenant import StreamsTenant
from pyatlassdk.admin.models.streams_tenant_update_request import StreamsTenantUpdateRequest
from pyatlassdk.admin.models.streams_workspace_private_endpoint_request import StreamsWorkspacePrivateEndpointRequest
from pyatlassdk.admin.models.streams_workspace_private_endpoint_response import StreamsWorkspacePrivateEndpointResponse
from pyatlassdk.admin.models.tenant_with_sample_connections import TenantWithSampleConnections
from pyatlassdk.admin.models.vpc_peering_action_challenge import VPCPeeringActionChallenge

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class Streams:
    """Returns, adds, edits, and removes Streams Workspaces. This resource requires your project ID."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_group_stream_workspaces(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiStreamsTenantView:
        """
        Return All Stream Workspaces in One Project

        Returns all stream workspaces for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams"
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
            response_model=PaginatedApiStreamsTenantView,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def create_group_stream_workspace(
        self,
        group_id: str,
        body: StreamsTenant,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsTenant:
        """
        Create One Stream Workspace

        Creates one stream workspace in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to create one streams workspace in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=StreamsTenant,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def get_group_stream_account_details(
        self,
        group_id: str,
        *,
        cloud_provider: str,
        envelope: bool | None = None,
        region_name: str,
    ) -> AccountDetails:
        """
        Return Account ID and VPC ID for One Project and Region

        Returns the Account ID, and the VPC ID for the group and region specified.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            cloud_provider: One of "aws", "azure" or "gcp".
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            region_name: The cloud provider specific region name, i.e. "US_EAST_1" for cloud provider "aws".
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/accountDetails"
        params = {
            "cloudProvider": cloud_provider,
            "envelope": envelope,
            "regionName": region_name,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AccountDetails,
            accept="application/vnd.atlas.2024-11-13+json",
        )

    def list_group_stream_active_vpc_peering_connections(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiStreamsVPCPeeringConnectionView:
        """
        Return All Active Incoming VPC Peering Connections

        Returns a list of active incoming VPC Peering Connections.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/activeVpcPeeringConnections"
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
            response_model=PaginatedApiStreamsVPCPeeringConnectionView,
            accept="application/vnd.atlas.2024-11-13+json",
        )

    def list_group_stream_private_link_connections(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiStreamsPrivateLinkView:
        """
        Return All Private Link Connections

        Returns all Private Link connections for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/privateLinkConnections"
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
            response_model=PaginatedApiStreamsPrivateLinkView,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def create_group_stream_private_link_connection(
        self,
        group_id: str,
        body: StreamsPrivateLinkConnection,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsPrivateLinkConnection:
        """
        Create One Private Link Connection

        Creates one Private Link in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to create one Private Link connection for a project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/privateLinkConnections"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=StreamsPrivateLinkConnection,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def delete_group_stream_private_link_connection(
        self,
        connection_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Private Link Connection

        Deletes one Private Link in the specified project.

        Args:
            connection_id: Unique ID that identifies the Private Link connection.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/privateLinkConnections/{quote(str(connection_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def get_group_stream_private_link_connection(
        self,
        connection_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> StreamsPrivateLinkConnection:
        """
        Return One Private Link Connection

        Returns the details of one Private Link connection within the project.

        Args:
            connection_id: Unique ID that identifies the Private Link connection.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/privateLinkConnections/{quote(str(connection_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=StreamsPrivateLinkConnection,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def update_group_stream_private_link_connection(
        self,
        connection_id: str,
        group_id: str,
        body: StreamsPrivateLinkConnectionRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsPrivateLinkConnection:
        """
        Update One Private Link Connection

        Updates one Private Link connection in the specified project.

        Args:
            connection_id: Unique ID that identifies the Private Link connection.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The fields to update on the Private Link connection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/privateLinkConnections/{quote(str(connection_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=StreamsPrivateLinkConnection,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def list_group_stream_vpc_peering_connections(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        requester_account_id: str,
    ) -> PaginatedApiStreamsVPCPeeringConnectionView:
        """
        Return All VPC Peering Connections

        Returns a list of incoming VPC Peering Connections.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            requester_account_id: The Account ID of the VPC Peering connection/s.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/vpcPeeringConnections"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "requesterAccountId": requester_account_id,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedApiStreamsVPCPeeringConnectionView,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def delete_group_stream_vpc_peering_connection(
        self,
        group_id: str,
        id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Delete One VPC Peering Connection

        Deletes an incoming VPC Peering connection.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            id: The VPC Peering Connection id.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/vpcPeeringConnections/{quote(str(id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def accept_group_stream_vpc_peering_connection(
        self,
        group_id: str,
        id: str,
        body: VPCPeeringActionChallenge,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Accept One Incoming VPC Peering Connection

        Requests the acceptance of an incoming VPC Peering connection.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            id: The VPC Peering Connection id.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Challenge values for VPC Peering requester account ID, and requester VPC ID.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/vpcPeeringConnections/{quote(str(id), safe='')}:accept"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Any,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def reject_group_stream_vpc_peering_connection(
        self,
        group_id: str,
        id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Reject One Incoming VPC Peering Connection

        Requests the rejection of an incoming VPC Peering connection.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            id: The VPC Peering Connection id.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/vpcPeeringConnections/{quote(str(id), safe='')}:reject"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def delete_group_stream_workspace(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Stream Workspace

        Delete one stream workspace in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace to delete.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def get_group_stream_workspace(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        include_connections: bool | None = None,
    ) -> StreamsTenant:
        """
        Return One Stream Workspace

        Returns the details of one stream workspace within the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_connections: Flag to indicate whether connections information should be included in the stream workspace.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}"
        params = {
            "envelope": envelope,
            "includeConnections": include_connections,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=StreamsTenant,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def update_group_stream_workspace(
        self,
        group_id: str,
        tenant_name: str,
        body: StreamsTenantUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsTenant:
        """
        Update One Stream Workspace

        Update one stream workspace in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace to update.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update in the streams workspace.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=StreamsTenant,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def download_group_stream_audit_logs(
        self,
        group_id: str,
        tenant_name: str,
        *,
        end_date: int | None = None,
        envelope: bool | None = None,
        sp_name: str | None = None,
        start_date: int | None = None,
    ) -> bytes:
        """
        Download Audit Logs for One Atlas Stream Processing Workspace

        Downloads the audit logs for the specified Atlas Streams Processing workspace or stream processor. By default, logs cover periods of 30 days. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            end_date: Timestamp that specifies the end point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            sp_name: Name of the stream processor to download logs for. An empty string will download logs for all stream processors in the workspace.
            start_date: Timestamp that specifies the starting point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/auditLogs"
        params = {
            "endDate": end_date,
            "envelope": envelope,
            "spName": sp_name,
            "startDate": start_date,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=bytes,
            accept="application/vnd.atlas.2023-02-01+gzip",
        )

    def list_group_stream_connections(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiStreamsConnectionView:
        """
        Return All Connections of the Stream Workspaces

        Returns all connections of the stream workspace for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections"
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
            response_model=PaginatedApiStreamsConnectionView,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def create_group_stream_connection(
        self,
        group_id: str,
        tenant_name: str,
        body: StreamsConnection,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsConnection:
        """
        Create One Stream Connection

        Creates one connection for a stream workspace in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to create one connection for a streams workspace in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=StreamsConnection,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def delete_group_stream_connection(
        self,
        connection_name: str,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Stream Connection

        Delete one connection of the specified stream workspace.

        Args:
            connection_name: Label that identifies the stream connection.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def get_group_stream_connection(
        self,
        connection_name: str,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
    ) -> StreamsConnection:
        """
        Return One Stream Connection

        Returns the details of one stream connection within the specified stream workspace.

        Args:
            connection_name: Label that identifies the stream connection to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=StreamsConnection,
            accept="application/vnd.atlas.2023-02-01+json",
        )

    def update_group_stream_connection(
        self,
        connection_name: str,
        group_id: str,
        tenant_name: str,
        body: StreamsConnection,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsConnection:
        """
        Update One Stream Connection

        Update one connection for the specified stream workspace in the specified project.

        Args:
            connection_name: Label that identifies the stream connection.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update one connection for a streams workspace in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=StreamsConnection,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def list_group_stream_connection_failover_connections(
        self,
        connection_name: str,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiStreamsFailoverConnection:
        """
        Return All Stream Failover Connections

        Returns all failover connections for the specified connection in a stream workspace.

        Args:
            connection_name: Label that identifies the stream connection.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}/failoverConnections"
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
            response_model=PaginatedApiStreamsFailoverConnection,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def create_group_stream_connection_failover_connection(
        self,
        connection_name: str,
        group_id: str,
        tenant_name: str,
        body: StreamsFailoverConnection,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsFailoverConnection:
        """
        Create One Failover Stream Connection

        Creates one failover connection for a stream workspace in the specified project.

        Args:
            connection_name: Label that identifies the stream connection name.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to create one failover connection for a streams workspace in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}/failoverConnections"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=StreamsFailoverConnection,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def delete_group_stream_connection_failover_connection(
        self,
        connection_name: str,
        failover_connection_id: str,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Stream Failover Connection

        Delete one failover connection of the specified stream workspace.

        Args:
            connection_name: Label that identifies the stream connection.
            failover_connection_id: Label that identifies the stream failover connection id.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}/failoverConnections/{quote(str(failover_connection_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_group_stream_connection_failover_connection(
        self,
        connection_name: str,
        failover_connection_id: str,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsFailoverConnection:
        """
        Return One Stream Failover Connection

        Get one failover connection of the specified stream workspace.

        Args:
            connection_name: Label that identifies the stream connection.
            failover_connection_id: Label that identifies the stream failover connection id.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}/failoverConnections/{quote(str(failover_connection_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=StreamsFailoverConnection,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def update_group_stream_connection_failover_connection(
        self,
        connection_name: str,
        failover_connection_id: str,
        group_id: str,
        tenant_name: str,
        body: StreamsFailoverConnection,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsFailoverConnection:
        """
        Update One Stream Failover Connection

        Update one failover connection of the specified stream workspace.

        Args:
            connection_name: Label that identifies the stream connection.
            failover_connection_id: Label that identifies the stream failover connection id.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update one failover connection for a streams workspace in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/connections/{quote(str(connection_name), safe='')}/failoverConnections/{quote(str(failover_connection_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=StreamsFailoverConnection,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def create_group_stream_processor(
        self,
        group_id: str,
        tenant_name: str,
        body: StreamsProcessorRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsProcessor:
        """
        Create One Stream Processor

        Create one Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to create an Atlas Streams Processor.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=StreamsProcessor,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def delete_group_stream_processor(
        self,
        group_id: str,
        processor_name: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Stream Processor

        Delete a Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            processor_name: Label that identifies the stream processor.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor/{quote(str(processor_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def get_group_stream_processor(
        self,
        group_id: str,
        processor_name: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsProcessorWithStats:
        """
        Return One Stream Processor

        Get one Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            processor_name: Label that identifies the stream processor.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor/{quote(str(processor_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=StreamsProcessorWithStats,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def update_group_stream_processor(
        self,
        group_id: str,
        processor_name: str,
        tenant_name: str,
        body: StreamsModifyStreamProcessor,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsProcessorWithStats:
        """
        Update One Stream Processor

        Modify one existing Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            processor_name: Label that identifies the stream processor.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Modifications to apply to the stream processor.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor/{quote(str(processor_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=StreamsProcessorWithStats,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def start_group_stream_processor(
        self,
        group_id: str,
        processor_name: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Start One Stream Processor

        Start a Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            processor_name: Label that identifies the stream processor.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor/{quote(str(processor_name), safe='')}:start"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def start_group_stream_processor_with(
        self,
        group_id: str,
        processor_name: str,
        tenant_name: str,
        *,
        body: StreamsStartStreamProcessorWith | None = None,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Start One Stream Processor With Options

        Start a Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            processor_name: Label that identifies the stream processor.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Options for starting a stream processor.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor/{quote(str(processor_name), safe='')}:startWith"
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
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def stop_group_stream_processor(
        self,
        group_id: str,
        processor_name: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Stop One Stream Processor

        Stop a Stream Processor within the specified stream workspace.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            processor_name: Label that identifies the stream processor.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processor/{quote(str(processor_name), safe='')}:stop"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def get_group_stream_processors(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiStreamsStreamProcessorWithStatsView:
        """
        Return All Stream Processors in One Stream Workspace

        Returns all Stream Processors within the specified stream workspace, including information on which processors are failover-eligible.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}/processors"
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
            response_model=PaginatedApiStreamsStreamProcessorWithStatsView,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def download_group_stream_operational_logs(
        self,
        group_id: str,
        tenant_name: str,
        *,
        end_date: int | None = None,
        envelope: bool | None = None,
        sp_name: str | None = None,
        start_date: int | None = None,
    ) -> bytes:
        """
        Download Operational Logs for One Atlas Stream Processing Workspace

        Downloads the operational logs for the specified Atlas Streams Processing workspace or stream processor. By default, logs cover periods of 30 days. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: "Accept: application/vnd.atlas.2025-03-12+gzip".

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Label that identifies the stream workspace.
            end_date: Timestamp that specifies the end point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            sp_name: Name of the stream processor to download logs for. An empty string will download logs for all stream processors in the workspace.
            start_date: Timestamp that specifies the starting point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams/{quote(str(tenant_name), safe='')}:downloadOperationalLogs"
        params = {
            "endDate": end_date,
            "envelope": envelope,
            "spName": sp_name,
            "startDate": start_date,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=bytes,
            accept="application/vnd.atlas.2025-03-12+gzip",
        )

    def with_group_stream_sample_connections(
        self,
        group_id: str,
        body: TenantWithSampleConnections,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> StreamsTenant:
        """
        Create One Stream Workspace with Sample Connections

        Creates one stream workspace in the specified project with sample connections.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to create one streams workspace in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streams:withSampleConnections"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=StreamsTenant,
            accept="application/vnd.atlas.2024-08-05+json",
            content_type="application/vnd.atlas.2024-08-05+json",
        )

    def list_group_streams_workspace_private_endpoints(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedStreamsWorkspacePrivateEndpointResponse:
        """
        Return All Workspace Private Endpoints for Atlas Stream Processing

        Returns all private endpoints registered for Atlas Stream Processing in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streamsWorkspacePrivateEndpoints"
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
            response_model=PaginatedStreamsWorkspacePrivateEndpointResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def create_group_streams_workspace_private_endpoint(
        self,
        group_id: str,
        body: StreamsWorkspacePrivateEndpointRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Create One Workspace Private Endpoint for Atlas Stream Processing

        Registers one customer VPC endpoint for Atlas Stream Processing in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Customer VPC endpoint to register for Atlas Stream Processing.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streamsWorkspacePrivateEndpoints"
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
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def delete_group_streams_workspace_private_endpoint(
        self,
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Workspace Private Endpoint for Atlas Stream Processing

        Removes one private endpoint registered for Atlas Stream Processing in the specified project.

        Args:
            endpoint_id: Unique identifier of the customer's VPC endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streamsWorkspacePrivateEndpoints/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_group_streams_workspace_private_endpoint(
        self,
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> StreamsWorkspacePrivateEndpointResponse:
        """
        Return One Workspace Private Endpoint for Atlas Stream Processing

        Returns one private endpoint registered for Atlas Stream Processing in the specified project.

        Args:
            endpoint_id: Unique identifier of the customer's VPC endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/streamsWorkspacePrivateEndpoints/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=StreamsWorkspacePrivateEndpointResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )
