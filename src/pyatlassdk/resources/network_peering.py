"""Generated resource for NetworkPeering. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.base_network_peering_connection_settings import BaseNetworkPeeringConnectionSettings
from pyatlassdk.models.cloud_provider_container import CloudProviderContainer
from pyatlassdk.models.paginated_cloud_provider_container_view import PaginatedCloudProviderContainerView
from pyatlassdk.models.paginated_container_peer_view import PaginatedContainerPeerView
from pyatlassdk.models.private_ip_mode_view import PrivateIPModeView
from pyatlassdk.models.request_accepted import RequestAccepted

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class NetworkPeering:
    """
    Returns, adds, edits, and removes network peering containers and peering connections.
    When you deploy an M10+ dedicated cluster, Atlas creates a VPC for the selected provider and region or regions if no existing VPC or VPC peering connection exists for that provider and region. Atlas assigns the VPC a Classless Inter-Domain Routing (CIDR) block.
    """

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_containers(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        provider_name: Literal["AWS", "AZURE", "GCP"],
    ) -> PaginatedCloudProviderContainerView:
        """
        Return All Network Peering Containers in One Project for One Cloud Provider

        Returns details about all network peering containers in the specified project for the specified cloud provider. If you do not specify the cloud provider, MongoDB Cloud returns details about all network peering containers in the project for Amazon Web Services (AWS).

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            provider_name: Cloud service provider that serves the desired network peering containers.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/containers"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "providerName": provider_name,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedCloudProviderContainerView,
        )

    def create_group_container(
        self,
        group_id: str,
        body: CloudProviderContainer,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderContainer:
        """
        Create One Network Peering Container

        Creates one new network peering container in the specified project. MongoDB Cloud can deploy Network Peering connections in a network peering container. GCP can have one container per project. AWS and Azure can have one container per cloud provider region.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one new network peering container in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/containers"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=CloudProviderContainer,
        )

    def list_group_container_all(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedCloudProviderContainerView:
        """
        Return All Network Peering Containers in One Project

        Returns details about all network peering containers in the specified project. Network peering containers contain network peering connections.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/containers/all"
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
            response_model=PaginatedCloudProviderContainerView,
        )

    def delete_group_container(
        self,
        container_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Network Peering Container

        Removes one network peering container in the specified project.

        Args:
            container_id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that you want to remove.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/containers/{quote(str(container_id), safe='')}"
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

    def get_group_container(
        self,
        container_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderContainer:
        """
        Return One Network Peering Container

        Returns details about one network peering container in one specified project. Network peering containers contain network peering connections.

        Args:
            container_id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/containers/{quote(str(container_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CloudProviderContainer,
        )

    def update_group_container(
        self,
        container_id: str,
        group_id: str,
        body: CloudProviderContainer,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderContainer:
        """
        Update One Network Peering Container

        Updates the network details and labels of one specified network peering container in the specified project.

        Args:
            container_id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that you want to remove.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the network details and labels of one specified network peering container in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/containers/{quote(str(container_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=CloudProviderContainer,
        )

    def list_group_peers(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        provider_name: Literal["AWS", "AZURE", "GCP"] | None = None,
    ) -> PaginatedContainerPeerView:
        """
        Return All Network Peering Connections in One Project

        Returns details about all network peering connections in the specified project. Network peering allows multiple cloud-hosted applications to securely connect to the same project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            provider_name: Cloud service provider to use for this VPC peering connection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/peers"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "providerName": provider_name,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedContainerPeerView,
        )

    def create_group_peer(
        self,
        group_id: str,
        body: BaseNetworkPeeringConnectionSettings,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BaseNetworkPeeringConnectionSettings:
        """
        Create One Network Peering Connection

        Creates one new network peering connection in the specified project. Network peering allows multiple cloud-hosted applications to securely connect to the same project. To learn more about considerations and prerequisites, see the Network Peering Documentation.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Create one network peering connection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/peers"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=BaseNetworkPeeringConnectionSettings,
        )

    def delete_group_peer(
        self,
        group_id: str,
        peer_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> RequestAccepted:
        """
        Remove One Network Peering Connection

        Removes one network peering connection in the specified project. If you remove the last network peering connection associated with a project, MongoDB Cloud also removes any AWS security groups from the project IP access list.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            peer_id: Unique 24-hexadecimal digit string that identifies the network peering connection that you want to delete.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/peers/{quote(str(peer_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=RequestAccepted,
        )

    def get_group_peer(
        self,
        group_id: str,
        peer_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BaseNetworkPeeringConnectionSettings:
        """
        Return One Network Peering Connection in One Project

        Returns details about one specified network peering connection in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            peer_id: Unique 24-hexadecimal digit string that identifies the network peering connection that you want to retrieve.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/peers/{quote(str(peer_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=BaseNetworkPeeringConnectionSettings,
        )

    def update_group_peer(
        self,
        group_id: str,
        peer_id: str,
        body: BaseNetworkPeeringConnectionSettings,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> BaseNetworkPeeringConnectionSettings:
        """
        Update One Network Peering Connection

        Updates one specified network peering connection in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            peer_id: Unique 24-hexadecimal digit string that identifies the network peering connection that you want to update.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Modify one network peering connection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/peers/{quote(str(peer_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=BaseNetworkPeeringConnectionSettings,
        )

    def verify_group_private_ip_mode(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PrivateIPModeView:
        """
        Verify Connect via Peering-Only Mode for One Project

        Verifies if someone set the specified project to **Connect via Peering Only** mode.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateIpMode"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PrivateIPModeView,
        )

    def disable_group_private_ip_mode_peering(
        self,
        group_id: str,
        body: PrivateIPModeView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PrivateIPModeView:
        """
        Disable Connect via Peering-Only Mode for One Project

        Disables Connect via Peering Only mode for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Disables Connect via Peering Only mode for the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateIpMode"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=PrivateIPModeView,
        )
