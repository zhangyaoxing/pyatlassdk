"""Generated resource for Teams. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.add_user_to_team import AddUserToTeam
from pyatlassdk.admin.models.paginated_api_app_user_view import PaginatedApiAppUserView
from pyatlassdk.admin.models.paginated_team_role_view import PaginatedTeamRoleView
from pyatlassdk.admin.models.paginated_team_view import PaginatedTeamView
from pyatlassdk.admin.models.team import Team
from pyatlassdk.admin.models.team_response import TeamResponse
from pyatlassdk.admin.models.team_role import TeamRole
from pyatlassdk.admin.models.team_update import TeamUpdate

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class Teams:
    """Returns, adds, edits, or removes teams."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_group_teams(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedTeamRoleView:
        """
        Return All Teams in One Project

        Returns all teams to which the authenticated user has access in the project specified using its unique 24-hexadecimal digit identifier. All members of the team share the same project access.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/teams"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedTeamRoleView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def add_group_teams(
        self,
        group_id: str,
        body: list[TeamRole],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedTeamRoleView:
        """
        Add Multiple Teams to One Project

        Adds multiple teams to the specified project. All members of a team share the same project access. MongoDB Cloud limits the number of users to a maximum of 100 teams per project and a maximum of 250 teams per organization.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Teams and their roles to be added to the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/teams"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedTeamRoleView,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def remove_group_team(
        self,
        group_id: str,
        team_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Team from One Project

        Removes one team specified using its unique 24-hexadecimal digit identifier from the project specified using its unique 24-hexadecimal digit identifier.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            team_id: Unique 24-hexadecimal digit string that identifies the team that you want to remove from the specified project.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/teams/{quote(str(team_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_team(
        self,
        group_id: str,
        team_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> TeamRole:
        """
        Return One Team in One Project

        Returns one team to which the authenticated user has access in the project specified using its unique 24-hexadecimal digit identifier. All members of the team share the same project access.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            team_id: Unique 24-hexadecimal digit string that identifies the team for which you want to get.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/teams/{quote(str(team_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=TeamRole,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_team(
        self,
        group_id: str,
        team_id: str,
        body: TeamRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedTeamRoleView:
        """
        Update Team Roles in One Project

        Updates the project roles assigned to the specified team. You can grant team roles for specific projects and grant project access roles to users in the team. All members of the team share the same project access.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            team_id: Unique 24-hexadecimal digit string that identifies the team for which you want to update roles.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The project roles assigned to the specified team.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/teams/{quote(str(team_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedTeamRoleView,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def list_org_teams(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedTeamView:
        """
        Return All Teams in One Organization

        Returns all teams that belong to the specified organization. Teams enable you to grant project access roles to MongoDB Cloud users. MongoDB Cloud only returns teams for which you have access.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedTeamView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_org_team(
        self,
        org_id: str,
        body: Team,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Team:
        """
        Create One Team in One Organization

        Creates one team in the specified organization. Teams enable you to grant project access roles to MongoDB Cloud users. MongoDB Cloud limits the number of teams to a maximum of 250 teams per organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Team that you want to create in the specified organization.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Team,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_org_team_by_name(
        self,
        org_id: str,
        team_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> TeamResponse:
        """
        Return One Team by Name

        Returns one team that you identified using its human-readable name. This team belongs to one organization. Teams enable you to grant project access roles to MongoDB Cloud users.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_name: Name of the team whose information you want to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams/byName/{quote(str(team_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=TeamResponse,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def delete_org_team(
        self,
        org_id: str,
        team_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Team from One Organization

        Removes one team specified using its unique 24-hexadecimal digit identifier from the organization specified using its unique 24-hexadecimal digit identifier.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team that you want to delete.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}"
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

    def get_org_team(
        self,
        org_id: str,
        team_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> TeamResponse:
        """
        Return One Team by ID

        Returns one team that you identified using its unique 24-hexadecimal digit ID. This team belongs to one organization. Teams enable you to grant project access roles to MongoDB Cloud users.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team whose information you want to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=TeamResponse,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def rename_org_team(
        self,
        org_id: str,
        team_id: str,
        body: TeamUpdate,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> TeamResponse:
        """
        Rename One Team

        Renames one team in the specified organization. Teams enable you to grant project access roles to MongoDB Cloud users.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team that you want to rename.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update on the specified team.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=TeamResponse,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def add_org_team_users(
        self,
        org_id: str,
        team_id: str,
        body: list[AddUserToTeam],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAppUserView:
        """
        Assign MongoDB Cloud Users in One Organization to One Team

        Adds one or more MongoDB Cloud users from the specified organization to the specified team. Teams enable you to grant project access roles to MongoDB Cloud users. You can assign up to 250 MongoDB Cloud users from one organization to one team.

        **Note**: This endpoint is deprecated. Use [Add One MongoDB Cloud User to One Team](#tag/MongoDB-Cloud-Users/operation/addUserToTeam) to add an active or pending user to a team.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal character string that identifies the team to which you want to add MongoDB Cloud users.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: One or more MongoDB Cloud users that you want to add to the specified team.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}/users"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedApiAppUserView,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def remove_org_team_user_from_team(
        self,
        org_id: str,
        team_id: str,
        user_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One MongoDB Cloud User from One Team

        Removes one MongoDB Cloud user from the specified team. This team belongs to one organization. Teams enable you to grant project access roles to MongoDB Cloud users. 

        **Note**: This endpoint is deprecated. Use [Remove One MongoDB Cloud User from One Team](#tag/MongoDB-Cloud-Users/operation/removeUserFromTeam) to remove an active or pending user from a team.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team from which you want to remove one database application user.
            user_id: Unique 24-hexadecimal digit string that identifies MongoDB Cloud user that you want to remove from the specified team.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}/users/{quote(str(user_id), safe='')}"
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
