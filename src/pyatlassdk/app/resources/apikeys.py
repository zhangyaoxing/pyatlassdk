"""Generated resource for Apikeys. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.api_key import ApiKey
from pyatlassdk.app.models.api_key_response import ApiKeyResponse

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Apikeys:
    """View and manage API keys through the [API Key provider](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_api_keys(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List API keys

        List [API keys](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key)
        associated with a Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/api_keys"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_api_key(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> ApiKey:
        """
        Create a new API key

        Create a new [API key](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The API key to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/api_keys"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=ApiKey,
            content_type="application/json",
        )

    def admin_delete_api_key(
        self,
        api_key_id: str,
        app_id: str,
        group_id: str,
    ) -> None:
        """
        Delete an API key

        Delete an [API key](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key).

        Args:
            api_key_id: The unique `_id` value of an API key
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/api_keys/{quote(str(api_key_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_api_key(
        self,
        api_key_id: str,
        app_id: str,
        group_id: str,
    ) -> ApiKeyResponse:
        """
        Retrieve information about an API key

        Retrieve information about an [API key](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key).

        Args:
            api_key_id: The unique `_id` value of an API key
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/api_keys/{quote(str(api_key_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=ApiKeyResponse,
        )

    def admin_disable_api_key(
        self,
        api_key_id: str,
        app_id: str,
        group_id: str,
    ) -> None:
        """
        Disable an API key

        Disable an [API key](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key).

        Args:
            api_key_id: The unique `_id` value of an API key
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/api_keys/{quote(str(api_key_id), safe='')}/disable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )

    def admin_enable_api_key(
        self,
        api_key_id: str,
        app_id: str,
        group_id: str,
    ) -> None:
        """
        Enable an API key

        Enable an [API key](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key).

        Args:
            api_key_id: The unique `_id` value of an API key
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/api_keys/{quote(str(api_key_id), safe='')}/enable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )
