"""Generated resource for Alerts. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.acknowledge_alert import AcknowledgeAlert
from pyatlassdk.models.alert_view_for_nds_group import AlertViewForNdsGroup
from pyatlassdk.models.paginated_alert_view import PaginatedAlertView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class Alerts:
    """Returns and acknowledges alerts that MongoDB Cloud triggers based on the alert conditions that you define. This collection remains under revision and may change."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_alert_config_alerts(
        self,
        alert_config_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAlertView:
        """
        Return All Open Alerts for One Alert Configuration

        Returns all open alerts that the specified alert configuration triggers. These alert configurations apply to the specified project only. Alert configurations define the triggers and notification methods for alerts. Open alerts have been triggered but remain unacknowledged. Use the Return All Alert Configurations for One Project endpoint to retrieve all alert configurations to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            alert_config_id: Unique 24-hexadecimal digit string that identifies the alert configuration.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs/{quote(str(alert_config_id), safe='')}/alerts"
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
            response_model=PaginatedAlertView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_alerts(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
        status: Literal["OPEN", "TRACKING", "CLOSED"] | None = None,
    ) -> PaginatedAlertView:
        """
        Return All Alerts from One Project

        Returns all alerts. These alerts apply to all components in one project. You receive an alert when a monitored component meets or exceeds a value you set.

        This resource remains under revision and may change.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            status: Status of the alerts to return. Omit this parameter to return all alerts in all statuses. TRACKING indicates the alert condition exists but has not persisted for the minimum notification delay. OPEN indicates the alert condition currently exists. CLOSED indicates the alert condition has been resolved.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alerts"
        params = {
            "envelope": envelope,
            "includeCount": include_count,
            "itemsPerPage": items_per_page,
            "pageNum": page_num,
            "pretty": pretty,
            "status": status,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PaginatedAlertView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_alert(
        self,
        alert_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AlertViewForNdsGroup:
        """
        Return One Alert from One Project

        Returns one alert. This alert applies to any component in one project. You receive an alert when a monitored component meets or exceeds a value you set. Use the Return All Alerts from One Project endpoint to retrieve all alerts to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            alert_id: Unique 24-hexadecimal digit string that identifies the alert.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alerts/{quote(str(alert_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AlertViewForNdsGroup,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def acknowledge_group_alert(
        self,
        alert_id: str,
        group_id: str,
        body: AcknowledgeAlert,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AlertViewForNdsGroup:
        """
        Acknowledge One Alert from One Project

        Confirms receipt of one existing alert. This alert applies to any component in one project. Acknowledging an alert prevents successive notifications. You receive an alert when a monitored component meets or exceeds a value you set until you acknowledge the alert. Use the Return All Alerts from One Project endpoint to retrieve all alerts to which the authenticated user has access.

        This resource remains under revision and may change. Deprecated versions: v2-{2023-01-01}

        Args:
            alert_id: Unique 24-hexadecimal digit string that identifies the alert.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Acknowledges or unacknowledges one alert.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alerts/{quote(str(alert_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AlertViewForNdsGroup,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )
