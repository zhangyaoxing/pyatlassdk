"""Generated resource for ResourcePolicies. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.api_atlas_non_compliant_resource_view import ApiAtlasNonCompliantResourceView
from pyatlassdk.models.api_atlas_resource_policy_create_view import ApiAtlasResourcePolicyCreateView
from pyatlassdk.models.api_atlas_resource_policy_edit_view import ApiAtlasResourcePolicyEditView
from pyatlassdk.models.api_atlas_resource_policy_view import ApiAtlasResourcePolicyView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ResourcePolicies:
    """Configure and manage Atlas Resource Policies within your organization."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_org_non_compliant_resources(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[ApiAtlasNonCompliantResourceView]:
        """
        Return All Non-Compliant Resources

        Return all non-compliant resources for an organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/nonCompliantResources"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[ApiAtlasNonCompliantResourceView],
        )

    def list_org_resource_policies(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[ApiAtlasResourcePolicyView]:
        """
        Return All Atlas Resource Policies

        Return all Atlas Resource Policies for the organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/resourcePolicies"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[ApiAtlasResourcePolicyView],
        )

    def create_org_resource_policy(
        self,
        org_id: str,
        body: ApiAtlasResourcePolicyCreateView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasResourcePolicyView:
        """
        Create One Atlas Resource Policy

        Create one Atlas Resource Policy for an organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Atlas Resource Policy to create.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/resourcePolicies"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ApiAtlasResourcePolicyView,
        )

    def delete_org_resource_policy(
        self,
        org_id: str,
        resource_policy_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Atlas Resource Policy

        Delete one Atlas Resource Policy for an organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            resource_policy_id: Unique 24-hexadecimal digit string that identifies an atlas resource policy.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/resourcePolicies/{quote(str(resource_policy_id), safe='')}"
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

    def get_org_resource_policy(
        self,
        org_id: str,
        resource_policy_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasResourcePolicyView:
        """
        Return One Atlas Resource Policy

        Return one Atlas Resource Policy for an organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            resource_policy_id: Unique 24-hexadecimal digit string that identifies an atlas resource policy.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/resourcePolicies/{quote(str(resource_policy_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiAtlasResourcePolicyView,
        )

    def update_org_resource_policy(
        self,
        org_id: str,
        resource_policy_id: str,
        body: ApiAtlasResourcePolicyEditView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasResourcePolicyView:
        """
        Update One Atlas Resource Policy

        Update one Atlas Resource Policy for an organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            resource_policy_id: Unique 24-hexadecimal digit string that identifies an atlas resource policy.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Atlas Resource Policy to update.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/resourcePolicies/{quote(str(resource_policy_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ApiAtlasResourcePolicyView,
        )

    def validate_org_resource_policies(
        self,
        org_id: str,
        body: ApiAtlasResourcePolicyCreateView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiAtlasResourcePolicyView:
        """
        Validate One Atlas Resource Policy

        Validate one Atlas Resource Policy for an organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Atlas Resource Policy to create.
        """
        path = f"/api/atlas/v2/orgs/{quote(str(org_id), safe='')}/resourcePolicies:validate"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ApiAtlasResourcePolicyView,
        )
