"""Generated resource for Webhooks. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.incoming_webhook import IncomingWebhook

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Webhooks:
    """View and manage your application's [webhooks](https://www.mongodb.com/docs/atlas/app-services/services/configure/service-webhooks/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_webhooks(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> IncomingWebhook:
        """
        List webhooks

        List webhooks.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/incoming_webhooks"
        return self._client.request(
            method="GET",
            path=path,
            response_model=IncomingWebhook,
        )

    def admin_create_webhook(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
        body: IncomingWebhook,
    ) -> None:
        """
        Create a webhook

        Create a webhook.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
            body: The webhook to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/incoming_webhooks"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_delete_webhook(
        self,
        app_id: str,
        group_id: str,
        incoming_webhook_id: str,
        service_id: str,
    ) -> None:
        """
        Delete a webhook

        Delete a webhook.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            incoming_webhook_id: The unique `_id` value of an incoming webhook
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/incoming_webhooks/{quote(str(incoming_webhook_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_webhook(
        self,
        app_id: str,
        group_id: str,
        incoming_webhook_id: str,
        service_id: str,
    ) -> None:
        """
        Retrieve a webhook

        Retrieve a webhook.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            incoming_webhook_id: The unique `_id` value of an incoming webhook
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/incoming_webhooks/{quote(str(incoming_webhook_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=None,
        )

    def admin_update_webhook(
        self,
        app_id: str,
        group_id: str,
        incoming_webhook_id: str,
        service_id: str,
        body: IncomingWebhook,
    ) -> None:
        """
        Update a webhook

        Update a webhook.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            incoming_webhook_id: The unique `_id` value of an incoming webhook
            service_id: The unique `_id` value of a service.
            body: The updated state of the webhook.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/incoming_webhooks/{quote(str(incoming_webhook_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
