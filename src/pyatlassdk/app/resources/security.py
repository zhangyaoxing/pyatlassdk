"""Generated resource for Security. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.private_endpoint import PrivateEndpoint
from pyatlassdk.app.models.private_endpoint_create import PrivateEndpointCreate
from pyatlassdk.app.models.private_endpoint_service_info import PrivateEndpointServiceInfo
from pyatlassdk.app.models.refresh_token_expiration import RefreshTokenExpiration

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Security:
    """Configure your application's [security](https://www.mongodb.com/docs/atlas/app-services/security/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def allowed_ip_access_list_get(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List the allowed entries in the Access List

        List the allowed entries in the Access List of your Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/access_list"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def allowed_ip_access_list_create(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create an IP address or CIDR block in the Access List

        Create an IP address or CIDR block in the Access List for your App Services
        app.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The IP Access List entry to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/access_list"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def allowed_ip_access_list_delete(
        self,
        app_id: str,
        group_id: str,
        ip_id: str,
    ) -> None:
        """
        Delete an IP address or CIDR block from the Access List

        Delete an IP address or CIDR block from the Access List of your App Services
        app

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            ip_id: The IP address entry denoted by `ip_id` with the information given in the request body
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/access_list/{quote(str(ip_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def allowed_ip_access_list_update(
        self,
        app_id: str,
        group_id: str,
        ip_id: str,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Modify an IP address or CIDR block in the Access List

        Modify an IP address or CIDR block in the Access List of your App Services
        app

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            ip_id: The IP address entry denoted by `ip_id` with the information given in the request body
            body: The updated value of the IP Access List entry.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/access_list/{quote(str(ip_id), safe='')}"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def allow_non_vpc_client_requests(
        self,
        app_id: str,
        group_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> None:
        """
        Toggle Non-VPC Requests

        For Apps with Private Endpoints enabled, toggle whether or not the App processes requests that originate from outside of the VPC.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/allow_non_vpc_client_requests"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_list_allowed_request_origins(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List allowed HTTP origins

        List the allowed [HTTP
        origins](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)
        from which App Services should allow requests.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/allowed_request_origins"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_set_allowed_request_origins(
        self,
        app_id: str,
        group_id: str,
        body: Any,
    ) -> None:
        """
        Set allowed HTTP origins

        Set the allowed [HTTP
        origins](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)
        from which App Services should allow requests.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A list of HTTP origins.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/allowed_request_origins"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_list_private_endpoint_services(
        self,
        app_id: str,
        group_id: str,
    ) -> list[PrivateEndpointServiceInfo]:
        """
        List VPC Private Endpoint Services

        Get a list of all private endpoint services configured for the App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/private_endpoint_service_infos"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[PrivateEndpointServiceInfo],
        )

    def admin_get_private_endpoints(
        self,
        app_id: str,
        group_id: str,
    ) -> list[PrivateEndpoint]:
        """
        List VPC Private Endpoints

        Get a list of all private endpoints configured for the App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/private_endpoints"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[PrivateEndpoint],
        )

    def admin_create_private_endpoint(
        self,
        app_id: str,
        group_id: str,
        body: PrivateEndpointCreate,
    ) -> PrivateEndpoint:
        """
        Create a VPC Private Endpoint

        Configure a new private endpoint for the App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/private_endpoints"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=PrivateEndpoint,
            content_type="application/json",
        )

    def admin_delete_private_endpoint(
        self,
        app_id: str,
        group_id: str,
        private_endpoint_id: str,
    ) -> None:
        """
        Delete a VPC Private Endpoint

        Delete a private endpoint.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            private_endpoint_id: The _id ObjectID of a VPC private endpoint.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/private_endpoints/{quote(str(private_endpoint_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_private_endpoint(
        self,
        app_id: str,
        group_id: str,
        private_endpoint_id: str,
    ) -> PrivateEndpoint:
        """
        Get a VPC Private Endpoint

        Get a specific private endpoint configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            private_endpoint_id: The _id ObjectID of a VPC private endpoint.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/private_endpoints/{quote(str(private_endpoint_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=PrivateEndpoint,
        )

    def admin_update_private_endpoint(
        self,
        app_id: str,
        group_id: str,
        private_endpoint_id: str,
        body: PrivateEndpointCreate,
    ) -> PrivateEndpoint:
        """
        Modify a VPC Private Endpoint

        Update the configuration of a private endpoint.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            private_endpoint_id: The _id ObjectID of a VPC private endpoint.
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/private_endpoints/{quote(str(private_endpoint_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=PrivateEndpoint,
            content_type="application/json",
        )

    def admin_get_refresh_token_expiration(
        self,
        app_id: str,
        group_id: str,
    ) -> RefreshTokenExpiration:
        """
        Get User Refresh Token Expiration Time

        Get the current expiration time in seconds for user session refresh tokens.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/refresh_token_expiration"
        return self._client.request(
            method="GET",
            path=path,
            response_model=RefreshTokenExpiration,
        )

    def admin_set_refresh_token_expiration(
        self,
        app_id: str,
        group_id: str,
        body: RefreshTokenExpiration,
    ) -> None:
        """
        Set User Refresh Token Expiration Time

        Set the expiration time in seconds for user session refresh tokens.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/security/refresh_token_expiration"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
