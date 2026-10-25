"""Generated resource for Notifications. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.message import Message
from pyatlassdk.app.models.new_message import NewMessage

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Notifications:
    """View and manage your application's [push notifications](https://www.mongodb.com/docs/atlas/app-services/push-notifications/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_notifications(
        self,
        app_id: str,
        group_id: str,
        *,
        state: Literal["sent", "draft"] | None = None,
    ) -> Any:
        """
        List push notifications

        List [push notifications](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            state: Only list notifications with the given state.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications"
        params = {
            "state": state,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=Any,
        )

    def admin_create_notification(
        self,
        app_id: str,
        group_id: str,
        body: NewMessage,
    ) -> None:
        """
        Create a push notification

        Create a [push
        notification](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The notification to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_delete_message(
        self,
        app_id: str,
        group_id: str,
        message_id: str,
    ) -> None:
        """
        Delete a push notification message

        Delete a [push
        notification](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications)
        message.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            message_id: Message ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications/{quote(str(message_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_message(
        self,
        app_id: str,
        group_id: str,
        message_id: str,
    ) -> Message:
        """
        Retrieve a push notification message

        Retrieve a [push
        notification](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications)
        message.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            message_id: Message ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications/{quote(str(message_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Message,
        )

    def admin_update_message(
        self,
        app_id: str,
        group_id: str,
        message_id: str,
    ) -> Message:
        """
        Update a push notification

        Update a [push
        notification](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications)
        message.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            message_id: Message ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications/{quote(str(message_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=Message,
        )

    def admin_send_message(
        self,
        app_id: str,
        group_id: str,
        message_id: str,
    ) -> None:
        """
        Send a push notification

        Send a [push
        notification](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            message_id: Message ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications/{quote(str(message_id), safe='')}/send"
        return self._client.request(
            method="POST",
            path=path,
            response_model=None,
        )

    def admin_set_message_type(
        self,
        app_id: str,
        group_id: str,
        message_id: str,
    ) -> None:
        """
        Set a push notification's type

        Set a [push
        notification's](https://www.mongodb.com/docs/atlas/app-services/reference/push-notifications)
        type.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            message_id: Message ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push/notifications/{quote(str(message_id), safe='')}/type"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )
