"""Generated resource for Maintenance. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyatlassdk.status.models.scheduled_maintenances_response import ScheduledMaintenancesResponse

if TYPE_CHECKING:
    from pyatlassdk.status.client import AtlasStatusClient


class Maintenance:
    """Operations for Maintenance."""

    def __init__(self, client: AtlasStatusClient) -> None:
        self._client = client

    def get_all_scheduled_maintenances(
        self,
    ) -> ScheduledMaintenancesResponse:
        """
        Get All Scheduled Maintenances

        Retrieves the 50 most recent scheduled maintenances, including all states (Scheduled, In Progress, Verifying, Completed).
        """
        path = "/scheduled-maintenances.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=ScheduledMaintenancesResponse,
        )

    def get_active_scheduled_maintenances(
        self,
    ) -> ScheduledMaintenancesResponse:
        """
        Get Active Scheduled Maintenances

        Retrieves a list of active scheduled maintenances (in the In Progress or Verifying states).
        """
        path = "/scheduled-maintenances/active.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=ScheduledMaintenancesResponse,
        )

    def get_upcoming_scheduled_maintenances(
        self,
    ) -> ScheduledMaintenancesResponse:
        """
        Get Upcoming Scheduled Maintenances

        Retrieves a list of upcoming scheduled maintenances (in the Scheduled state).
        """
        path = "/scheduled-maintenances/upcoming.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=ScheduledMaintenancesResponse,
        )
