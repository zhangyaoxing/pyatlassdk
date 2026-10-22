"""Generated resource for EncryptionAtRestUsingCustomerKeyManagement. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.ear_private_endpoint import EARPrivateEndpoint
from pyatlassdk.models.encryption_at_rest import EncryptionAtRest
from pyatlassdk.models.paginated_api_atlas_ear_private_endpoint_view import PaginatedApiAtlasEARPrivateEndpointView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class EncryptionAtRestUsingCustomerKeyManagement:
    """Returns and edits the Encryption at Rest using Customer Key Management configuration. MongoDB Cloud encrypts all storage whether or not you use your own key management."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_encryption_at_rest(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EncryptionAtRest:
        """
        Return One Configuration for Encryption at Rest Using Customer-Managed Keys for One Project

        Returns the configuration for encryption at rest using the keys you manage through your cloud provider. MongoDB Cloud encrypts all storage even if you don't use your own key management.

        **LIMITED TO M10 OR GREATER:** MongoDB Cloud limits this feature to dedicated cluster tiers of M10 and greater.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/encryptionAtRest"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EncryptionAtRest,
        )

    def update_group_encryption_at_rest(
        self,
        group_id: str,
        body: EncryptionAtRest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EncryptionAtRest:
        """
        Update Encryption at Rest Configuration in One Project

        Updates the configuration for encryption at rest using the keys you manage through your cloud provider. MongoDB Cloud encrypts all storage even if you don't use your own key management. This feature isn't available for `M0` free clusters, `M2`, `M5`, or serverless clusters.

         After you configure at least one Encryption at Rest using a Customer Key Management provider for the MongoDB Cloud project, Project Owners can enable Encryption at Rest using Customer Key Management for each MongoDB Cloud cluster for which they require encryption. The Encryption at Rest using Customer Key Management provider doesn't have to match the cluster cloud service provider. MongoDB Cloud doesn't automatically rotate user-managed encryption keys. Defer to your preferred Encryption at Rest using Customer Key Management provider's documentation and guidance for best practices on key rotation. MongoDB Cloud automatically creates a 90-day key rotation alert when you configure Encryption at Rest using Customer Key Management using your Key Management in an MongoDB Cloud project. MongoDB Cloud encrypts all storage whether or not you use your own key management.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Required parameters depend on whether someone has enabled Encryption at Rest using Customer Key Management: If you have enabled Encryption at Rest using Customer Key Management (CMK), Atlas requires all of the parameters for the desired encryption provider. - To use AWS Key Management Service (KMS), MongoDB Cloud requires all the fields in the `awsKms` object. - To use Azure Key Vault, MongoDB Cloud requires all the fields in the `azureKeyVault` object. - To use Google Cloud Key Management Service (KMS), MongoDB Cloud requires all the fields in the `googleCloudKms` object For authentication, you must provide either `serviceAccountKey` (static credentials) or `roleId` (service-account–based authentication) Once `roleId` is configured, `serviceAccountKey` is no longer supported. If you enabled Encryption at Rest using Customer Key Management, administrators can pass only the changed fields for the `awsKms`, `azureKeyVault`, or `googleCloudKms` object to update the configuration to this endpoint.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/encryptionAtRest"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=EncryptionAtRest,
        )

    def list_group_encryption_at_rest_private_endpoints(
        self,
        cloud_provider: Literal["AZURE", "AWS"],
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedApiAtlasEARPrivateEndpointView:
        """
        Return Private Endpoints for Encryption at Rest Using Customer Key Management for One Cloud Provider in One Project

        Returns the private endpoints of the specified cloud provider for encryption at rest using customer key management.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider for the private endpoints to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/encryptionAtRest/{quote(str(cloud_provider), safe='')}/privateEndpoints"
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
            response_model=PaginatedApiAtlasEARPrivateEndpointView,
        )

    def create_group_encryption_at_rest_private_endpoint(
        self,
        cloud_provider: Literal["AZURE", "AWS"],
        group_id: str,
        body: EARPrivateEndpoint,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EARPrivateEndpoint:
        """
        Create One Private Endpoint for Encryption at Rest Using Customer Key Management for One Cloud Provider in One Project

        Creates a private endpoint in the specified region for encryption at rest using customer key management.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider for the private endpoint to create.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates a private endpoint in the specified region.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/encryptionAtRest/{quote(str(cloud_provider), safe='')}/privateEndpoints"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=EARPrivateEndpoint,
        )

    def request_group_encryption_at_rest_private_endpoint_deletion(
        self,
        cloud_provider: Literal["AZURE", "AWS"],
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Private Endpoint for Encryption at Rest Using Customer Key Management for One Cloud Provider from One Project

        Deletes one private endpoint, identified by its ID, for encryption at rest using Customer Key Management.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider of the private endpoint to delete.
            endpoint_id: Unique 24-hexadecimal digit string that identifies the private endpoint to delete.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/encryptionAtRest/{quote(str(cloud_provider), safe='')}/privateEndpoints/{quote(str(endpoint_id), safe='')}"
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

    def get_group_encryption_at_rest_private_endpoint(
        self,
        cloud_provider: Literal["AZURE", "AWS"],
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> EARPrivateEndpoint:
        """
        Return One Private Endpoint for Encryption at Rest Using Customer Key Management for One Cloud Provider in One Project

        Returns one private endpoint, identified by its ID, for encryption at rest using Customer Key Management.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider of the private endpoint.
            endpoint_id: Unique 24-hexadecimal digit string that identifies the private endpoint.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/encryptionAtRest/{quote(str(cloud_provider), safe='')}/privateEndpoints/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EARPrivateEndpoint,
        )
