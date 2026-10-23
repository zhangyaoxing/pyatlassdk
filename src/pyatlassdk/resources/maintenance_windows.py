"""Generated resource for MaintenanceWindows. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.group_maintenance_window import GroupMaintenanceWindow

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class MaintenanceWindows:
    """Returns, edits, and removes maintenance windows. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. You can defer a scheduled maintenance event for a project up to two times. Deferred maintenance events occur during your preferred maintenance window exactly one week after the previously scheduled date and time."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def reset_group_maintenance_window(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Reset One Maintenance Window for One Project

        Resets the maintenance window for the specified project. Urgent maintenance activities such as security patches can't wait for your chosen window. MongoDB Cloud starts those maintenance activities when needed. After you schedule maintenance for your cluster, you can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/maintenanceWindow"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_maintenance_window(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GroupMaintenanceWindow:
        """
        Return One Maintenance Window for One Project

        Returns the maintenance window for the specified project. MongoDB Cloud starts those maintenance activities when needed. You can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/maintenanceWindow"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupMaintenanceWindow,
        )

    def update_group_maintenance_window(
        self,
        group_id: str,
        body: GroupMaintenanceWindow,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Update One Maintenance Window for One Project

        Updates the maintenance window for the specified project. Urgent maintenance activities such as security patches can't wait for your chosen window. MongoDB Cloud starts those maintenance activities when needed. After you schedule maintenance for your cluster, you can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time. Updating the maintenance window will reset any maintenance deferrals for this project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Updates the maintenance window for the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/maintenanceWindow"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=Any,
        )

    def toggle_group_maintenance_window_auto_defer(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Toggle Automatic Deferral of Maintenance for One Project

        Toggles automatic deferral of the maintenance window for the specified project. When automatic deferral is enabled, all maintenance windows are deferred for one week. This endpoint controls the same underlying feature as the `autoDeferOnceEnabled` field in the PATCH `/maintenanceWindow` endpoint. The difference is that this endpoint toggles the current value (switches from enabled to disabled or vice versa), while the `autoDeferOnceEnabled` field allows you to set a specific value. For most use cases, the PATCH endpoint with `autoDeferOnceEnabled` is recommended because it allows setting an explicit value rather than toggling.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/maintenanceWindow/autoDefer"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
        )

    def defer_group_maintenance_window(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Defer One Maintenance Window for One Project

        Defers the maintenance window for the specified project. Urgent maintenance activities such as security patches can't wait for your chosen window. MongoDB Cloud starts those maintenance activities when needed. After you schedule maintenance for your cluster, you can't change your maintenance window until the current maintenance efforts complete. The maintenance procedure that MongoDB Cloud performs requires at least one replica set election during the maintenance window per replica set. Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or unexpected system issues could delay the start time. You can only defer maintenance within a limited time window before the scheduled maintenance starts; deferral requests made outside of this window return an error.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/maintenanceWindow/defer"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            response_model=Any,
        )
