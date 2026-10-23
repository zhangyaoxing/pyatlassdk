"""Generated resource for FederatedAuthentication. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.auth_federation_role_mapping import AuthFederationRoleMapping
from pyatlassdk.models.connected_org_config import ConnectedOrgConfig
from pyatlassdk.models.federation_identity_provider import FederationIdentityProvider
from pyatlassdk.models.federation_identity_provider_update import FederationIdentityProviderUpdate
from pyatlassdk.models.federation_oidc_identity_provider import FederationOidcIdentityProvider
from pyatlassdk.models.federation_oidc_identity_provider_update import FederationOidcIdentityProviderUpdate
from pyatlassdk.models.org_federation_settings import OrgFederationSettings
from pyatlassdk.models.paginated_connected_org_configs_view import PaginatedConnectedOrgConfigsView
from pyatlassdk.models.paginated_federation_identity_provider import PaginatedFederationIdentityProvider
from pyatlassdk.models.paginated_role_mapping_view import PaginatedRoleMappingView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class FederatedAuthentication:
    """Returns, adds, edits, and removes federation-related features such as role mappings and connected organization configurations."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def delete_federation_setting(
        self,
        federation_settings_id: str,
    ) -> Any:
        """
        Delete One Federation Settings Instance

        Deletes the federation settings instance and all associated data, including identity providers and domains. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in the last remaining connected organization. **Note**: requests to this resource will fail if there is more than one connected organization in the federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=Any,
        )

    def list_federation_setting_connected_org_configs(
        self,
        federation_settings_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
    ) -> PaginatedConnectedOrgConfigsView:
        """
        Return All Organization Configurations from One Federation

        Returns all connected organization configurations in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedConnectedOrgConfigsView,
        )

    def remove_federation_setting_connected_org_config(
        self,
        federation_settings_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Organization Configuration from One Federation

        Removes one connected organization configuration from the specified federation. Note: This request fails if only one connected organization exists in the federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            org_id: Unique 24-hexadecimal digit string that identifies the connected organization configuration to remove.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_federation_setting_connected_org_config(
        self,
        federation_settings_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> ConnectedOrgConfig:
        """
        Return One Organization Configuration from One Federation

        Returns the specified connected organization configuration from the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in the connected organization.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            org_id: Unique 24-hexadecimal digit string that identifies the connected organization configuration to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ConnectedOrgConfig,
        )

    def update_federation_setting_connected_org_config(
        self,
        federation_settings_id: str,
        org_id: str,
        body: ConnectedOrgConfig,
        *,
        envelope: bool | None = None,
    ) -> ConnectedOrgConfig:
        """
        Update One Organization Configuration in One Federation

        Updates one connected organization configuration from the specified federation.

        **Note** If the organization configuration has no associated identity provider, you can't use this resource to update role mappings or post authorization role grants.  

        **Note**: The `domainRestrictionEnabled` field defaults to false if not provided in the request. 

        **Note**: If the `identityProviderId` field is not provided, you will disconnect the organization and the identity provider. 

        **Note**: Currently connected data access identity providers missing from the `dataAccessIdentityProviderIds` field will be disconnected.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            org_id: Unique 24-hexadecimal digit string that identifies the connected organization configuration to update.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: The connected organization configuration that you want to update.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ConnectedOrgConfig,
        )

    def list_federation_setting_connected_org_config_role_mappings(
        self,
        federation_settings_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> PaginatedRoleMappingView:
        """
        Return All Role Mappings from One Organization

        Returns all role mappings from the specified organization in the specified federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}/roleMappings"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedRoleMappingView,
        )

    def create_federation_setting_connected_org_config_role_mapping(
        self,
        federation_settings_id: str,
        org_id: str,
        body: AuthFederationRoleMapping,
        *,
        envelope: bool | None = None,
    ) -> AuthFederationRoleMapping:
        """
        Create One Role Mapping in One Organization Configuration

        Adds one role mapping to the specified organization in the specified federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: The role mapping that you want to create.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}/roleMappings"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=AuthFederationRoleMapping,
        )

    def delete_federation_setting_connected_org_config_role_mapping(
        self,
        federation_settings_id: str,
        id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Role Mapping from One Organization

        Removes one role mapping in the specified organization from the specified federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            id: Unique 24-hexadecimal digit string that identifies the role mapping that you want to remove.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}/roleMappings/{quote(str(id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_federation_setting_connected_org_config_role_mapping(
        self,
        federation_settings_id: str,
        id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> AuthFederationRoleMapping:
        """
        Return One Role Mapping from One Organization

        Returns one role mapping from the specified organization in the specified federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            id: Unique 24-hexadecimal digit string that identifies the role mapping that you want to return.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}/roleMappings/{quote(str(id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AuthFederationRoleMapping,
        )

    def update_federation_setting_connected_org_config_role_mapping(
        self,
        federation_settings_id: str,
        id: str,
        org_id: str,
        body: AuthFederationRoleMapping,
        *,
        envelope: bool | None = None,
    ) -> AuthFederationRoleMapping:
        """
        Update One Role Mapping in One Organization

        Updates one role mapping in the specified organization in the specified federation.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            id: Unique 24-hexadecimal digit string that identifies the role mapping that you want to update.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: The role mapping that you want to update.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/connectedOrgConfigs/{quote(str(org_id), safe='')}/roleMappings/{quote(str(id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=AuthFederationRoleMapping,
        )

    def list_federation_setting_identity_providers(
        self,
        federation_settings_id: str,
        *,
        envelope: bool | None = None,
        idp_type: list[Literal["WORKFORCE", "WORKLOAD"]] | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        protocol: list[Literal["SAML", "OIDC"]] | None = None,
    ) -> PaginatedFederationIdentityProvider:
        """
        Return All Identity Providers in One Federation

        Returns all identity providers with the provided protocol and type in the specified federation. If no protocol is specified, only SAML identity providers will be returned. If no `idpType` is specified, only WORKFORCE identity providers will be returned. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            idp_type: The types of the target identity providers.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            protocol: The protocols of the target identity providers.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders"
        params = {
            "envelope": envelope,
            "idpType": idp_type,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "protocol": protocol,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedFederationIdentityProvider,
        )

    def create_federation_setting_identity_provider(
        self,
        federation_settings_id: str,
        body: FederationOidcIdentityProviderUpdate,
        *,
        envelope: bool | None = None,
    ) -> FederationOidcIdentityProvider:
        """
        Create One Identity Provider

        Creates one identity provider within the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

        **Note**: This resource only supports the creation of OIDC identity providers.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: The identity provider that you want to create.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=FederationOidcIdentityProvider,
        )

    def delete_federation_setting_identity_provider(
        self,
        federation_settings_id: str,
        identity_provider_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Delete One Identity Provider

        Deletes one identity provider in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role for the connected organization. 

        **Note**: Requests to this resource will fail if the identity provider is connected to more than one organization or is connected to an organization unowned by the requesting Service Account or API key. Before deleting an identity provider, confirm that no organization in your federation uses this identity provider.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            identity_provider_id: Unique 24-hexadecimal digit string that identifies the identity provider to connect.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders/{quote(str(identity_provider_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_federation_setting_identity_provider(
        self,
        federation_settings_id: str,
        identity_provider_id: str,
        *,
        envelope: bool | None = None,
    ) -> FederationIdentityProvider:
        """
        Return One Identity Provider by ID

        Returns one identity provider in the specified federation by the identity provider's id. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations. Deprecated versions: v2-{2023-01-01}

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            identity_provider_id: Unique string that identifies the identity provider to connect. If using an API version before 11-15-2023, use the legacy 20-hexadecimal digit id. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider. For all other versions, use the 24-hexadecimal digit id.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders/{quote(str(identity_provider_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=FederationIdentityProvider,
        )

    def update_federation_setting_identity_provider(
        self,
        federation_settings_id: str,
        identity_provider_id: str,
        body: FederationIdentityProviderUpdate,
        *,
        envelope: bool | None = None,
    ) -> FederationIdentityProvider:
        """
        Update One Identity Provider

        Updates one identity provider in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

        **Note**: Changing authorization types and/or updating authorization claims can prevent current users and/or groups from accessing the database.

        **Note**: When deactivating a SAML identity provider connected to an organization, the requesting Service Account or API key must have the Organization Owner role for the organization. If the identity provider is connected to multiple organizations, the request will fail. Deprecated versions: v2-{2023-01-01}

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            identity_provider_id: Unique string that identifies the identity provider to connect. If using an API version before 11-15-2023, use the legacy 20-hexadecimal digit id. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider. For all other versions, use the 24-hexadecimal digit id.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: The identity provider that you want to update.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders/{quote(str(identity_provider_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=FederationIdentityProvider,
        )

    def revoke_federation_setting_identity_provider_jwks(
        self,
        federation_settings_id: str,
        identity_provider_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Revoke JWKS from One OIDC Identity Provider

        Revokes the JWKS tokens from the requested OIDC identity provider. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations. 

        **Note**: Revoking your JWKS tokens immediately refreshes your IdP public keys from all your Atlas clusters, invalidating previously signed access tokens and logging out all users. You may need to restart your MongoDB clients. All organizations connected to the identity provider will be affected.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            identity_provider_id: Unique 24-hexadecimal digit string that identifies the identity provider to connect.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders/{quote(str(identity_provider_id), safe='')}/jwks"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_federation_setting_identity_provider_metadata(
        self,
        federation_settings_id: str,
        identity_provider_id: str,
    ) -> str:
        """
        Return Metadata of One Identity Provider

        Returns the metadata of one identity provider in the specified federation. To use this resource, the requesting Service Account or API Key must have the Organization Owner role in one of the connected organizations.

        Args:
            federation_settings_id: Unique 24-hexadecimal digit string that identifies your federation.
            identity_provider_id: Legacy 20-hexadecimal digit string that identifies the identity provider. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider.
        """
        path = f"/federationSettings/{quote(str(federation_settings_id), safe='')}/identityProviders/{quote(str(identity_provider_id), safe='')}/metadata.xml"
        return self._client.request(
            method="GET",
            path=path,
            response_model=str,
        )

    def get_org_federation_settings(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OrgFederationSettings:
        """
        Return Federation Settings for One Organization

        Returns information about the federation settings for the specified organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/federationSettings"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgFederationSettings,
        )
