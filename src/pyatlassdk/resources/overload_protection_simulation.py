"""Generated resource for OverloadProtectionSimulation. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.overload_protection_simulation_request import OverloadProtectionSimulationRequest
from pyatlassdk.models.overload_protection_simulation_response import OverloadProtectionSimulationResponse
from pyatlassdk.models.paginated_overload_protection_simulation_response import PaginatedOverloadProtectionSimulationResponse

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class OverloadProtectionSimulation:
    """Returns and starts overload protection simulations for a cluster."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_cluster_overload_simulations(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedOverloadProtectionSimulationResponse:
        """
        Return All Overload Protection Simulations

        Returns all overload protection simulations for one cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster on which the overload protection simulations are running.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/overloadSimulations"
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
            response_model=PaginatedOverloadProtectionSimulationResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def create_group_cluster_overload_simulation(
        self,
        cluster_name: str,
        group_id: str,
        body: OverloadProtectionSimulationRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OverloadProtectionSimulationResponse:
        """
        Create One Overload Protection Simulation

        Starts an overload protection simulation for one cluster. Returns a 409 if a simulation is already in progress or completed; DELETE the existing simulation before starting a new one.

        Args:
            cluster_name: Human-readable label that identifies the cluster on which to start the overload protection simulation.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details of the overload protection simulation to start. Valid durations (in seconds): 900, 3600, 28800, 86400.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/overloadSimulations"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=OverloadProtectionSimulationResponse,
            accept="application/vnd.atlas.2025-03-12+json",
            content_type="application/vnd.atlas.2025-03-12+json",
        )

    def delete_group_cluster_overload_simulation(
        self,
        cluster_name: str,
        group_id: str,
        simulation_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete One Overload Protection Simulation

        Deletes the overload protection simulation for one cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster on which the overload protection simulation is running.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            simulation_id: Unique 24-hexadecimal digit string that identifies the overload protection simulation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/overloadSimulations/{quote(str(simulation_id), safe='')}"
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

    def get_group_cluster_overload_simulation(
        self,
        cluster_name: str,
        group_id: str,
        simulation_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> OverloadProtectionSimulationResponse:
        """
        Return One Overload Protection Simulation

        Returns the overload protection simulation for one cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster on which the overload protection simulation is running.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            simulation_id: Unique 24-hexadecimal digit string that identifies the overload protection simulation.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/overloadSimulations/{quote(str(simulation_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OverloadProtectionSimulationResponse,
            accept="application/vnd.atlas.2025-03-12+json",
        )
