"""Generated resource for RollingIndex. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.database_rolling_index_request import DatabaseRollingIndexRequest

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class RollingIndex:
    """Creates one index to a database deployment in a rolling manner. Rolling indexes build indexes on the applicable nodes sequentially and may reduce the performance impact of an index build if your deployment's average CPU utilization exceeds (N-1)/N-10% where N is the number of CPU threads available to mongod of if the WiredTiger cache fill ratio regularly exceeds 90%. If your deployment does not meet this criteria, use the default index build. You can't create a rolling index on an `M0` free cluster or `M2/M5` shared cluster."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def create_group_cluster_index_rolling_index(
        self,
        cluster_name: str,
        group_id: str,
        body: DatabaseRollingIndexRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Create One Rolling Index

        Creates an index on the cluster identified by its name in a rolling manner. Creating the index in this way allows index builds on one replica set member as a standalone at a time, starting with the secondary members. Creating indexes in this way requires at least one replica set election.

        Args:
            cluster_name: Human-readable label that identifies the cluster on which MongoDB Cloud creates an index.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Rolling index to create on the specified cluster.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/index"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )
