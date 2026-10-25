"""Generated resource for Secrets. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Secrets:
    """View and manage your application's [secrets](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_all_secrets(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List secrets

        List [secrets](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/define-and-manage-secrets/#define-a-secret)
        associated with a Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/secrets"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_a_secret(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create a new Secret

        Create a new
        [Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/define-and-manage-secrets).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The Secret to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/secrets"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_delete_secret(
        self,
        app_id: str,
        group_id: str,
        secret_id: str,
    ) -> None:
        """
        Delete a Secret

        Delete a
        [Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/define-and-manage-secrets)
        associated with a Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            secret_id: The unique `_id` value of a secret.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_modify_a_secret(
        self,
        app_id: str,
        group_id: str,
        secret_id: str,
        body: dict[str, Any],
    ) -> None:
        """
        Modify a Secret

        Modify a
        [Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/define-and-manage-secrets)
        associated with a Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            secret_id: The unique `_id` value of a secret.
            body: The modified value of the Secret.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/secrets/{quote(str(secret_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
