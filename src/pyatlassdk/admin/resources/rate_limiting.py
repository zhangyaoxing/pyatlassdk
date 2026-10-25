"""Generated resource for RateLimiting. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.paginated_rate_limit_endpoint_sets import PaginatedRateLimitEndpointSets
from pyatlassdk.admin.models.rate_limit_endpoint_set_response import RateLimitEndpointSetResponse

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class RateLimiting:
    """Returns details about rate limit policies for the Atlas Administration API."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_rate_limits(
        self,
        *,
        endpoint_path: str | None = None,
        envelope: bool | None = None,
        group_id: str | None = None,
        ip_address: str | None = None,
        items_per_page: int | None = None,
        name: str | None = None,
        org_id: str | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        user_id: str | None = None,
    ) -> PaginatedRateLimitEndpointSets:
        """
        Return All Rate Limits

        Get all rate limits for all v2 Atlas Administration API endpoint sets.

        Args:
            endpoint_path: Filters the returned endpoint sets by the provided endpoint path. Multiple paths may be provided, for example `/rateLimits?endpointPath=%2Fapi%2Fatlas%2Fv2%2Fclusters&endpointPath=%2Fapi%2Fatlas%2Fv2%2Fgroups%2F%7BgroupId%7D%2F`. Replace `/`, `{` and `}` with their URL-encoded values (`%2F`, `%7B` and `%7D` respectively).
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            group_id: Unique 24-hexadecimal digit string that identifies the Atlas Project to request rate limits for. When this parameter is provided, only group scoped endpoint sets are returned and the limits returned are applicable to the specified project. The requesting user must have the Project Read Only role for the specified project.
            ip_address: An IP address to request rate limits for. When this parameter is provided, only IP scoped endpoint sets are returned and the limits returned are applicable to the specified IP address. The requesting user must have the same IP address as the one provided in the request.
            items_per_page: Number of items that the response returns per page.
            name: Filters the returned endpoint sets by the provided endpoint set name. Multiple names may be provided, for example `/rateLimits?name=Name1&name=Name2`. For names that use spaces, replace the space with its URL-encoded value (`%20`).
            org_id: Unique 24-hexadecimal digit string that identifies the Atlas Organization to request rate limits for. When this parameter is provided, only organization scoped endpoint sets are returned and the limits returned are applicable to the specified organization. The requesting user must have the Organization Read Only role for the specified organization.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            user_id: A string that identifies the Atlas user to request rate limits for. The ID can for example be the Service Account Client ID or the API Public Key. When this parameter is provided, only user scoped endpoint sets are returned and the limits returned are applicable to the specified user. The requesting user must be the same as the specified user.
        """
        path = "/rateLimits"
        params = {
            "endpointPath": endpoint_path,
            "envelope": envelope,
            "groupId": group_id,
            "ipAddress": ip_address,
            "itemsPerPage": items_per_page,
            "name": name,
            "orgId": org_id,
            "pageNum": page_num,
            "pretty": pretty,
            "userId": user_id,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedRateLimitEndpointSets,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_rate_limit(
        self,
        endpoint_set_id: str,
        *,
        envelope: bool | None = None,
        group_id: str | None = None,
        ip_address: str | None = None,
        org_id: str | None = None,
        pretty: bool | None = None,
        user_id: str | None = None,
    ) -> RateLimitEndpointSetResponse:
        """
        Return One Rate Limit

        Get one rate limit endpoint set.

        Args:
            endpoint_set_id: The ID of the rate limit endpoint set.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            group_id: Unique 24-hexadecimal digit string that identifies the Atlas Project to request rate limits for. When this parameter is provided, the limits returned are applicable to the specified project. The requesting user must have the Project Read Only role for the specified project.
            ip_address: An IP address to request rate limits for. When this parameter is provided, the limits returned are applicable to the specified IP address. The requesting user must have the same IP address as the one provided in the request.
            org_id: Unique 24-hexadecimal digit string that identifies the Atlas Organization to request rate limits for. When this parameter is provided, the limits returned are applicable to the specified organization. The requesting user must have the Organization Read Only role for the specified organization.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            user_id: A string that identifies the Atlas user to request rate limits for. The ID can for example be the Service Account Client ID or the API Public Key. When this parameter is provided, the limits returned are applicable to the specified user. The requesting user must be the same as the specified user.
        """
        path = f"/rateLimits/{quote(str(endpoint_set_id), safe='')}"
        params = {
            "envelope": envelope,
            "groupId": group_id,
            "ipAddress": ip_address,
            "orgId": org_id,
            "pretty": pretty,
            "userId": user_id,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=RateLimitEndpointSetResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )
