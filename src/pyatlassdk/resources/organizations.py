"""Generated resource for Organizations. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.atlas_organization import AtlasOrganization
from pyatlassdk.models.create_organization_request import CreateOrganizationRequest
from pyatlassdk.models.create_organization_response import CreateOrganizationResponse
from pyatlassdk.models.org_delegation_settings_response import OrgDelegationSettingsResponse
from pyatlassdk.models.org_delegation_settings_update_request import OrgDelegationSettingsUpdateRequest
from pyatlassdk.models.organization_invitation import OrganizationInvitation
from pyatlassdk.models.organization_invitation_request import OrganizationInvitationRequest
from pyatlassdk.models.organization_invitation_update_request import OrganizationInvitationUpdateRequest
from pyatlassdk.models.organization_maintenance_settings_response import OrganizationMaintenanceSettingsResponse
from pyatlassdk.models.organization_maintenance_settings_update_request import OrganizationMaintenanceSettingsUpdateRequest
from pyatlassdk.models.organization_settings import OrganizationSettings
from pyatlassdk.models.paginated_atlas_group_view import PaginatedAtlasGroupView
from pyatlassdk.models.paginated_organization_view import PaginatedOrganizationView
from pyatlassdk.models.update_org_roles_for_user import UpdateOrgRolesForUser

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class Organizations:
    """Returns, adds, and edits organizational units in MongoDB Cloud."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_orgs(
        self,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        name: str | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOrganizationView:
        """
        Return All Organizations

        Returns all organizations to which the requesting Service Account or API Key has access.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            name: Human-readable label of the organization to use to filter the returned list. Performs a case-insensitive search for an organization that starts with the specified name.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/api/atlas/v2/orgs"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "name": name,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedOrganizationView,
        )

    def create_org(
        self,
        body: CreateOrganizationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CreateOrganizationResponse:
        """
        Create One Organization

        Creates one organization in MongoDB Cloud and links it to the requesting Service Account's or API Key's organization. The requesting Service Account's or API Key's organization must be a paying organization. To learn more, see Configure a Paying Organization in the MongoDB Atlas documentation. Optionally, if `federationSettingsId` is provided, the new Organization will be linked to the federation. The requesting Service Account or API Key must be an Organization Owner in the federation.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Organization that you want to create.
        """
        path = "/api/atlas/v2/orgs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=CreateOrganizationResponse,
        )

    def delete_org(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Organization

        Removes one specified organization. MongoDB Cloud imposes the following limits on this resource:

         - Organizations with active projects cannot be removed.
         - All projects in the organization must be removed before you can remove the organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_org(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AtlasOrganization:
        """
        Return One Organization

        Returns one organization to which the requesting Service Account or API Key has access.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AtlasOrganization,
        )

    def update_org(
        self,
        org_id: str,
        body: AtlasOrganization,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AtlasOrganization:
        """
        Update One Organization

        Updates one organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update on the specified organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AtlasOrganization,
        )

    def get_org_delegation_settings(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgDelegationSettingsResponse:
        """
        Return Delegation Settings for One Organization

        Returns the delegation settings for the specified organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/delegationSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgDelegationSettingsResponse,
        )

    def update_org_delegation_settings(
        self,
        org_id: str,
        body: OrgDelegationSettingsUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgDelegationSettingsResponse:
        """
        Update Delegation Settings for One Organization

        Updates the delegation settings for the specified organization. Only fields present in the request body are updated; omitted fields retain their current values.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Delegation settings to update.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/delegationSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrgDelegationSettingsResponse,
        )

    def get_org_groups(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        name: str | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasGroupView:
        """
        Return All Projects in One Organization

        Returns multiple projects in the specified organization. Each organization can have multiple projects. Use projects to:

        - Isolate different environments, such as development, test, or production environments, from each other.
        - Associate different MongoDB Cloud users or teams with different environments, or give different permission to MongoDB Cloud users in different environments.
        - Maintain separate cluster security configurations.
        - Create different alert settings.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            name: Human-readable label of the project to use to filter the returned list. Performs a case-insensitive search for a project within the organization which is prefixed by the specified name.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/groups"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "name": name,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedAtlasGroupView,
        )

    def list_org_invites(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        username: str | None = None,
    ) -> list[OrganizationInvitation]:
        """
        Return All Invitations in One Organization

        Returns all pending invitations to the specified organization. 

        **Note**: Invitation management APIs are deprecated. Use Return All MongoDB Cloud Users in One Organization and filter by `orgMembershipStatus` to return all pending users.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            username: Email address of the user account invited to this organization. If you exclude this parameter, this resource returns all pending invitations.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/invites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "username": username,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[OrganizationInvitation],
        )

    def update_org_invites(
        self,
        org_id: str,
        body: OrganizationInvitationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationInvitation:
        """
        Update One Invitation in One Organization

        Updates the details of one pending invitation to the specified organization. To specify which invitation, provide the username of the invited user. 

        **Note**:  Invitation management are deprecated. Use Update One MongoDB Cloud User in One Organization to update a pending user.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the details of one pending invitation to the specified organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/invites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrganizationInvitation,
        )

    def create_org_invite(
        self,
        org_id: str,
        body: OrganizationInvitationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationInvitation:
        """
        Create Invitation for One MongoDB Cloud User in One Organization

        Invites one MongoDB Cloud user to join the specified organization. The user must accept the invitation to access information within the specified organization.

        **Note**: Invitation management APIs are deprecated. Use Add One MongoDB Cloud User to One Organization to invite a user.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Invites one MongoDB Cloud user to join the specified organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/invites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OrganizationInvitation,
        )

    def delete_org_invite(
        self,
        invitation_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Invitation from One Organization

        Cancels one pending invitation sent to the specified MongoDB Cloud user to join an organization. You can't cancel an invitation that the user accepted.

        **Note**: Invitation management APIs are deprecated. Use Remove One MongoDB Cloud User From One Organization to remove a pending user.

        Args:
            invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/invites/{quote(str(invitation_id), safe='')}"
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

    def get_org_invite(
        self,
        invitation_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> OrganizationInvitation:
        """
        Return One Invitation in One Organization by Invitation ID

        Returns the details of one pending invitation to the specified organization.

        **Note**: Invitation management APIs are deprecated. Use Return One MongoDB Cloud User in One Organization to return a pending user.

        Args:
            invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/invites/{quote(str(invitation_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrganizationInvitation,
        )

    def update_org_invite_by_id(
        self,
        invitation_id: str,
        org_id: str,
        body: OrganizationInvitationUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationInvitation:
        """
        Update One Invitation in One Organization by Invitation ID

        Updates the details of one pending invitation to the specified organization. To specify which invitation, provide the unique identification string for that invitation. Use the Return All Organization Invitations endpoint to retrieve IDs for all pending organization invitations. 

        **Note**: Invitation management APIs are deprecated. Use Update One MongoDB Cloud User in One Organization to update a pending user.

        Args:
            invitation_id: Unique 24-hexadecimal digit string that identifies the invitation.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the details of one pending invitation to the specified organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/invites/{quote(str(invitation_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrganizationInvitation,
        )

    def get_org_maintenance_settings(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationMaintenanceSettingsResponse:
        """
        Return Maintenance Settings for One Organization

        Returns maintenance settings for the specified organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/maintenanceSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrganizationMaintenanceSettingsResponse,
        )

    def update_org_maintenance_settings(
        self,
        org_id: str,
        body: OrganizationMaintenanceSettingsUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationMaintenanceSettingsResponse:
        """
        Update Maintenance Settings for One Organization

        Updates maintenance settings for the specified organization. Omit optional fields from the request body to leave their current values unchanged. Specify null on an optional field to reset it to its default value.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Maintenance settings to update for the specified organization.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/maintenanceSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrganizationMaintenanceSettingsResponse,
        )

    def reset_org_maintenance_settings(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationMaintenanceSettingsResponse:
        """
        Reset Maintenance Settings for One Organization

        Resets maintenance settings for the specified organization to their default values. Restores the wave assignment mode to the default manual mode.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/maintenanceSettings:reset"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=OrganizationMaintenanceSettingsResponse,
        )

    def get_org_settings(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationSettings:
        """
        Return Settings for One Organization

        Returns details about the specified organization's settings.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/settings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrganizationSettings,
        )

    def update_org_settings(
        self,
        org_id: str,
        body: OrganizationSettings,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrganizationSettings:
        """
        Update Settings for One Organization

        Updates the organization's settings.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update on the specified organization's settings.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/settings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=OrganizationSettings,
        )

    def update_org_user_roles(
        self,
        org_id: str,
        user_id: str,
        body: UpdateOrgRolesForUser,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UpdateOrgRolesForUser:
        """
        Update Organization Roles for One MongoDB Cloud User

        Updates the roles of the specified user in the specified organization. To specify the user to update, provide the unique 24-hexadecimal digit string that identifies the user in the specified organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            user_id: Unique 24-hexadecimal digit string that identifies the user to modify.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Roles to update for the specified user.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/users/{quote(str(user_id), safe='')}/roles"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=UpdateOrgRolesForUser,
        )
