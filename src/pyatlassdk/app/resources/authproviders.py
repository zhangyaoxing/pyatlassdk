"""Generated resource for Authproviders. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.auth_provider import AuthProvider
from pyatlassdk.app.models.auth_provider_constructor import AuthProviderConstructor

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Authproviders:
    """View and manage [authentication providers](https://www.mongodb.com/docs/atlas/app-services/authentication/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_auth_providers(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List authentication providers in a Atlas App Services App

        List [authentication providers](https://www.mongodb.com/docs/atlas/app-services/authentication/)
        within a Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_auth_provider(
        self,
        app_id: str,
        group_id: str,
        body: AuthProviderConstructor,
    ) -> AuthProvider:
        """
        Create an authentication provider

        Create an [authentication provider](https://www.mongodb.com/docs/atlas/app-services/authentication/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=AuthProvider,
            content_type="application/json",
        )

    def admin_delete_auth_provider(
        self,
        app_id: str,
        group_id: str,
        provider_id: str,
    ) -> None:
        """
        Delete an authentication provider

        Delete an [authentication provider](https://www.mongodb.com/docs/atlas/app-services/authentication/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            provider_id: The unique `_id` value of an authentication provider
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers/{quote(str(provider_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_auth_provider(
        self,
        app_id: str,
        group_id: str,
        provider_id: str,
    ) -> AuthProvider:
        """
        Retrieve information about authentication provider

        Retrieve information about one of an application's [authentication
        providers](https://www.mongodb.com/docs/atlas/app-services/authentication/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            provider_id: The unique `_id` value of an authentication provider
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers/{quote(str(provider_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=AuthProvider,
        )

    def admin_update_auth_provider(
        self,
        app_id: str,
        group_id: str,
        provider_id: str,
        body: AuthProviderConstructor,
    ) -> None:
        """
        Update an authentication provider

        Update an [authentication provider](https://www.mongodb.com/docs/atlas/app-services/authentication/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            provider_id: The unique `_id` value of an authentication provider
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers/{quote(str(provider_id), safe='')}"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_disable_auth_provider(
        self,
        app_id: str,
        group_id: str,
        provider_id: str,
    ) -> None:
        """
        Disable an authentication provider

        Disable an [authentication provider](https://www.mongodb.com/docs/atlas/app-services/authentication/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            provider_id: The unique `_id` value of an authentication provider
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers/{quote(str(provider_id), safe='')}/disable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )

    def admin_enable_auth_provider(
        self,
        app_id: str,
        group_id: str,
        provider_id: str,
    ) -> None:
        """
        Enable an authentication provider

        Enable an [authentication provider](https://www.mongodb.com/docs/atlas/app-services/authentication/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            provider_id: The unique `_id` value of an authentication provider
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/auth_providers/{quote(str(provider_id), safe='')}/enable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )
