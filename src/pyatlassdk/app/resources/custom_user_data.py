"""Generated resource for CustomUserData. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.custom_user_data_config import CustomUserDataConfig

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class CustomUserData:
    """Configure [custom user data](https://www.mongodb.com/docs/atlas/app-services/users/enable-custom-user-data/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_custom_user_data_config(
        self,
        app_id: str,
        group_id: str,
    ) -> CustomUserDataConfig:
        """
        Get the Custom User Data Configuration

        Get the [Custom User
        Data](https://www.mongodb.com/docs/atlas/app-services/users/enable-custom-user-data/)
        configuration for an Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/custom_user_data"
        return self._client.request(
            method="GET",
            path=path,
            response_model=CustomUserDataConfig,
        )

    def admin_set_custom_user_data_config(
        self,
        app_id: str,
        group_id: str,
        *,
        body: CustomUserDataConfig | None = None,
    ) -> None:
        """
        Configure Custom User Data

        Modify the [Custom User
        Data](https://www.mongodb.com/docs/atlas/app-services/users/enable-custom-user-data/)
        configuration for an Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/custom_user_data"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
