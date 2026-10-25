"""Generated resource for EventSubscriptions. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.event_subscription import EventSubscription

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class EventSubscriptions:
    """
    View your app's active event subscriptions. These monitor
    real-time events, e.g. from a MongoDB change stream, to power
    application services like Triggers and Device Sync.
    """

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_event_subscriptions(
        self,
        app_id: str,
        group_id: str,
        *,
        type: Literal["DATABASE", "AUTHENTICATION", "SCHEDULED", "SYNCTRANSLATOR"] | None = None,
    ) -> list[EventSubscription]:
        """
        List Event Subscriptions

        Get all event subscriptions.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            type: The type of event subscription to return. - `DATABASE`: Return Database Triggers - `AUTHENTICATION`: Return Authentication Triggers - `SCHEDULED`: Return Scheduled Triggers - `SYNCTRANSLATOR`: Return Device Sync translators
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/event_subscriptions"
        params = {
            "type": type,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[EventSubscription],
        )

    def admin_get_event_subscription(
        self,
        app_id: str,
        event_subscription_id: str,
        group_id: str,
    ) -> EventSubscription:
        """
        Get an Event Subscription

        Return information about an event subscription.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            event_subscription_id: The unique `_id` value of an event subscription.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/event_subscriptions/{quote(str(event_subscription_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=EventSubscription,
        )

    def admin_get_latest_event_subscription_execution(
        self,
        app_id: str,
        event_subscription_id: str,
        group_id: str,
    ) -> dict[str, Any]:
        """
        Get the Latest Event Subscription Execution

        Return information about the most recent execution of an event subscription.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            event_subscription_id: The unique `_id` value of an event subscription.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/event_subscriptions/{quote(str(event_subscription_id), safe='')}/execution"
        return self._client.request(
            method="GET",
            path=path,
            response_model=dict[str, Any],
        )
