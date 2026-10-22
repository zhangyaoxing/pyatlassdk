"""Generated resource for MongoDBCloudUsers. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.add_or_remove_group_role import AddOrRemoveGroupRole
from pyatlassdk.models.add_or_remove_org_role import AddOrRemoveOrgRole
from pyatlassdk.models.add_or_remove_user_from_team import AddOrRemoveUserFromTeam
from pyatlassdk.models.cloud_app_user import CloudAppUser
from pyatlassdk.models.group_user_request import GroupUserRequest
from pyatlassdk.models.group_user_response import GroupUserResponse
from pyatlassdk.models.org_user_request import OrgUserRequest
from pyatlassdk.models.org_user_response import OrgUserResponse
from pyatlassdk.models.org_user_update_request import OrgUserUpdateRequest
from pyatlassdk.models.paginated_group_user_view import PaginatedGroupUserView
from pyatlassdk.models.paginated_org_user_view import PaginatedOrgUserView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class MongoDBCloudUsers:
    """Returns, adds, and edits MongoDB Cloud users."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_users(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        flatten_teams: bool | None = None,
        include_count: bool | None = None,
        include_org_users: bool | None = None,
        items_per_page: int | None = None,
        org_membership_status: str | None = None,
        org_membership_statuses: list[Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"]] | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        username: str | None = None,
    ) -> PaginatedGroupUserView:
        """
        Return All MongoDB Cloud Users in One Project

        Returns details about the pending and active MongoDB Cloud users associated with the specified project. 

        **Note**: This resource cannot be used to view details about users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        **Note**: To return both pending and active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users will be returned. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            flatten_teams: Flag that indicates whether the returned list should include users who belong to a team with a role in this project. You might not have assigned the individual users a role in this project. If `"flattenTeams" : false`, this resource returns only users with a role in the project. If `"flattenTeams" : true`, this resource returns both users with roles in the project and users who belong to teams with roles in the project.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            include_org_users: Flag that indicates whether the returned list should include users with implicit access to the project, the Organization Owner or Organization Read Only role. You might not have assigned the individual users a role in this project. If `"includeOrgUsers": false`, this resource returns only users with a role in the project. If `"includeOrgUsers": true`, this resource returns both users with roles in the project and users who have implicit access to the project through their organization role.
            items_per_page: Number of items that the response returns per page.
            org_membership_status: Deprecated: Use `orgMembershipStatuses` instead. Organization membership status to filter users by. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Not supported in deprecated versions.
            org_membership_statuses: Organization membership status to filter users by. You can supply this parameter multiple times. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. Replaces the deprecated `orgMembershipStatus` parameter. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Cannot be combined with `orgMembershipStatus`. Not supported in deprecated versions.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            username: Email address to filter users by. Not supported in deprecated versions.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/users"
        params = {
            "envelope": envelope,
            "flattenTeams": flatten_teams,
            "includeCount": include_count,
            "includeOrgUsers": include_org_users,
            "itemsPerPage": items_per_page,
            "orgMembershipStatus": org_membership_status,
            "orgMembershipStatuses": org_membership_statuses,
            "pageNum": page_num,
            "pretty": pretty,
            "username": username,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedGroupUserView,
        )

    def add_group_users(
        self,
        group_id: str,
        body: GroupUserRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupUserResponse:
        """
        Add One MongoDB Cloud User to One Project

        Adds one MongoDB Cloud user to one project. 
        - If the user has a pending invitation to join the project's organization, MongoDB Cloud modifies it and grants project access. 
        - If the user doesn't have an invitation to join the organization, MongoDB Cloud sends a new invitation that grants the user organization and project access. 
        - If the user is already active in the project's organization, MongoDB Cloud grants access to the project. 
        - Replaces `INVITATION_EXPIRED` and `INVITATION_REJECTED` user with the same email. A conflict, if and only if, there is an existing `PENDING` or `ACTIVE` user.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The active or pending MongoDB Cloud user that you want to add to the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/users"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupUserResponse,
        )

    def remove_group_user(
        self,
        group_id: str,
        user_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One MongoDB Cloud User from One Project

        Removes one MongoDB Cloud user from the specified project. You can remove an active user or a user that has not yet accepted the invitation to join the organization.

        **Note**: This resource cannot be used to remove pending users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        **Note**: To remove pending or active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users can be removed. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the [Return All MongoDB Cloud Users in One Project](#tag/MongoDB-Cloud-Users/operation/listProjectUsers) resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/users/{quote(str(user_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_user(
        self,
        group_id: str,
        user_id: str,
        *,
        envelope: bool | None = None,
        org_membership_statuses: list[Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"]] | None = None,
        pretty: bool | None = None,
    ) -> GroupUserResponse:
        """
        Return One MongoDB Cloud User in One Project

        Returns information about the specified MongoDB Cloud user within the context of the specified project. 

        **Note**: You can only use this resource to fetch information about MongoDB Cloud human users. To return information about an API Key, use the [Return One Organization API Key](#tag/Programmatic-API-Keys/operation/getApiKey) endpoint.

        **Note**: This resource does not return information about pending users invited via the deprecated [Invite One MongoDB Cloud User to Join One Project](#tag/Projects/operation/createProjectInvitation) endpoint.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Project resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            org_membership_statuses: Organization membership status to filter users by. You can supply this parameter multiple times. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Not supported in deprecated versions.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/users/{quote(str(user_id), safe='')}"
        params = {
            "envelope": envelope,
            "orgMembershipStatuses": org_membership_statuses,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupUserResponse,
        )

    def add_group_user_role(
        self,
        group_id: str,
        user_id: str,
        body: AddOrRemoveGroupRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupUserResponse:
        """
        Add One Project Role to One MongoDB Cloud User

        Adds one project-level role to the MongoDB Cloud user. You can add a role to an active user or a user that has been invited to join the project. 

        **Note**: This resource cannot be used to add a role to users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Project resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Project-level role to assign to the MongoDB Cloud user.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/users/{quote(str(user_id), safe='')}:addRole"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupUserResponse,
        )

    def remove_group_user_role(
        self,
        group_id: str,
        user_id: str,
        body: AddOrRemoveGroupRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupUserResponse:
        """
        Remove One Project Role from One MongoDB Cloud User

        Removes one project-level role from the MongoDB Cloud user. You can remove a role from an active user or a user that has been invited to join the project. To replace a user's only role, add the new role before removing the old role. A user must have at least one role at all times. 

        **Note**: This resource cannot be used to remove a role from users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the project. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Project resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Project-level role to remove from the MongoDB Cloud user.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/users/{quote(str(user_id), safe='')}:removeRole"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupUserResponse,
        )

    def list_org_team_users(
        self,
        org_id: str,
        team_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        org_membership_status: str | None = None,
        org_membership_statuses: list[Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"]] | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        user_id: str | None = None,
        username: str | None = None,
    ) -> PaginatedOrgUserView:
        """
        Return All MongoDB Cloud Users Assigned to One Team

        Returns details about the pending and active MongoDB Cloud users associated with the specified team in the organization. Teams enable you to grant project access roles to MongoDB Cloud users. 

        **Note**: This resource cannot be used to view details about users invited via the deprecated [Invite One MongoDB Cloud User to Join One Project](#tag/Projects/operation/createProjectInvitation) endpoint.

        **Note**: To return both pending and active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users will be returned. Deprecated versions: v2-{2023-01-01}

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team whose application users you want to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            org_membership_status: Deprecated: Use `orgMembershipStatuses` instead. Organization membership status to filter users by. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Not supported in deprecated versions.
            org_membership_statuses: Organization membership status to filter users by. You can supply this parameter multiple times. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. Replaces the deprecated `orgMembershipStatus` parameter. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Cannot be combined with `orgMembershipStatus`. Not supported in deprecated versions.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            user_id: Unique 24-hexadecimal digit string to filter users by. Not supported in deprecated versions.
            username: Email address to filter users by. Not supported in deprecated versions.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}/users"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "orgMembershipStatus": org_membership_status,
            "orgMembershipStatuses": org_membership_statuses,
            "pageNum": page_num,
            "pretty": pretty,
            "userId": user_id,
            "username": username,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedOrgUserView,
        )

    def add_org_team_user(
        self,
        org_id: str,
        team_id: str,
        body: AddOrRemoveUserFromTeam,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Add One MongoDB Cloud User to One Team

        Adds one MongoDB Cloud user to one team. You can add an active user or a user that has not yet accepted the invitation to join the organization. 

        **Note**: This resource cannot be used to add a user invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint. 

        A user whose only organization invitation has `EXPIRED` or been `REJECTED` is treated as not belonging to the organization (`USER_NOT_IN_ORG`); re-invite them to the organization first (which creates a new pending invitation), then add them to the team.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team to add the MongoDB Cloud user to.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The active or pending MongoDB Cloud user that you want to add to the specified team.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}:addUser"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgUserResponse,
        )

    def remove_org_team_user(
        self,
        org_id: str,
        team_id: str,
        body: AddOrRemoveUserFromTeam,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Remove One MongoDB Cloud User from One Team

        Removes one MongoDB Cloud user from one team. You can remove an active user or a user that has not yet accepted the invitation to join the organization.

        **Note**: This resource cannot be used to remove a user invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            team_id: Unique 24-hexadecimal digit string that identifies the team to remove the MongoDB user from.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The id of the active or pending MongoDB Cloud user that you want to remove from the specified team.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/teams/{quote(str(team_id), safe='')}:removeUser"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgUserResponse,
        )

    def list_org_users(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        org_membership_status: str | None = None,
        org_membership_statuses: list[Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"]] | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        username: str | None = None,
    ) -> PaginatedOrgUserView:
        """
        Return All MongoDB Cloud Users in One Organization

        Returns details about the pending and active MongoDB Cloud users associated with the specified organization. 

        **Note**: This resource cannot be used to view details about users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        **Note**: To return both pending and active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users will be returned. Deprecated versions: v2-{2023-01-01}

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            org_membership_status: Deprecated: Use `orgMembershipStatuses` instead. Organization membership status to filter users by. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Not supported in deprecated versions.
            org_membership_statuses: Organization membership status to filter users by. You can supply this parameter multiple times. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. Replaces the deprecated `orgMembershipStatus` parameter. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Cannot be combined with `orgMembershipStatus`. Not supported in deprecated versions.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            username: Email address to filter users by. Not supported in deprecated versions.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "orgMembershipStatus": org_membership_status,
            "orgMembershipStatuses": org_membership_statuses,
            "pageNum": page_num,
            "pretty": pretty,
            "username": username,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedOrgUserView,
        )

    def create_org_user(
        self,
        org_id: str,
        body: OrgUserRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Add One MongoDB Cloud User to One Organization

        Invites one new or existing MongoDB Cloud user to join the organization. The invitation to join the organization will be sent to the username provided and must be accepted within 30 days. 

        **Note**: If the user does not have an existing MongoDB Cloud account, they will be prompted to finish setting up an account upon accepting the invitation. If the user already has an account, they will still receive an invitation to access the organization. 

        Replaces `INVITATION_EXPIRED` and `INVITATION_REJECTED` user with the same email. A conflict, if and only if, there is an existing `PENDING` or `ACTIVE` user.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Represents the MongoDB Cloud user to be created within the organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgUserResponse,
        )

    def remove_org_user(
        self,
        org_id: str,
        user_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One MongoDB Cloud User from One Organization

        Removes one MongoDB Cloud user in the specified organization. You can remove an active user or a user that has not yet accepted the invitation to join the organization. 

        **Note**: This resource cannot be used to remove pending users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        **Note**: To remove pending or active users, use v2-{2025-02-19} or later. If using a deprecated version, only active users can be removed. Deprecated versions: v2-{2023-01-01}

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the [Return All MongoDB Cloud Users in One Organization](#tag/MongoDB-Cloud-Users/operation/listOrganizationUsers) resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users/{quote(str(user_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_org_user(
        self,
        org_id: str,
        user_id: str,
        *,
        envelope: bool | None = None,
        org_membership_statuses: list[Literal["PENDING", "ACTIVE", "INVITATION_EXPIRED", "INVITATION_REJECTED"]] | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Return One MongoDB Cloud User in One Organization

        Returns information about the specified MongoDB Cloud user within the context of the specified organization. 

        **Note**: This resource can only be used to fetch information about MongoDB Cloud human users. To return information about an API Key, use the [Return One Organization API Key](#tag/Programmatic-API-Keys/operation/getApiKey) endpoint.

        **Note**: This resource does not return information about pending users invited via the deprecated [Invite One MongoDB Cloud User to Join One Project](#tag/Projects/operation/createProjectInvitation) endpoint.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            org_membership_statuses: Organization membership status to filter users by. You can supply this parameter multiple times. Allowed values: `ACTIVE`, `PENDING`, `INVITATION_EXPIRED`, `INVITATION_REJECTED`. If you exclude this parameter, this resource returns ACTIVE and PENDING users. Not supported in deprecated versions.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users/{quote(str(user_id), safe='')}"
        params = {
            "envelope": envelope,
            "orgMembershipStatuses": org_membership_statuses,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgUserResponse,
        )

    def update_org_user(
        self,
        org_id: str,
        user_id: str,
        body: OrgUserUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Update One MongoDB Cloud User in One Organization

        Updates one MongoDB Cloud user in the specified organization. You can update an active user or a user that has not yet accepted the invitation to join the organization. 

        **Note**: Only include the fields you wish to update in the request body. Supplying a field with an empty value will reset that field on the user.

        **Note**: This resource cannot be used to update pending users invited via the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Represents the roles and teams to assign the MongoDB Cloud user.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users/{quote(str(user_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrgUserResponse,
        )

    def add_org_user_role(
        self,
        org_id: str,
        user_id: str,
        body: AddOrRemoveOrgRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Add One Organization Role to One MongoDB Cloud User

        Adds one organization-level role to the MongoDB Cloud user. You can add a role to an active user or a user that has not yet accepted the invitation to join the organization. 

        **Note**: This operation is atomic.

        **Note**: This resource cannot be used to add a role to users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization-level role to assign to the MongoDB Cloud user.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users/{quote(str(user_id), safe='')}:addRole"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgUserResponse,
        )

    def remove_org_user_role(
        self,
        org_id: str,
        user_id: str,
        body: AddOrRemoveOrgRole,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgUserResponse:
        """
        Remove One Organization Role from One MongoDB Cloud User

        Removes one organization-level role from the MongoDB Cloud user. You can remove a role from an active user or a user that has not yet accepted the invitation to join the organization. To replace a user's only role, add the new role before removing the old role. A user must have at least one role at all times.

        **Note**: This operation is atomic.

        **Note**: This resource cannot be used to remove a role from users invited using the deprecated Invite One MongoDB Cloud User to Join One Project endpoint.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            user_id: Unique 24-hexadecimal digit string that identifies the pending or active user in the organization. If you need to lookup a user's `userId` or verify a user's status in the organization, use the Return All MongoDB Cloud Users in One Organization resource and filter by `username`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization-level role to remove from the MongoDB Cloud user.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users/{quote(str(user_id), safe='')}:removeRole"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrgUserResponse,
        )

    def create_user(
        self,
        body: CloudAppUser,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudAppUser:
        """
        Create One MongoDB Cloud User

        Creates one MongoDB Cloud user account. A MongoDB Cloud user account grants access to only the MongoDB Cloud application. To grant database access, create a database user. MongoDB Cloud sends an email to the users you specify, inviting them to join the project. Invited users don't have access to the project until they accept the invitation. Invitations expire after 30 days.

         MongoDB Cloud limits MongoDB Cloud user membership to a maximum of 250 MongoDB Cloud users per team. MongoDB Cloud limits MongoDB Cloud user membership to 500 MongoDB Cloud users per project and 500 MongoDB Cloud users per organization, which includes the combined membership of all projects in the organization. MongoDB Cloud raises an error if an operation exceeds these limits. For example, if you have an organization with five projects, and each project has 100 MongoDB Cloud users, and each MongoDB Cloud user belongs to only one project, you can't add any MongoDB Cloud users to this organization without first removing existing MongoDB Cloud users from the organization.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: MongoDB Cloud user account to create.
        """
        path = "/api/atlas/v2/users"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=CloudAppUser,
        )

    def get_user_by_name(
        self,
        user_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudAppUser:
        """
        Return One MongoDB Cloud User by Username

        Returns the details for one MongoDB Cloud user account with the specified username. You can't use this endpoint to return information about an API Key. To return information about an API Key, use the Return One Organization API Key endpoint.

        Args:
            user_name: Email address that belongs to the MongoDB Cloud user account. You cannot modify this address after creating the user.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/users/byName/{quote(str(user_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CloudAppUser,
        )

    def get_user(
        self,
        user_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudAppUser:
        """
        Return One MongoDB Cloud User by ID

        Returns the details for one MongoDB Cloud user account with the specified unique identifier for the user. You can't use this endpoint to return information on an API Key. To return information about an API Key, use the Return One Organization API Key endpoint. You can always retrieve your own user account. If you are the owner of a MongoDB Cloud organization or project, you can also retrieve the user profile for any user with membership in that organization or project.

        Args:
            user_id: Unique 24-hexadecimal digit string that identifies this user.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/users/{quote(str(user_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CloudAppUser,
        )
