"""Generated resource for AIModelRateLimits. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.ai_model_rate_limit_response import AiModelRateLimitResponse
from pyatlassdk.admin.models.ai_models_rate_limit_update_request import AiModelsRateLimitUpdateRequest
from pyatlassdk.admin.models.paginated_atlas_ai_model_rate_limits_response import PaginatedAtlasAiModelRateLimitsResponse

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class AIModelRateLimits:
    """Returns, adds, edits, and removes Rate Limits for your AI Models."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def get_group_ai_model_api_cloud_geography_model_group_name_rate_limits(
        self,
        cloud: Literal["ANY"],
        geography: Literal["ANY"],
        group_id: str,
        model_group_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelRateLimitResponse:
        """
        Return Single AI Model Rate Limit for One Group

        Retrieve a single scoped AI model rate limit for the given group.

        Args:
            cloud: Cloud provider scope. Must be "ANY". Additional values will be supported in future API versions.
            geography: Geography scope. Must be "ANY". Additional values will be supported in future API versions.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            model_group_name: The name of the model group to be retrieved.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiClouds/{quote(str(cloud), safe='')}/geographies/{quote(str(geography), safe='')}/modelGroupNames/{quote(str(model_group_name), safe='')}/rateLimits"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AiModelRateLimitResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def update_group_ai_model_api_cloud_geography_model_group_name_rate_limits(
        self,
        cloud: Literal["ANY"],
        geography: Literal["ANY"],
        group_id: str,
        model_group_name: str,
        body: AiModelsRateLimitUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelRateLimitResponse:
        """
        Update AI Model Rate Limit

        Update a scoped AI model rate limit for the given model group.

        Args:
            cloud: Cloud provider scope. Must be "ANY". Additional values will be supported in future API versions.
            geography: Geography scope. Must be "ANY". Additional values will be supported in future API versions.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            model_group_name: The name of the model group to be updated.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: A request containing the new rate limits for the given model group.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiClouds/{quote(str(cloud), safe='')}/geographies/{quote(str(geography), safe='')}/modelGroupNames/{quote(str(model_group_name), safe='')}/rateLimits"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AiModelRateLimitResponse,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def reset_group_ai_model_api_cloud_geography_model_group_name_rate_limits(
        self,
        cloud: Literal["ANY"],
        geography: Literal["ANY"],
        group_id: str,
        model_group_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelRateLimitResponse:
        """
        Reset AI Model Rate Limit for One Model Group

        Reset the scoped AI model rate limit for the given model group to default values.

        Args:
            cloud: Cloud provider scope. Must be "ANY". Additional values will be supported in future API versions.
            geography: Geography scope. Must be "ANY". Additional values will be supported in future API versions.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            model_group_name: The name of the model group to be reset to default rate limits.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiClouds/{quote(str(cloud), safe='')}/geographies/{quote(str(geography), safe='')}/modelGroupNames/{quote(str(model_group_name), safe='')}/rateLimits:reset"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=AiModelRateLimitResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_group_ai_model_api_rate_limits(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasAiModelRateLimitsResponse:
        """
        Return AI Model Rate Limits for One Group

        Retrieve AI model rate limits for the given group.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiRateLimits"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedAtlasAiModelRateLimitsResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def reset_group_ai_model_api_rate_limits(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasAiModelRateLimitsResponse:
        """
        Reset AI Model Rate Limits for Group

        Reset the AI Model rate limits for the given group to default values.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiRateLimits:reset"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=PaginatedAtlasAiModelRateLimitsResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_org_ai_model_api_cloud_geography_model_group_name_rate_limits(
        self,
        cloud: Literal["ANY"],
        geography: Literal["ANY"],
        model_group_name: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelRateLimitResponse:
        """
        Return Single AI Model Rate Limit for One Organization

        Retrieve a single scoped AI model rate limit for the given organization.

        Args:
            cloud: Cloud provider scope. Must be "ANY". Additional values will be supported in future API versions.
            geography: Geography scope. Must be "ANY". Additional values will be supported in future API versions.
            model_group_name: The name of the model group to be retrieved.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/aiModelApiClouds/{quote(str(cloud), safe='')}/geographies/{quote(str(geography), safe='')}/modelGroupNames/{quote(str(model_group_name), safe='')}/rateLimits"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AiModelRateLimitResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_org_ai_model_api_rate_limits(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasAiModelRateLimitsResponse:
        """
        Return AI Model Rate Limits for One Organization

        Retrieve AI model rate limits for the given organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/aiModelApiRateLimits"
        params = {
            "envelope": envelope,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedAtlasAiModelRateLimitsResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )
