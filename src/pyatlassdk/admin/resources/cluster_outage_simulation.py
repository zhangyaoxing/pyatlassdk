"""Generated resource for ClusterOutageSimulationResource. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.admin.models.cluster_outage_simulation import ClusterOutageSimulation

if TYPE_CHECKING:
    from pyatlassdk.admin.client import AtlasAdminClient


class ClusterOutageSimulationResource:
    """Returns, starts, or ends a cluster outage simulation."""

    def __init__(self, client: AtlasAdminClient) -> None:
        self._client = client

    def end_group_cluster_outage_simulation(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterOutageSimulation:
        """
        End One Outage Simulation

        Ends a cluster outage simulation.

        Args:
            cluster_name: Human-readable label that identifies the cluster that is undergoing outage simulation.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/outageSimulation"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=ClusterOutageSimulation,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_cluster_outage_simulation(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterOutageSimulation:
        """
        Return One Outage Simulation

        Returns one outage simulation for one cluster.

        Args:
            cluster_name: Human-readable label that identifies the cluster that is undergoing outage simulation.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/outageSimulation"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ClusterOutageSimulation,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def start_group_cluster_outage_simulation(
        self,
        cluster_name: str,
        group_id: str,
        body: ClusterOutageSimulation,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterOutageSimulation:
        """
        Start One Outage Simulation

        Starts a cluster outage simulation.

        Args:
            cluster_name: Human-readable label that identifies the cluster to undergo an outage simulation.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Describes the outage simulation.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/outageSimulation"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ClusterOutageSimulation,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )
