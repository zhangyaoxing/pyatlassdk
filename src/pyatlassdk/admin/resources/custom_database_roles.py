"""Generated resource for CustomDatabaseRoles. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.update_custom_db_role import UpdateCustomDBRole
from pyatlassdk.admin.models.user_custom_db_role import UserCustomDBRole

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class CustomDatabaseRoles:
    """Returns, adds, edits, and removes custom database user privilege roles. Use custom roles to specify custom sets of actions that the MongoDB Cloud built-in roles can't describe. You define custom roles at the project level, for all clusters in the project. This resource supports a subset of MongoDB privilege actions. You can create a subset of custom role actions. To create a wider list of custom role actions, use the MongoDB Cloud user interface. Custom roles must include actions that all project's clusters support, and that are compatible with each MongoDB version that your project's clusters use. For example, if your project has MongoDB 4.2 clusters, you can't create custom roles that use actions introduced in MongoDB 4.4."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_group_custom_db_role_roles(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[UserCustomDBRole]:
        """
        Return All Custom Roles in One Project

        Returns all custom roles for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/customDBRoles/roles"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[UserCustomDBRole],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_group_custom_db_role_role(
        self,
        group_id: str,
        body: UserCustomDBRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserCustomDBRole:
        """
        Create One Custom Role

        Creates one custom role in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one custom role in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/customDBRoles/roles"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=UserCustomDBRole,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_custom_db_role_role(
        self,
        group_id: str,
        role_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Custom Role from One Project

        Removes one custom role from the specified project. You can't remove a custom role that would leave one or more child roles with no parent roles or actions. You also can't remove a custom role that would leave one or more database users without roles.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            role_name: Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/customDBRoles/roles/{quote(str(role_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_custom_db_role_role(
        self,
        group_id: str,
        role_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserCustomDBRole:
        """
        Return One Custom Role in One Project

        Returns one custom role for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            role_name: Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/customDBRoles/roles/{quote(str(role_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=UserCustomDBRole,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_custom_db_role_role(
        self,
        group_id: str,
        role_name: str,
        body: UpdateCustomDBRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserCustomDBRole:
        """
        Update One Custom Role in One Project

        Updates one custom role in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            role_name: Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates one custom role in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/customDBRoles/roles/{quote(str(role_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=UserCustomDBRole,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )
