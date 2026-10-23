"""Generated resource for ThirdPartyIntegrations. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.paginated_integration_view import PaginatedIntegrationView
from pyatlassdk.models.third_party_integration import ThirdPartyIntegration

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ThirdPartyIntegrations:
    """
    Returns, adds, edits, and removes third-party service integration configurations. MongoDB Cloud sends alerts to each third-party service that you configure.

    **IMPORTANT**: Each project can only have one configuration per `integrationType`.
    """

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_integrations(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedIntegrationView:
        """
        Return All Active Third-Party Service Integrations

        Returns the settings that permit integrations with all configured third-party services. These settings apply to all databases managed in one MongoDB Cloud project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/integrations"
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
            response_model=PaginatedIntegrationView,
        )

    def delete_group_integration(
        self,
        group_id: str,
        integration_type: Literal["PAGER_DUTY", "SLACK", "DATADOG", "NEW_RELIC", "OPS_GENIE", "VICTOR_OPS", "WEBHOOK", "HIP_CHAT", "PROMETHEUS", "MICROSOFT_TEAMS"],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Third-Party Service Integration

        Removes the settings that permit configuring one third-party service integration. These settings apply to all databases managed in one MongoDB Cloud project. If you delete an integration from a project, you remove that integration configuration only for that project. This action doesn't affect any other project or organization's configured `{INTEGRATION-TYPE}` integrations.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            integration_type: Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/integrations/{quote(str(integration_type), safe='')}"
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

    def get_group_integration(
        self,
        group_id: str,
        integration_type: Literal["PAGER_DUTY", "SLACK", "DATADOG", "NEW_RELIC", "OPS_GENIE", "VICTOR_OPS", "WEBHOOK", "HIP_CHAT", "PROMETHEUS", "MICROSOFT_TEAMS"],
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ThirdPartyIntegration:
        """
        Return One Third-Party Service Integration

        Returns the settings for configuring integration with one third-party service. These settings apply to all databases managed in one MongoDB Cloud project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            integration_type: Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/integrations/{quote(str(integration_type), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ThirdPartyIntegration,
        )

    def create_group_integration(
        self,
        group_id: str,
        integration_type: Literal["PAGER_DUTY", "SLACK", "DATADOG", "NEW_RELIC", "OPS_GENIE", "VICTOR_OPS", "WEBHOOK", "HIP_CHAT", "PROMETHEUS", "MICROSOFT_TEAMS"],
        body: ThirdPartyIntegration,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedIntegrationView:
        """
        Create One Third-Party Service Integration

        Adds the settings for configuring one third-party service integration. These settings apply to all databases managed in the specified MongoDB Cloud project. Each project can have only one configuration per `{INTEGRATION-TYPE}`.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            integration_type: Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Third-party integration that you want to configure for your project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/integrations/{quote(str(integration_type), safe='')}"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedIntegrationView,
        )

    def update_group_integration(
        self,
        group_id: str,
        integration_type: Literal["PAGER_DUTY", "SLACK", "DATADOG", "NEW_RELIC", "OPS_GENIE", "VICTOR_OPS", "WEBHOOK", "HIP_CHAT", "PROMETHEUS", "MICROSOFT_TEAMS"],
        body: ThirdPartyIntegration,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedIntegrationView:
        """
        Update One Third-Party Service Integration

        Updates the settings for configuring integration with one third-party service. These settings apply to all databases managed in one MongoDB Cloud project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            integration_type: Human-readable label that identifies the service which you want to integrate with MongoDB Cloud.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Third-party integration that you want to configure for your project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/integrations/{quote(str(integration_type), safe='')}"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedIntegrationView,
        )
