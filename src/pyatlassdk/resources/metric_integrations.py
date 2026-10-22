"""Generated resource for MetricIntegrations. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.metric_integration_request import MetricIntegrationRequest
from pyatlassdk.models.metric_integration_response import MetricIntegrationResponse
from pyatlassdk.models.metric_integration_update_request import MetricIntegrationUpdateRequest
from pyatlassdk.models.paginated_metric_integration_response import PaginatedMetricIntegrationResponse

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class MetricIntegrations:
    """Returns, creates, updates, and removes metric integration configurations for a project."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_metric_integrations(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        integration_type: str | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        provider_type: str | None = None,
    ) -> PaginatedMetricIntegrationResponse:
        """
        Return All Active Metric Integrations

        Returns all metric integration configurations for the project. Optionally filter by integration type and provider type.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            integration_type: Optional filter by integration type (e.g., `OTEL`).
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            provider_type: Optional filter by provider type (e.g., `CUSTOM`). When specified, `integrationType` must also be specified.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/metricIntegrations"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "integrationType": integration_type,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "providerType": provider_type,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedMetricIntegrationResponse,
        )

    def create_group_metric_integration(
        self,
        group_id: str,
        body: MetricIntegrationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> MetricIntegrationResponse:
        """
        Create One Metric Integration

        Creates a new metric integration configuration identified by a unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Metric integration configuration to create.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/metricIntegrations"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=MetricIntegrationResponse,
        )

    def delete_group_metric_integration(
        self,
        group_id: str,
        metric_integration_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Metric Integration

        Removes the configuration for one metric integration identified by its unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            metric_integration_id: Unique identifier of the metric integration configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/metricIntegrations/{quote(str(metric_integration_id), safe='')}"
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

    def get_group_metric_integration(
        self,
        group_id: str,
        metric_integration_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> MetricIntegrationResponse:
        """
        Return One Metric Integration

        Returns the configuration for one metric integration identified by its unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            metric_integration_id: Unique identifier of the metric integration configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/metricIntegrations/{quote(str(metric_integration_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=MetricIntegrationResponse,
        )

    def update_group_metric_integration(
        self,
        group_id: str,
        metric_integration_id: str,
        body: MetricIntegrationUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> MetricIntegrationResponse:
        """
        Update One Metric Integration

        Updates the configuration for one metric integration identified by its unique ID.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            metric_integration_id: Unique identifier of the metric integration configuration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updated metric integration configuration.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/metricIntegrations/{quote(str(metric_integration_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=MetricIntegrationResponse,
        )
