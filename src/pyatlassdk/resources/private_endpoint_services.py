"""Generated resource for PrivateEndpointServices. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.api_atlas_modify_endpoint_service_request_view import ApiAtlasModifyEndpointServiceRequestView
from pyatlassdk.models.cloud_provider_endpoint_service_request import CloudProviderEndpointServiceRequest
from pyatlassdk.models.create_endpoint_request import CreateEndpointRequest
from pyatlassdk.models.endpoint_service import EndpointService
from pyatlassdk.models.private_link_endpoint import PrivateLinkEndpoint
from pyatlassdk.models.project_setting_item_view import ProjectSettingItemView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class PrivateEndpointServices:
    """Returns, adds, edits, and removes private endpoint services."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def create_group_private_endpoint_endpoint_service(
        self,
        group_id: str,
        body: CloudProviderEndpointServiceRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EndpointService:
        """
        Create One Private Endpoint Service for One Provider

        Creates one private endpoint service for the specified cloud service provider. This cloud service provider manages the private endpoint service for the project. When you create a private endpoint service, MongoDB Cloud creates a network container in the project for the cloud provider for which you create the private endpoint service if one doesn't already exist. To learn more about private endpoint terminology in MongoDB Cloud, see Private Endpoint Concepts.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one private endpoint for the specified cloud service provider.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/endpointService"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=EndpointService,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_private_endpoint_endpoint_service(
        self,
        endpoint_service_id: str,
        group_id: str,
        body: ApiAtlasModifyEndpointServiceRequestView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EndpointService:
        """
        Update One Private Endpoint Service for One Provider

        Updates the specified private endpoint service for the project. The cloud service provider manages the private endpoint service that belongs to the project.

        Args:
            endpoint_service_id: Unique 24-hexadecimal digit string that identifies the private endpoint service that you want to update.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates to apply to the private endpoint service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/endpointService/{quote(str(endpoint_service_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=EndpointService,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_private_endpoint_regional_mode(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ProjectSettingItemView:
        """
        Return Regionalized Private Endpoint Status

        Checks whether each region in the specified cloud service provider can create multiple private endpoints per region. The cloud service provider manages the private endpoint for the project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/regionalMode"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ProjectSettingItemView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def toggle_group_private_endpoint_regional_mode(
        self,
        group_id: str,
        body: ProjectSettingItemView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ProjectSettingItemView:
        """
        Toggle Regionalized Private Endpoint Status

        Enables or disables the ability to create multiple private endpoints per region in all cloud service providers in one project. The cloud service provider manages the private endpoints for the project. Connection strings to existing multi-region and global sharded clusters change when you enable this setting. You must update your applications to use the new connection strings. This might cause downtime. Once enabled, you cannot create replica sets. To use this resource, all clusters in the deployment must be sharded clusters.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Enables or disables the ability to create multiple private endpoints per region in all cloud service providers in one project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/regionalMode"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ProjectSettingItemView,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_private_endpoint_endpoint_service(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[EndpointService]:
        """
        Return All Private Endpoint Services for One Provider

        Returns the name, interfaces, and state of all private endpoint services for the specified cloud service provider. This cloud service provider manages the private endpoint service for the project.

        Args:
            cloud_provider: Cloud service provider that manages this private endpoint service.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/{quote(str(cloud_provider), safe='')}/endpointService"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[EndpointService],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_private_endpoint_endpoint_service(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        endpoint_service_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Private Endpoint Service for One Provider

        Removes one private endpoint service from the specified project. This cloud service provider manages the private endpoint service that belongs to the project.

        Args:
            cloud_provider: Cloud service provider that manages this private endpoint service.
            endpoint_service_id: Unique 24-hexadecimal digit string that identifies the private endpoint service that you want to delete.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/{quote(str(cloud_provider), safe='')}/endpointService/{quote(str(endpoint_service_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_private_endpoint_endpoint_service(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        endpoint_service_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EndpointService:
        """
        Return One Private Endpoint Service for One Provider

        Returns the name, interfaces, and state of the specified private endpoint service from one project. The cloud service provider hosted this private endpoint service that belongs to the project.

        Args:
            cloud_provider: Cloud service provider that manages this private endpoint service.
            endpoint_service_id: Unique 24-hexadecimal digit string that identifies the private endpoint service that you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/{quote(str(cloud_provider), safe='')}/endpointService/{quote(str(endpoint_service_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EndpointService,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_group_private_endpoint_endpoint_service_endpoint(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        endpoint_service_id: str,
        group_id: str,
        body: CreateEndpointRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PrivateLinkEndpoint:
        """
        Create One Private Endpoint for One Provider

        Creates one private endpoint for the specified cloud service provider. This cloud service provider manages the private endpoint service, which in turn manages the private endpoints for the project. To learn more about considerations, limitations, and prerequisites, see the MongoDB documentation for setting up a private endpoint.

        Args:
            cloud_provider: Cloud service provider that manages this private endpoint.
            endpoint_service_id: Unique 24-hexadecimal digit string that identifies the private endpoint service for which you want to create a private endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one private endpoint for the specified cloud service provider.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/{quote(str(cloud_provider), safe='')}/endpointService/{quote(str(endpoint_service_id), safe='')}/endpoint"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PrivateLinkEndpoint,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_private_endpoint_endpoint_service_endpoint(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        endpoint_id: str,
        endpoint_service_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Private Endpoint for One Provider

        Removes one private endpoint from the specified project and private endpoint service, as managed by the specified cloud service provider. When the last private endpoint is removed from a given private endpoint service, that private endpoint service is also removed.

        Args:
            cloud_provider: Cloud service provider that manages this private endpoint.
            endpoint_id: Unique string that identifies the private endpoint you want to delete. The format of the `endpointId` parameter differs for AWS and Azure. You must URL encode the `endpointId` for Azure private endpoints.
            endpoint_service_id: Unique 24-hexadecimal digit string that identifies the private endpoint service from which you want to delete a private endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/{quote(str(cloud_provider), safe='')}/endpointService/{quote(str(endpoint_service_id), safe='')}/endpoint/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_private_endpoint_endpoint_service_endpoint(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        endpoint_id: str,
        endpoint_service_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PrivateLinkEndpoint:
        """
        Return One Private Endpoint for One Provider

        Returns the connection state of the specified private endpoint. The private endpoint service manages this private endpoint which belongs to one project hosted from one cloud service provider.

        Args:
            cloud_provider: Cloud service provider that manages this private endpoint.
            endpoint_id: Unique string that identifies the private endpoint you want to return. The format of the `endpointId` parameter differs for AWS and Azure. You must URL encode the `endpointId` for Azure private endpoints.
            endpoint_service_id: Unique 24-hexadecimal digit string that identifies the private endpoint service for which you want to return a private endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/{quote(str(cloud_provider), safe='')}/endpointService/{quote(str(endpoint_service_id), safe='')}/endpoint/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PrivateLinkEndpoint,
            accept="application/vnd.atlas.2023-01-01+json",
        )
