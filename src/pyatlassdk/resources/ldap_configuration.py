"""Generated resource for LDAPConfiguration. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.ldap_verify_connectivity_job_request import LDAPVerifyConnectivityJobRequest
from pyatlassdk.models.ldap_verify_connectivity_job_request_params import LDAPVerifyConnectivityJobRequestParams
from pyatlassdk.models.user_security import UserSecurity

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class LDAPConfiguration:
    """Returns, edits, verifies, and removes LDAP configurations. An LDAP configuration defines settings for MongoDB Cloud to connect to your LDAP server over TLS for user authentication and authorization. Your LDAP server must be visible to the internet or connected to your MongoDB Cloud cluster with VPC Peering. Also, your LDAP server must use TLS. You must have the MongoDB Cloud admin user privilege to use these endpoints. Also, to configure user authentication and authorization with LDAPS, your cluster must run MongoDB 3.6 or higher. Groups for which you have configured LDAPS can't create a cluster using a version of MongoDB 3.6 or lower."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_user_security(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserSecurity:
        """
        Return LDAP or X.509 Configuration

        Returns the current LDAP configuration for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/userSecurity"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=UserSecurity,
        )

    def update_group_user_security(
        self,
        group_id: str,
        body: UserSecurity,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserSecurity:
        """
        Update LDAP or X.509 Configuration

        Edits the LDAP configuration for the specified project.

        Updating this configuration triggers a rolling restart of the database.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the LDAP configuration for the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/userSecurity"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=UserSecurity,
        )

    def delete_group_user_security_ldap_user_to_dn_mapping(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> UserSecurity:
        """
        Remove LDAP User to DN Mapping

        Removes the current LDAP Distinguished Name mapping captured in the ``userToDNMapping`` document from the LDAP configuration for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/userSecurity/ldap/userToDNMapping"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=UserSecurity,
        )

    def verify_group_user_security_ldap(
        self,
        group_id: str,
        body: LDAPVerifyConnectivityJobRequestParams,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LDAPVerifyConnectivityJobRequest:
        """
        Verify LDAP Configuration in One Project

        Verifies the LDAP configuration for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: The LDAP configuration for the specified project that you want to verify.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/userSecurity/ldap/verify"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=LDAPVerifyConnectivityJobRequest,
        )

    def get_group_user_security_ldap_verify(
        self,
        group_id: str,
        request_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LDAPVerifyConnectivityJobRequest:
        """
        Return Status of LDAP Configuration Verification in One Project

        Returns the status of one request to verify one LDAP configuration for the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            request_id: Unique string that identifies the request to verify an Lightweight Directory Access Protocol (LDAP) configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/userSecurity/ldap/verify/{quote(str(request_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=LDAPVerifyConnectivityJobRequest,
        )
