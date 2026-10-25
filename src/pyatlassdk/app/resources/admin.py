"""Generated resource for Admin. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from pyatlassdk.app.models.admin_user import AdminUser
from pyatlassdk.app.models.base_auth_provider import BaseAuthProvider

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Admin:
    """Log in and adminstrate App Services Apps."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def get_admin_profile(
        self,
    ) -> AdminUser:
        """
        Get information about the currently logged in user
        """
        path = "/auth/profile"
        return self._client.request(
            method="GET",
            path=path,
            response_model=AdminUser,
        )

    def get_admin_auth_providers(
        self,
    ) -> list[BaseAuthProvider]:
        """
        List App Services Admin Auth Providers
        """
        path = "/auth/providers"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[BaseAuthProvider],
        )

    def admin_login(
        self,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Authenticate as an App Services administrator

        Authenticate as an App Services administrator using an Atlas
        programmatic API key pair. To learn more, see [Get An Admin API
        Session Access Token](#get-an-admin-api-session-access-token).

        Args:
            body:
        """
        path = "/auth/providers/mongodb-cloud/login"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_delete_session(
        self,
    ) -> None:
        """
        Delete a session access token
        """
        path = "/auth/session"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_create_session(
        self,
    ) -> dict[str, Any]:
        """
        Obtain a session access token
        """
        path = "/auth/session"
        return self._client.request(
            method="POST",
            path=path,
            response_model=dict[str, Any],
        )
