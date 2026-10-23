"""Generated resource for ServerlessPrivateEndpoints. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.serverless_tenant_create_request import ServerlessTenantCreateRequest
from pyatlassdk.models.serverless_tenant_endpoint import ServerlessTenantEndpoint
from pyatlassdk.models.serverless_tenant_endpoint_update import ServerlessTenantEndpointUpdate

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ServerlessPrivateEndpoints:
    """Returns, adds, edits, and removes private endpoints for serverless instances. To learn more, see the Atlas Administration API tab on the following tutorial."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_private_endpoint_serverless_instance_endpoint(
        self,
        group_id: str,
        instance_name: str,
        *,
        envelope: bool | None = None,
    ) -> list[ServerlessTenantEndpoint]:
        """
        Return All Private Endpoints for One Serverless Instance

        Returns all private endpoints for one serverless instance. You must have at least the Project Read Only role for the project to successfully call this resource.

        This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            instance_name: Human-readable label that identifies the serverless instance associated with the tenant endpoint.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/serverless/instance/{quote(str(instance_name), safe='')}/endpoint"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[ServerlessTenantEndpoint],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_group_private_endpoint_serverless_instance_endpoint(
        self,
        group_id: str,
        instance_name: str,
        body: ServerlessTenantCreateRequest,
        *,
        envelope: bool | None = None,
    ) -> ServerlessTenantEndpoint:
        """
        Create One Private Endpoint for One Serverless Instance

        Creates one private endpoint for one serverless instance. 

         A new endpoint won't be immediately available after creation.  Read the steps in the linked tutorial for detailed guidance.

        This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            instance_name: Human-readable label that identifies the serverless instance for which the tenant endpoint will be created.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Information about the Private Endpoint to create for the Serverless Instance.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/serverless/instance/{quote(str(instance_name), safe='')}/endpoint"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ServerlessTenantEndpoint,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_private_endpoint_serverless_instance_endpoint(
        self,
        endpoint_id: str,
        group_id: str,
        instance_name: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Private Endpoint for One Serverless Instance

        Remove one private endpoint from one serverless instance. 

        This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.

        Args:
            endpoint_id: Unique 24-hexadecimal digit string that identifies the tenant endpoint which will be removed.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            instance_name: Human-readable label that identifies the serverless instance from which the tenant endpoint will be removed.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/serverless/instance/{quote(str(instance_name), safe='')}/endpoint/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_private_endpoint_serverless_instance_endpoint(
        self,
        endpoint_id: str,
        group_id: str,
        instance_name: str,
        *,
        envelope: bool | None = None,
    ) -> ServerlessTenantEndpoint:
        """
        Return One Private Endpoint for One Serverless Instance

        Return one private endpoint for one serverless instance. Identify this endpoint using its unique ID. You must have at least the Project Read Only role for the project to successfully call this resource.

        This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.

        Args:
            endpoint_id: Unique 24-hexadecimal digit string that identifies the tenant endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            instance_name: Human-readable label that identifies the serverless instance associated with the tenant endpoint.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/serverless/instance/{quote(str(instance_name), safe='')}/endpoint/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ServerlessTenantEndpoint,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_private_endpoint_serverless_instance_endpoint(
        self,
        endpoint_id: str,
        group_id: str,
        instance_name: str,
        body: ServerlessTenantEndpointUpdate,
        *,
        envelope: bool | None = None,
    ) -> ServerlessTenantEndpoint:
        """
        Update One Private Endpoint for One Serverless Instance

        Updates one private endpoint for one serverless instance. 

        This feature does not work for Flex clusters. To continue using Private Endpoints once Serverless is replaced by Flex, please use a Dedicated cluster instead. This endpoint will be sunset on January 22, 2026.

        Args:
            endpoint_id: Unique 24-hexadecimal digit string that identifies the tenant endpoint which will be updated.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            instance_name: Human-readable label that identifies the serverless instance associated with the tenant endpoint that will be updated.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Object used for update.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateEndpoint/serverless/instance/{quote(str(instance_name), safe='')}/endpoint/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ServerlessTenantEndpoint,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )
