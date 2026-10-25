"""Generated resource for Email. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Email:
    """Confirm pending users with the built-in email confirmation flow."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_confirm_pending_user(
        self,
        app_id: str,
        email: str,
        group_id: str,
    ) -> None:
        """
        Confirm a pending user

        Confirm a pending [user](https://www.mongodb.com/docs/atlas/app-services/authentication).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            email: Email address
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/user_registrations/by_email/{quote(str(email), safe='')}/confirm"
        return self._client.request(
            method="POST",
            path=path,
            response_model=None,
        )

    def admin_rerun_pending_user_confirmation(
        self,
        app_id: str,
        email: str,
        group_id: str,
    ) -> None:
        """
        Rerun a user confirmation workflow

        Reruns a pending user's [confirmation workflow](https://www.mongodb.com/docs/atlas/app-services/authentication).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            email: Email address
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/user_registrations/by_email/{quote(str(email), safe='')}/run_confirm"
        return self._client.request(
            method="POST",
            path=path,
            response_model=None,
        )

    def admin_send_confirmation_email(
        self,
        app_id: str,
        email: str,
        group_id: str,
    ) -> None:
        """
        Send a confirmation email

        Send a [confirmation
        email](https://www.mongodb.com/docs/atlas/app-services/authentication/email-password/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            email: Email address
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/user_registrations/by_email/{quote(str(email), safe='')}/send_confirm"
        return self._client.request(
            method="POST",
            path=path,
            response_model=None,
        )
