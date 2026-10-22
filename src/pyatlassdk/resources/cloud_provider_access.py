"""Generated resource for CloudProviderAccess. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.cloud_provider_access_role import CloudProviderAccessRole
from pyatlassdk.models.cloud_provider_access_role_request import CloudProviderAccessRoleRequest
from pyatlassdk.models.cloud_provider_access_role_request_update import CloudProviderAccessRoleRequestUpdate
from pyatlassdk.models.cloud_provider_access_roles import CloudProviderAccessRoles

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class CloudProviderAccess:
    """Returns, adds, authorizes, and removes AWS IAM roles in Atlas."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_cloud_provider_access(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderAccessRoles:
        """
        Return All Cloud Provider Access Roles

        Returns all cloud provider access roles with access to the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/cloudProviderAccess"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CloudProviderAccessRoles,
        )

    def create_group_cloud_provider_access(
        self,
        group_id: str,
        body: CloudProviderAccessRoleRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderAccessRole:
        """
        Create One Cloud Provider Access Role

        Creates one access role for the specified cloud provider. Some MongoDB Cloud features use these cloud provider access roles for authentication. For the GCP provider, if the project folder is not yet provisioned, Atlas will now create the role asynchronously. An intermediate role with status `IN_PROGRESS` will be returned, and the final service account will be provisioned. Once the GCP project is set up, subsequent requests will create the service account synchronously.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one role for the specified cloud provider.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/cloudProviderAccess"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=CloudProviderAccessRole,
        )

    def deauthorize_group_cloud_provider_access_role(
        self,
        cloud_provider: Literal["AWS", "AZURE", "GCP"],
        group_id: str,
        role_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Deauthorize One Cloud Provider Access Role

        Revokes access to the specified project for the specified access role.

        Args:
            cloud_provider: Human-readable label that identifies the cloud provider of the role to deauthorize.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            role_id: Unique 24-hexadecimal digit string that identifies the role. Amazon Web Services (AWS) IAM roles and Google Service Accounts return this value as `roleId`. Azure Service Principals return it as `_id`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/cloudProviderAccess/{quote(str(cloud_provider), safe='')}/{quote(str(role_id), safe='')}"
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

    def get_group_cloud_provider_access(
        self,
        group_id: str,
        role_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderAccessRole:
        """
        Return One Cloud Provider Access Role

        Returns the access role with the specified id and with access to the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            role_id: Unique 24-hexadecimal digit string that identifies the role. Amazon Web Services (AWS) IAM roles and Google Service Accounts return this value as `roleId`. Azure Service Principals return it as `_id`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/cloudProviderAccess/{quote(str(role_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=CloudProviderAccessRole,
        )

    def authorize_group_cloud_provider_access_role(
        self,
        group_id: str,
        role_id: str,
        body: CloudProviderAccessRoleRequestUpdate,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> CloudProviderAccessRole:
        """
        Authorize One Cloud Provider Access Role

        Grants access to the specified project for the specified access role. This API endpoint is one step in a procedure to create unified access for MongoDB Cloud services. This is not required for GCP service account access.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            role_id: Unique 24-hexadecimal digit string that identifies the role. Amazon Web Services (AWS) IAM roles and Google Service Accounts return this value as `roleId`. Azure Service Principals return it as `_id`.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Grants access to the specified project for the specified access role.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/cloudProviderAccess/{quote(str(role_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=CloudProviderAccessRole,
        )
