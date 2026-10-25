"""Generated resource for Triggers. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.trigger import Trigger
from pyatlassdk.app.models.trigger_constructor import TriggerConstructor

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Triggers:
    """View and manage your application's [triggers](https://www.mongodb.com/docs/atlas/app-services/triggers/overview/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_triggers(
        self,
        app_id: str,
        group_id: str,
    ) -> list[Trigger]:
        """
        Get all triggers

        Get a list of all [triggers](https://www.mongodb.com/docs/atlas/app-services/triggers/overview/) in your application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/triggers"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[Trigger],
        )

    def admin_create_trigger(
        self,
        app_id: str,
        group_id: str,
        body: TriggerConstructor,
    ) -> Trigger:
        """
        Create a trigger

        Create a new [trigger](https://www.mongodb.com/docs/atlas/app-services/triggers/overview/) in your application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A configuration for a database, scheduled, or authentication trigger.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/triggers"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=Trigger,
            content_type="application/json",
        )

    def admin_delete_trigger(
        self,
        app_id: str,
        group_id: str,
        trigger_id: str,
    ) -> dict[str, Any]:
        """
        Delete a trigger

        Remove an existing [trigger](https://www.mongodb.com/docs/atlas/app-services/triggers/overview/) from your application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            trigger_id: The unique `_id` value of a trigger.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/triggers/{quote(str(trigger_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=dict[str, Any],
        )

    def admin_get_trigger(
        self,
        app_id: str,
        group_id: str,
        trigger_id: str,
    ) -> Trigger:
        """
        Get a trigger

        Get the configuration for an existing [trigger](https://www.mongodb.com/docs/atlas/app-services/triggers/overview/) in your application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            trigger_id: The unique `_id` value of a trigger.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/triggers/{quote(str(trigger_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Trigger,
        )

    def admin_update_trigger(
        self,
        app_id: str,
        group_id: str,
        trigger_id: str,
        body: Trigger,
    ) -> None:
        """
        Update a trigger

        Modify an existing [trigger](https://www.mongodb.com/docs/atlas/app-services/triggers/overview/) in your application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            trigger_id: The unique `_id` value of a trigger.
            body: The updated trigger configuration.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/triggers/{quote(str(trigger_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_resume_trigger(
        self,
        app_id: str,
        group_id: str,
        trigger_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> None:
        """
        Resume a suspended trigger

        Resume a [suspended](https://www.mongodb.com/docs/atlas/app-services/triggers/database-triggers/#suspended-triggers) database trigger.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            trigger_id: The unique `_id` value of a trigger.
            body: Configuration options for the resume operation.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/triggers/{quote(str(trigger_id), safe='')}/resume"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
