"""Generated resource for Users. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.user import User

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Users:
    """View and manage your application's [users](https://www.mongodb.com/docs/atlas/app-services/authentication/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_delete_pending_email_password_user(
        self,
        app_id: str,
        email: str,
        group_id: str,
    ) -> None:
        """
        Delete a pending email/password authentication user

        Delete a pending [user](https://www.mongodb.com/docs/atlas/app-services/authentication).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            email: Email address
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/user_registrations/by_email/{quote(str(email), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_list_pending_users(
        self,
        app_id: str,
        group_id: str,
        *,
        after: str | None = None,
    ) -> list[dict[str, Any]]:
        """
        List pending users

        List pending user account registrations. Returns up to 50 pending users in a call.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            after: The unique ``_id`` for a pending user. ``List pending users`` can return 50 pending users at a time. To view additional results, find the ``_id`` of the last pending user listed in the previous call to ``list pending users``. Call ``list pending users`` again, passing the ``_id`` to the after parameter.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/user_registrations/pending_users"
        params = {
            "after": after,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[dict[str, Any]],
        )

    def admin_list_users(
        self,
        app_id: str,
        group_id: str,
        *,
        after: str | None = None,
        desc: bool | None = None,
        sort: str | None = None,
    ) -> list[User]:
        """
        List users

        List confirmed [user accounts](https://www.mongodb.com/docs/atlas/app-services/authentication#std-label-user-accounts).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            after: The `id` of the last user returned by a previous paginated request.
            desc: If `true`, returns sorted results in descending order. If not specified or set to `false`, results return in ascending order.
            sort: The field name to sort results by. The only valid value is the default: `_id`.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users"
        params = {
            "after": after,
            "desc": desc,
            "sort": sort,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[User],
        )

    def admin_create_user(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> User:
        """
        Create a user

        Create a new
        [email/password](https://www.mongodb.com/docs/atlas/app-services/authentication/email-password/)
        user account.

        *Note:* You cannot create user accounts through the Admin API
        for any authentication provider other than email/password.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The user to create
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=User,
            content_type="application/json",
        )

    def admin_verify_user_access_token(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> Literal["token expired"] | dict[str, Any]:
        """
        Verify & decode an access token

        Verify a that a user's client access token is valid.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The user's client access token. The access token represents a logged in application user. This is not the same as the [``access_token``](https://www.mongodb.com/docs/atlas/app-services/admin/api/v3/#section/Get-Authentication-Tokens) that you use to work with the Admin API.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/verify_token"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=Literal["token expired"] | dict[str, Any],
            content_type="application/json",
        )

    def admin_delete_user(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
    ) -> None:
        """
        Delete a user

        Delete a specific [user account](https://www.mongodb.com/docs/atlas/app-services/authentication) by ID.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_user(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
    ) -> User:
        """
        Get a User

        Get a specific [user account](https://www.mongodb.com/docs/atlas/app-services/authentication) by ID.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=User,
        )

    def admin_list_devices(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
    ) -> Any:
        """
        List a user's devices

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}/devices"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_disable_user(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
    ) -> None:
        """
        Disable a user

        Disable a [user](https://www.mongodb.com/docs/atlas/app-services/authentication).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}/disable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )

    def admin_enable_user(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
    ) -> None:
        """
        Enable a user

        Enable a [user](https://www.mongodb.com/docs/atlas/app-services/authentication).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}/enable"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )

    def admin_user_logout(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
    ) -> None:
        """
        Revoke user sessions

        Revoke all of a [user](https://www.mongodb.com/docs/atlas/app-services/authentication)'s
        sessions.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}/logout"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=None,
        )

    def admin_reset_user_email(
        self,
        app_id: str,
        group_id: str,
        user_id: str,
        body: dict[str, Any],
    ) -> None:
        """
        Change a user's email

        Change the email address for an [email/password user](https://www.mongodb.com/docs/atlas/app-services/authentication/email-password/) by ID.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            user_id: User Account ID
            body: The new email address for the user.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/users/{quote(str(user_id), safe='')}/reset_email"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
