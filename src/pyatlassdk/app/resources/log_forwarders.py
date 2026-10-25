"""Generated resource for LogForwarders. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.log_forwarder import LogForwarder
from pyatlassdk.app.models.log_forwarder_constructor import LogForwarderConstructor

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class LogForwarders:
    """View and manage your application's [log forwarders](https://www.mongodb.com/docs/atlas/app-services/logs/forward-logs/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def list_log_forwarders(
        self,
        app_id: str,
        group_id: str,
    ) -> list[LogForwarder]:
        """
        List log forwarders.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[LogForwarder],
        )

    def create_log_forwarder(
        self,
        app_id: str,
        group_id: str,
        body: LogForwarderConstructor,
    ) -> LogForwarder:
        """
        Create a log forwarder.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A log forwarder configuration
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=LogForwarder,
            content_type="application/json",
        )

    def delete_gwarder(
        self,
        app_id: str,
        forwarder_id: str,
        group_id: str,
    ) -> None:
        """
        Delete a log forwarder.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            forwarder_id: The _id ObjectID of a log forwarder.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders/{quote(str(forwarder_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def get_log_forwarder(
        self,
        app_id: str,
        forwarder_id: str,
        group_id: str,
    ) -> LogForwarder:
        """
        Get a specific log forwarder.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            forwarder_id: The _id ObjectID of a log forwarder.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders/{quote(str(forwarder_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=LogForwarder,
        )

    def update_log_forwarder(
        self,
        app_id: str,
        forwarder_id: str,
        group_id: str,
        body: LogForwarderConstructor,
    ) -> LogForwarder:
        """
        Update a log forwarder.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            forwarder_id: The _id ObjectID of a log forwarder.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A log forwarder configuration
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders/{quote(str(forwarder_id), safe='')}"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=LogForwarder,
            content_type="application/json",
        )

    def disable_log_forwarder(
        self,
        app_id: str,
        forwarder_id: str,
        group_id: str,
    ) -> None:
        """
        Disable a log forwarder.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            forwarder_id: The _id ObjectID of a log forwarder.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders/{quote(str(forwarder_id), safe='')}/disable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )

    def enable_log_forwarder(
        self,
        app_id: str,
        forwarder_id: str,
        group_id: str,
    ) -> None:
        """
        Enable a log forwarder.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            forwarder_id: The _id ObjectID of a log forwarder.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/log_forwarders/{quote(str(forwarder_id), safe='')}/enable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )
