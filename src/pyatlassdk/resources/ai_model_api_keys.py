"""Generated resource for AIModelAPIKeys. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.ai_model_api_key_create_request import AiModelApiKeyCreateRequest
from pyatlassdk.models.ai_model_api_key_response import AiModelApiKeyResponse
from pyatlassdk.models.ai_model_api_key_update_request import AiModelApiKeyUpdateRequest
from pyatlassdk.models.paginated_atlas_ai_model_api_keys_response import PaginatedAtlasAiModelApiKeysResponse

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class AIModelAPIKeys:
    """Returns, adds, edits, and removes API Keys for your AI Models."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_ai_model_api_keys(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasAiModelApiKeysResponse:
        """
        Return AI Model API Keys for One Group

        Retrieve AI model API keys for the given group.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiKeys"
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
            response_model=PaginatedAtlasAiModelApiKeysResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def create_group_ai_model_api_key(
        self,
        group_id: str,
        body: AiModelApiKeyCreateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelApiKeyResponse:
        """
        Create New AI Model API Key

        Create a new AI model API key for the given group.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: A request containing the name, cloud, and geography of the new API key.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiKeys"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=AiModelApiKeyResponse,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def delete_group_ai_model_api_key(
        self,
        api_key_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete Existing AI Model API Key

        Delete an existing AI model API key in the given group.

        Args:
            api_key_id: The id of the API key to be deleted.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiKeys/{quote(str(api_key_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_group_ai_model_api_key(
        self,
        api_key_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelApiKeyResponse:
        """
        Return Single AI Model API Key for One Group

        Retrieve a single AI model API key for the given group.

        Args:
            api_key_id: The id of the API key to be retrieved.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiKeys/{quote(str(api_key_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AiModelApiKeyResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def update_group_ai_model_api_key(
        self,
        api_key_id: str,
        group_id: str,
        body: AiModelApiKeyUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelApiKeyResponse:
        """
        Update Existing AI Model API Key

        Update an existing AI model API key in the given group. Only the name can be updated; scope is immutable after creation.

        Args:
            api_key_id: The id of the API key to be updated.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: A request containing the new name for the API key.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/aiModelApiKeys/{quote(str(api_key_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AiModelApiKeyResponse,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def list_org_ai_model_api_keys(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAtlasAiModelApiKeysResponse:
        """
        Return AI Model API Keys for One Organization

        Retrieve AI model API keys for the given organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/aiModelApiKeys"
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
            response_model=PaginatedAtlasAiModelApiKeysResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def get_org_ai_model_api_key(
        self,
        api_key_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AiModelApiKeyResponse:
        """
        Return Single AI Model API Key for One Organization

        Retrieve a single AI model API key for the given organization.

        Args:
            api_key_id: The id of the API key to be retrieved.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/aiModelApiKeys/{quote(str(api_key_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AiModelApiKeyResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )
