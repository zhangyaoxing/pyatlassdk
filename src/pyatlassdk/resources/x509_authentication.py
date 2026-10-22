"""Generated resource for X509Authentication. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.paginated_user_cert_view import PaginatedUserCertView
from pyatlassdk.models.user_cert import UserCert
from pyatlassdk.models.user_security import UserSecurity

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class X509Authentication:
    """Returns, edits, and removes user-managed X.509 configurations. Also returns and generates MongoDB Cloud-managed X.509 certificates for database users. The following resources help manage database users who authenticate using X.509 certificates. You can manage these X.509 certificates or let MongoDB Cloud do it for you. If MongoDB Cloud manages your certificates, it also manages your Certificate Authority and can generate certificates for your database users. No additional X.509 configuration is required. If you manage your certificates, you must provide a Certificate Authority and generate certificates for your database users."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_database_user_certs(
        self,
        group_id: str,
        username: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedUserCertView:
        """
        Return All X.509 Certificates Assigned to One Database User

        Returns all unexpired X.509 certificates for the specified MongoDB user. This MongoDB user belongs to one project. Atlas manages these certificates and the MongoDB user.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            username: Human-readable label that represents the MongoDB database user account whose certificates you want to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/databaseUsers/{quote(str(username), safe='')}/certs"
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
            response_model=PaginatedUserCertView,
        )

    def create_group_database_user_cert(
        self,
        group_id: str,
        username: str,
        body: UserCert,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> str:
        """
        Create One X.509 Certificate for One Database User

        Generates one X.509 certificate for the specified MongoDB user. Atlas manages the            certificate and MongoDB user that belong to one project.


        To get MongoDB Cloud to generate a managed certificate for a database user, set `"x509Type" : "MANAGED"` on the desired MongoDB Database User.

        If you are managing your own Certificate Authority (CA) in Self-Managed X.509 mode, you must generate certificates for database users using your own CA.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            username: Human-readable label that represents the MongoDB database user account for whom to create a certificate.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Generates one X.509 certificate for the specified MongoDB user.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/databaseUsers/{quote(str(username), safe='')}/certs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=str,
        )

    def disable_group_user_security_customer_x509(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> UserSecurity:
        """
        Disable Customer-Managed X.509

        Clears the customer-managed X.509 settings on a project, including the uploaded Certificate Authority, which disables self-managed X.509.

         Updating this configuration triggers a rolling restart of the database. You must have the Project Owner role to use this endpoint.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/userSecurity/customerX509"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=UserSecurity,
        )
