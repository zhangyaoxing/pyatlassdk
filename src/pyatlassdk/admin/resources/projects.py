"""Generated resource for Projects. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.data_federation_limit import DataFederationLimit
from pyatlassdk.admin.models.group import Group
from pyatlassdk.admin.models.group_ip_addresses import GroupIPAddresses
from pyatlassdk.admin.models.group_invitation import GroupInvitation
from pyatlassdk.admin.models.group_invitation_request import GroupInvitationRequest
from pyatlassdk.admin.models.group_invitation_update_request import GroupInvitationUpdateRequest
from pyatlassdk.admin.models.group_migration_request import GroupMigrationRequest
from pyatlassdk.admin.models.group_settings import GroupSettings
from pyatlassdk.admin.models.group_update import GroupUpdate
from pyatlassdk.admin.models.organization_invitation import OrganizationInvitation
from pyatlassdk.admin.models.paginated_atlas_group_view import PaginatedAtlasGroupView
from pyatlassdk.admin.models.paginated_available_version_view import PaginatedAvailableVersionView
from pyatlassdk.admin.models.update_group_roles_for_user import UpdateGroupRolesForUser

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class Projects:
    """Returns, adds, and edits collections of clusters and users in MongoDB Cloud."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_groups(
        self,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasGroupView:
        """
        Return All Projects

        Returns details about all projects. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/groups"
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
            response_model=PaginatedAtlasGroupView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_group(
        self,
        body: Group,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        project_owner_id: str | None = None,
    ) -> Group:
        """
        Create One Project

        Creates one project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            project_owner_id: Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user to whom to grant the Project Owner role on the specified project. If you set this parameter, it overrides the default value of the oldest Organization Owner.
            body: Creates one project.
        """
        path = "/groups"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "projectOwnerId": project_owner_id,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Group,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_by_name(
        self,
        group_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Group:
        """
        Return One Project by Name

        Returns details about the specified project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings.

        Args:
            group_name: Human-readable label that identifies this project.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/byName/{quote(str(group_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=Group,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Project

        Removes the specified project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings. You can delete a project only if there are no Online Archives for the clusters in the project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}"
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

    def get_group(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Group:
        """
        Return One Project

        Returns details about the specified project. Projects group clusters into logical collections that support an application environment, workload, or both. Each project can have its own users, teams, security, tags, and alert settings.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=Group,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group(
        self,
        group_id: str,
        body: GroupUpdate,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Group:
        """
        Update One Project

        Updates the human-readable label that identifies the specified project, or the tags associated with the project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Project to update.
        """
        path = f"/groups/{quote(str(group_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=Group,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def add_group_access_user(
        self,
        group_id: str,
        body: GroupInvitationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationInvitation | Any:
        """
        Add One MongoDB Cloud User to One Project

        Adds one MongoDB Cloud user to the specified project. If the MongoDB Cloud user is not a member of the project's organization, then the user must accept their invitation to the organization to access information within the specified project. If the MongoDB Cloud User is already a member of the project's organization, then they will be added to the project immediately and an invitation will not be returned by this resource.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Adds one MongoDB Cloud user to the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/access"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrganizationInvitation | Any,
            accept="application/vnd.atlas.2023-02-01+json",
            content_type="application/vnd.atlas.2023-02-01+json",
        )

    def list_group_invites(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        username: str | None = None,
    ) -> list[GroupInvitation]:
        """
        Return All Invitations in One Project

        Returns all pending invitations to the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            username: Email address of the user account invited to this project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/invites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "username": username,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[GroupInvitation],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_invites(
        self,
        group_id: str,
        body: GroupInvitationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupInvitation:
        """
        Update One Invitation in One Project

        Updates the details of one pending invitation to the specified project. To specify which invitation to update, provide the username of the invited user.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the details of one pending invitation to the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/invites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=GroupInvitation,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def create_group_invite(
        self,
        group_id: str,
        body: GroupInvitationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupInvitation:
        """
        Create Invitation for One MongoDB Cloud User in One Project

        Invites one MongoDB Cloud user to join the specified project. The MongoDB Cloud user must accept the invitation to access information within the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Invites one MongoDB Cloud user to join the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/invites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupInvitation,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_invite(
        self,
        group_id: str,
        invitation_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Invitation from One Project

        Cancels one pending invitation sent to the specified MongoDB Cloud user to join a project. You can't cancel an invitation that the user accepted. Note: deleting a project invitation does not delete an organization invitation even if they were created together.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/invites/{quote(str(invitation_id), safe='')}"
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

    def get_group_invite(
        self,
        group_id: str,
        invitation_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupInvitation:
        """
        Return One Invitation in One Project by Invitation ID

        Returns the details of one pending invitation to the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/invites/{quote(str(invitation_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupInvitation,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_invite_by_id(
        self,
        group_id: str,
        invitation_id: str,
        body: GroupInvitationUpdateRequest,
        *,
        envelope: bool | None = None,
    ) -> GroupInvitation:
        """
        Update One Invitation in One Project by Invitation ID

        Updates the details of one pending invitation to the specified project. To specify which invitation to update, provide the unique identification string for that invitation. Use the Return All Project Invitations endpoint to retrieve IDs for all pending project invitations.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Updates the details of one pending invitation to the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/invites/{quote(str(invitation_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=GroupInvitation,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_ip_addresses(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupIPAddresses:
        """
        Return All IP Addresses for One Project

        Returns all IP addresses for this project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/ipAddresses"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupIPAddresses,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_limits(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[DataFederationLimit]:
        """
        Return All Limits for One Project

        Returns all the limits for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/limits"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[DataFederationLimit],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_limit(
        self,
        group_id: str,
        limit_name: Literal["atlas.project.security.databaseAccess.users", "atlas.project.deployment.clusters", "atlas.project.deployment.serverlessMTMs", "atlas.project.security.databaseAccess.customRoles", "atlas.project.security.networkAccess.entries", "atlas.project.security.networkAccess.crossRegionEntries", "atlas.project.deployment.nodesPerPrivateLinkRegion", "dataFederation.bytesProcessed.query", "dataFederation.bytesProcessed.daily", "dataFederation.bytesProcessed.weekly", "dataFederation.bytesProcessed.monthly", "atlas.project.deployment.privateServiceConnectionsPerRegionGroup", "atlas.project.deployment.privateServiceConnectionsSubnetMask"],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Project Limit

        Removes the specified project limit. Depending on the limit, Atlas either resets the limit to its default value or removes the limit entirely.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            limit_name: Human-readable label that identifies this project limit. | Limit Name | Description | Default | API Override Limit | | --- | --- | --- | --- | | `atlas.project.deployment.clusters` | Limit on the number of clusters in this project | 25 | 100 | | `atlas.project.deployment.nodesPerPrivateLinkRegion` | Limit on AWS PrivateLink addressable target nodes per region in this project. For sharded clusters using optimized (load-balanced) connection strings, `currentUsage` doesn't grow with the number of `mongos` — the load balancer is counted as a single addressable target regardless of how many `mongos` sit behind it. | 50 | 90 | | `atlas.project.security.databaseAccess.customRoles` | Limit on the number of custom roles in this project | 100 | 1400 | | `atlas.project.security.databaseAccess.users` | Limit on the number of database users in this project | 100 | 900 | | `atlas.project.security.networkAccess.crossRegionEntries` | Limit on the number of cross-region network access entries in this project | 40 | 220 | | `atlas.project.security.networkAccess.entries` | Limit on the number of network access entries in this project | 200 | 20 | | `dataFederation.bytesProcessed.query` | Limit on the number of bytes processed during a single Data Federation query | N/A | N/A | | `dataFederation.bytesProcessed.daily` | Limit on the number of bytes processed across all Data Federation tenants for the current day | N/A | N/A | | `dataFederation.bytesProcessed.weekly` | Limit on the number of bytes processed across all Data Federation tenants for the current week | N/A | N/A | | `dataFederation.bytesProcessed.monthly` | Limit on the number of bytes processed across all Data Federation tenants for the current month | N/A | N/A | | `atlas.project.deployment.privateServiceConnectionsPerRegionGroup` | Number of Private Service Connections per Region Group | 50 | 100| | `atlas.project.deployment.privateServiceConnectionsSubnetMask` | Subnet mask for GCP PSC Networks. Has lower limit of 20. | 27 | 27|
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/limits/{quote(str(limit_name), safe='')}"
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

    def get_group_limit(
        self,
        group_id: str,
        limit_name: Literal["atlas.project.security.databaseAccess.users", "atlas.project.deployment.clusters", "atlas.project.deployment.serverlessMTMs", "atlas.project.security.databaseAccess.customRoles", "atlas.project.security.networkAccess.entries", "atlas.project.security.networkAccess.crossRegionEntries", "atlas.project.deployment.nodesPerPrivateLinkRegion", "dataFederation.bytesProcessed.query", "dataFederation.bytesProcessed.daily", "dataFederation.bytesProcessed.weekly", "dataFederation.bytesProcessed.monthly", "atlas.project.deployment.privateServiceConnectionsPerRegionGroup", "atlas.project.deployment.privateServiceConnectionsSubnetMask"],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DataFederationLimit:
        """
        Return One Limit for One Project

        Returns the specified limit for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            limit_name: Human-readable label that identifies this project limit. | Limit Name | Description | Default | API Override Limit | | --- | --- | --- | --- | | `atlas.project.deployment.clusters` | Limit on the number of clusters in this project | 25 | 100 | | `atlas.project.deployment.nodesPerPrivateLinkRegion` | Limit on AWS PrivateLink addressable target nodes per region in this project. For sharded clusters using optimized (load-balanced) connection strings, `currentUsage` doesn't grow with the number of `mongos` — the load balancer is counted as a single addressable target regardless of how many `mongos` sit behind it. | 50 | 90 | | `atlas.project.security.databaseAccess.customRoles` | Limit on the number of custom roles in this project | 100 | 1400 | | `atlas.project.security.databaseAccess.users` | Limit on the number of database users in this project | 100 | 900 | | `atlas.project.security.networkAccess.crossRegionEntries` | Limit on the number of cross-region network access entries in this project | 40 | 220 | | `atlas.project.security.networkAccess.entries` | Limit on the number of network access entries in this project | 200 | 20 | | `dataFederation.bytesProcessed.query` | Limit on the number of bytes processed during a single Data Federation query | N/A | N/A | | `dataFederation.bytesProcessed.daily` | Limit on the number of bytes processed across all Data Federation tenants for the current day | N/A | N/A | | `dataFederation.bytesProcessed.weekly` | Limit on the number of bytes processed across all Data Federation tenants for the current week | N/A | N/A | | `dataFederation.bytesProcessed.monthly` | Limit on the number of bytes processed across all Data Federation tenants for the current month | N/A | N/A | | `atlas.project.deployment.privateServiceConnectionsPerRegionGroup` | Number of Private Service Connections per Region Group | 50 | 100| | `atlas.project.deployment.privateServiceConnectionsSubnetMask` | Subnet mask for GCP PSC Networks. Has lower limit of 20. | 27 | 27|
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/limits/{quote(str(limit_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DataFederationLimit,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def set_group_limit(
        self,
        group_id: str,
        limit_name: Literal["atlas.project.security.databaseAccess.users", "atlas.project.deployment.clusters", "atlas.project.deployment.serverlessMTMs", "atlas.project.security.databaseAccess.customRoles", "atlas.project.security.networkAccess.entries", "atlas.project.security.networkAccess.crossRegionEntries", "atlas.project.deployment.nodesPerPrivateLinkRegion", "dataFederation.bytesProcessed.query", "dataFederation.bytesProcessed.daily", "dataFederation.bytesProcessed.weekly", "dataFederation.bytesProcessed.monthly", "atlas.project.deployment.privateServiceConnectionsPerRegionGroup", "atlas.project.deployment.privateServiceConnectionsSubnetMask"],
        body: DataFederationLimit,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DataFederationLimit:
        """
        Set One Project Limit

        Sets the specified project limit. 

        **NOTE**: Increasing the following configuration limits might lead to slower response times in the MongoDB Cloud UI or increased user management overhead leading to authentication or authorization re-architecture. If possible, we recommend that you create additional projects to gain access to more of these resources for a more sustainable growth pattern.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            limit_name: Human-readable label that identifies this project limit. | Limit Name | Description | Default | API Override Limit | | --- | --- | --- | --- | | `atlas.project.deployment.clusters` | Limit on the number of clusters in this project | 25 | 100 | | `atlas.project.deployment.nodesPerPrivateLinkRegion` | Limit on AWS PrivateLink addressable target nodes per region in this project. For sharded clusters using optimized (load-balanced) connection strings, `currentUsage` doesn't grow with the number of `mongos` — the load balancer is counted as a single addressable target regardless of how many `mongos` sit behind it. | 50 | 90 | | `atlas.project.security.databaseAccess.customRoles` | Limit on the number of custom roles in this project | 100 | 1400 | | `atlas.project.security.databaseAccess.users` | Limit on the number of database users in this project | 100 | 900 | | `atlas.project.security.networkAccess.crossRegionEntries` | Limit on the number of cross-region network access entries in this project | 40 | 220 | | `atlas.project.security.networkAccess.entries` | Limit on the number of network access entries in this project | 200 | 20 | | `dataFederation.bytesProcessed.query` | Limit on the number of bytes processed during a single Data Federation query | N/A | N/A | | `dataFederation.bytesProcessed.daily` | Limit on the number of bytes processed across all Data Federation tenants for the current day | N/A | N/A | | `dataFederation.bytesProcessed.weekly` | Limit on the number of bytes processed across all Data Federation tenants for the current week | N/A | N/A | | `dataFederation.bytesProcessed.monthly` | Limit on the number of bytes processed across all Data Federation tenants for the current month | N/A | N/A | | `atlas.project.deployment.privateServiceConnectionsPerRegionGroup` | Number of Private Service Connections per Region Group | 50 | 100| | `atlas.project.deployment.privateServiceConnectionsSubnetMask` | Subnet mask for GCP PSC Networks. Has lower limit of 20. | 27 | 27|
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Limit to update.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/limits/{quote(str(limit_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=DataFederationLimit,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_mongo_db_versions(
        self,
        group_id: str,
        *,
        cloud_provider: Literal["AWS", "AZURE", "GCP", "TENANT"] | None = None,
        default_status: Literal["DEFAULT"] | None = None,
        envelope: bool | None = None,
        instance_size: str | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAvailableVersionView:
        """
        Return All Available MongoDB LTS Versions for Clusters in One Project

        Returns the MongoDB Long Term Support Major Versions available to new clusters in this project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            cloud_provider: Filter results to only one cloud provider.
            default_status: Filter results to only the default values per tier. This value must be DEFAULT.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            instance_size: Filter results to only one instance size.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/mongoDBVersions"
        params = {
            "cloudProvider": cloud_provider,
            "defaultStatus": default_status,
            "envelope": envelope,
            "instanceSize": instance_size,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedAvailableVersionView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_settings(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupSettings:
        """
        Return Project Settings

        Returns details about the specified project's settings.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/settings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupSettings,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_settings(
        self,
        group_id: str,
        body: GroupSettings,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupSettings:
        """
        Update Project Settings

        Updates the settings of the specified project. You can update any of the options available. MongoDB cloud only updates the options provided in the request.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Settings to update.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/settings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=GroupSettings,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_user_roles(
        self,
        group_id: str,
        user_id: str,
        body: UpdateGroupRolesForUser,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UpdateGroupRolesForUser:
        """
        Update Project Roles for One MongoDB Cloud User

        Updates the roles of the specified user in the specified project. To specify the user to update, provide the unique 24-hexadecimal digit string that identifies the user in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            user_id: Unique 24-hexadecimal digit string that identifies the user to modify.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Roles to update for the specified user.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/users/{quote(str(user_id), safe='')}/roles"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=UpdateGroupRolesForUser,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def migrate_group(
        self,
        group_id: str,
        body: GroupMigrationRequest,
        *,
        envelope: bool | None = None,
    ) -> Group:
        """
        Migrate One Project to Another Organization

        Migrates a project from its current organization to another organization. All project users and their roles will be copied to the same project in the destination organization. You must include an organization API key with the Organization Owner role for the destination organization to verify access to the destination organization when you authenticate with Programmatic API Keys. Otherwise, the requesting user must have the Organization Owner role in both organizations.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Migrates a project from its current organization to another organization.
        """
        path = f"/groups/{quote(str(group_id), safe='')}:migrate"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Group,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )
