"""Generated resource for Environments. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.app_instance import AppInstance
from pyatlassdk.app.models.environment_value import EnvironmentValue
from pyatlassdk.app.models.environment_value_description import EnvironmentValueDescription

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Environments:
    """View and manage your app's [environment](https://www.mongodb.com/docs/atlas/app-services/apps/environment/) and environment values."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_set_environment(
        self,
        app_id: str,
        group_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> AppInstance:
        """
        Set the App Environment

        Set the App's active environment

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/environment"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=AppInstance,
            content_type="application/json",
        )

    def admin_list_environment_values(
        self,
        app_id: str,
        group_id: str,
    ) -> list[EnvironmentValueDescription]:
        """
        List All Environment Values

        Get basic information about all environment values in the App.
        Results do not include the environment-specific `values`. For
        details on a specific environment, call [Get an Environment
        Value](#tag/environments/operation/adminGetEnvironmentValue).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/environment_values"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[EnvironmentValueDescription],
        )

    def admin_create_environment_value(
        self,
        app_id: str,
        group_id: str,
        *,
        body: EnvironmentValue | None = None,
    ) -> EnvironmentValueDescription:
        """
        Create an Environment Value

        Define a new environment value.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/environment_values"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=EnvironmentValueDescription,
            content_type="application/json",
        )

    def admin_delete_environment_value(
        self,
        app_id: str,
        environment_value_id: str,
        group_id: str,
    ) -> None:
        """
        Delete an Environment Value

        Delete an existing environment value

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            environment_value_id: The `_id` value of an environment value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/environment_values/{quote(str(environment_value_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_environment_value(
        self,
        app_id: str,
        environment_value_id: str,
        group_id: str,
    ) -> EnvironmentValue:
        """
        Get an Environment Value

        Get details about a specific environment value

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            environment_value_id: The `_id` value of an environment value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/environment_values/{quote(str(environment_value_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=EnvironmentValue,
        )

    def admin_modify_environment_value(
        self,
        app_id: str,
        environment_value_id: str,
        group_id: str,
        *,
        body: EnvironmentValue | None = None,
    ) -> EnvironmentValueDescription:
        """
        Modify an Environment Value

        Modify an existing environment value

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            environment_value_id: The `_id` value of an environment value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/environment_values/{quote(str(environment_value_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=EnvironmentValueDescription,
            content_type="application/json",
        )
