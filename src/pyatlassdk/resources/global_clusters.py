"""Generated resource for GlobalClusters. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.custom_zone_mappings import CustomZoneMappings
from pyatlassdk.models.geo_sharding20240805 import GeoSharding20240805
from pyatlassdk.models.managed_namespaces import ManagedNamespaces

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class GlobalClusters:
    """
    Returns, adds, and removes Global Cluster managed namespaces and custom zone mappings. Each collection in a Global Cluster is associated with a managed namespace. When you create a managed namespace for a Global Cluster, MongoDB Cloud creates an empty collection for that namespace. Creating a managed namespace doesn't populate a collection with data. Similarly, deleting a managed namespace doesn't delete the associated collection.
    MongoDB Cloud shards the empty collection using the required location field and a custom shard key. For example, if your custom shard key is `city`, the compound shard key is `location, city`. Each Global Cluster is also associated with one or more Global Writes Zones. When a user creates a Global Cluster, MongoDB Cloud automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. For example, a use case might require mapping a location code to a geographically distant zone. Administrators can manage custom zone mappings with the APIs below and the **Global Cluster Configuration** pane when you create or modify your Global Cluster.
    """

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_cluster_global_writes(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GeoSharding20240805:
        """
        Return One Managed Namespace in One Global Cluster

        Returns one managed namespace within the specified global cluster. A managed namespace identifies a collection using the database name, the dot separator, and the collection name. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/globalWrites"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GeoSharding20240805,
        )

    def delete_group_cluster_global_write_custom_zone_mapping(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GeoSharding20240805:
        """
        Remove All Custom Zone Mappings from One Global Cluster

        Removes all custom zone mappings for the specified global cluster. A custom zone mapping matches one ISO 3166-2 location code to a zone in your global cluster. Removing the custom zone mappings restores the default mapping. By default, MongoDB Cloud maps each location code to the closest geographical zone. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/globalWrites/customZoneMapping"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=GeoSharding20240805,
        )

    def create_group_cluster_global_write_custom_zone_mapping(
        self,
        cluster_name: str,
        group_id: str,
        body: CustomZoneMappings,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GeoSharding20240805:
        """
        Add One Custom Zone Mapping to One Global Cluster

        Creates one custom zone mapping for the specified global cluster. A custom zone mapping matches one ISO 3166-2 location code to a zone in your global cluster. By default, MongoDB Cloud maps each location code to the closest geographical zone. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Custom zone mapping to add to the specified global cluster.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/globalWrites/customZoneMapping"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GeoSharding20240805,
        )

    def delete_group_cluster_global_write_managed_namespaces(
        self,
        cluster_name: str,
        group_id: str,
        *,
        collection: str | None = None,
        db: str | None = None,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GeoSharding20240805:
        """
        Remove One Managed Namespace from One Global Cluster

        Removes one managed namespace within the specified global cluster. A managed namespace identifies a collection using the database name, the dot separator, and the collection name. Deleting a managed namespace does not remove the associated collection or data. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            collection: Human-readable label that identifies the collection associated with the managed namespace.
            db: Human-readable label that identifies the database that contains the collection.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/globalWrites/managedNamespaces"
        params = {
            "collection": collection,
            "db": db,
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=GeoSharding20240805,
        )

    def create_group_cluster_global_write_managed_namespace(
        self,
        cluster_name: str,
        group_id: str,
        body: ManagedNamespaces,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> GeoSharding20240805:
        """
        Create One Managed Namespace in One Global Cluster

        Creates one managed namespace within the specified global cluster. A managed namespace identifies a collection using the database name, the dot separator, and the collection name. Deprecated versions: v2-{2023-02-01}, v2-{2023-01-01}

        Args:
            cluster_name: Human-readable label that identifies this cluster.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Managed namespace to create within the specified global cluster.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/globalWrites/managedNamespaces"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=GeoSharding20240805,
        )
