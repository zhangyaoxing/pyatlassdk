"""Generated resource for AlertConfigurations. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.alerts_toggle import AlertsToggle
from pyatlassdk.admin.models.group_alerts_config import GroupAlertsConfig
from pyatlassdk.admin.models.matcher_field_view import MatcherFieldView
from pyatlassdk.admin.models.paginated_alert_config_view import PaginatedAlertConfigView

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class AlertConfigurations:
    """Returns and edits the conditions that trigger alerts and how MongoDB Cloud notifies users. This collection remains under revision and may change."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def list_alert_config_matcher_field_names(
        self,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[MatcherFieldView]:
        """
        Return All Alert Configuration Matchers Field Names

        Get all field names that the `matchers.fieldName` parameter accepts when you create or update an Alert Configuration. You can successfully call this endpoint with any assigned role.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/alertConfigs/matchers/fieldNames"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[MatcherFieldView],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_alert_configs(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAlertConfigView:
        """
        Return All Alert Configurations in One Project

        Returns all alert configurations for one project. These alert configurations apply to any component in the project. Alert configurations define the triggers and notification methods for alerts. 

        This resource remains under revision and may change.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs"
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
            response_model=PaginatedAlertConfigView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_group_alert_config(
        self,
        group_id: str,
        body: GroupAlertsConfig,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupAlertsConfig:
        """
        Create One Alert Configuration in One Project

        Creates one alert configuration for the specified project. Alert configurations define the triggers and notification methods for alerts. 

        This resource remains under revision and may change.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one alert configuration for the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GroupAlertsConfig,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_alert_config(
        self,
        alert_config_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Alert Configuration from One Project

        Removes one alert configuration from the specified project. Use the Return All Alert Configurations for One Project endpoint to retrieve all alert configurations to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            alert_config_id: Unique 24-hexadecimal digit string that identifies the alert configuration.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs/{quote(str(alert_config_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_alert_config(
        self,
        alert_config_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupAlertsConfig:
        """
        Return One Alert Configuration from One Project

        Returns the specified alert configuration from the specified project. Use the Return All Alert Configurations for One Project endpoint to retrieve all alert configurations to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            alert_config_id: Unique 24-hexadecimal digit string that identifies the alert configuration.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs/{quote(str(alert_config_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupAlertsConfig,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def toggle_group_alert_config(
        self,
        alert_config_id: str,
        group_id: str,
        body: AlertsToggle,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupAlertsConfig:
        """
        Toggle State of One Alert Configuration in One Project

        Enables or disables the specified alert configuration in the specified project. The resource enables the specified alert configuration if currently enabled. The resource disables the specified alert configuration if currently disabled.

        **NOTE**: This endpoint updates only the enabled/disabled state for the alert configuration. To update more than just this configuration, see Update One Alert Configuration.

        This resource remains under revision and may change.

        Args:
            alert_config_id: Unique 24-hexadecimal digit string that identifies the alert configuration that triggered this alert.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Enables or disables the specified alert configuration in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs/{quote(str(alert_config_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=GroupAlertsConfig,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_alert_config(
        self,
        alert_config_id: str,
        group_id: str,
        body: GroupAlertsConfig,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupAlertsConfig:
        """
        Update One Alert Configuration in One Project

        Updates one alert configuration in the specified project. Alert configurations define the triggers and notification methods for alerts. 

        **NOTE**: To enable or disable the alert configuration, see Toggle One State of One Alert Configuration in One Project.

        This resource remains under revision and may change.

        Args:
            alert_config_id: Unique 24-hexadecimal digit string that identifies the alert configuration.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates one alert configuration in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alertConfigs/{quote(str(alert_config_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=GroupAlertsConfig,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_alert_alert_configs(
        self,
        alert_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedAlertConfigView:
        """
        Return All Alert Configurations Set for One Alert

        Returns all alert configurations set for the specified alert. Use the Return All Alerts from One Project endpoint to retrieve all alerts to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            alert_id: Unique 24-hexadecimal digit string that identifies the alert.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/alerts/{quote(str(alert_id), safe='')}/alertConfigs"
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
            response_model=PaginatedAlertConfigView,
            accept="application/vnd.atlas.2023-01-01+json",
        )
