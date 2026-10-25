"""Generated resource for Values. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.new_value import NewValue
from pyatlassdk.app.models.value import Value

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Values:
    """View and manage your application's [values](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_values(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List all values defined in an application.

        List all [values](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets)
        defined in an application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/values"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_value(
        self,
        app_id: str,
        group_id: str,
        body: NewValue,
    ) -> NewValue:
        """
        Define a Value in an application

        Define a [Value](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets) in
        an application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The value to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/values"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=NewValue,
            content_type="application/json",
        )

    def admin_delete_value(
        self,
        app_id: str,
        group_id: str,
        value_id: str,
    ) -> None:
        """
        Delete a value defined in an application.

        Delete a [value](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets)
        defined in an application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            value_id: The unique `_id` value of a value.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/values/{quote(str(value_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_value(
        self,
        app_id: str,
        group_id: str,
        value_id: str,
    ) -> Value:
        """
        Retrieve a value definition from an application

        Retrieve a [value](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets)
        definition from an application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            value_id: The unique `_id` value of a value.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/values/{quote(str(value_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Value,
        )

    def admin_update_value(
        self,
        app_id: str,
        group_id: str,
        value_id: str,
    ) -> Any:
        """
        Update a value definition in an application

        Update a [value](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets)
        definition in an application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            value_id: The unique `_id` value of a value.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/values/{quote(str(value_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=Any,
        )
