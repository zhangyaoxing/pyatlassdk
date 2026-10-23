"""Generated resource for AtlasSearch. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.api_search_deployment_request_view import ApiSearchDeploymentRequestView
from pyatlassdk.models.api_search_deployment_response_view import ApiSearchDeploymentResponseView
from pyatlassdk.models.cluster_search_index import ClusterSearchIndex
from pyatlassdk.models.search_index_create_request import SearchIndexCreateRequest
from pyatlassdk.models.search_index_response import SearchIndexResponse
from pyatlassdk.models.search_index_update_request import SearchIndexUpdateRequest

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class AtlasSearch:
    """Returns, adds, edits, and removes Atlas Search indexes for the specified cluster. Also returns and updates user-defined analyzers for the specified cluster."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def create_group_cluster_fts_index(
        self,
        cluster_name: str,
        group_id: str,
        body: ClusterSearchIndex,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterSearchIndex:
        """
        Create One Atlas Search Index

        Creates one Atlas Search index on the specified collection. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. Only clusters running MongoDB v4.2 or later can use Atlas Search.

        Args:
            cluster_name: Name of the cluster that contains the collection on which to create an Atlas Search index.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one Atlas Search index on the specified collection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/fts/indexes"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ClusterSearchIndex,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def list_group_cluster_fts_index(
        self,
        cluster_name: str,
        collection_name: str,
        database_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[ClusterSearchIndex]:
        """
        Return All Atlas Search Indexes for One Collection

        Returns all Atlas Search indexes on the specified collection. Atlas Search indexes contain the indexed fields and the analyzers used to create the indexes.

        Args:
            cluster_name: Name of the cluster that contains the collection with one or more Atlas Search indexes.
            collection_name: Name of the collection that contains one or more Atlas Search indexes.
            database_name: Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/fts/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[ClusterSearchIndex],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_cluster_fts_index(
        self,
        cluster_name: str,
        group_id: str,
        index_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Atlas Search Index

        Removes one Atlas Search index that you identified with its unique ID.

        Args:
            cluster_name: Name of the cluster that contains the database and collection with one or more Application Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_id: Unique 24-hexadecimal digit string that identifies the Atlas Search index. Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/fts/indexes/{quote(str(index_id), safe='')}"
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

    def get_group_cluster_fts_index(
        self,
        cluster_name: str,
        group_id: str,
        index_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterSearchIndex:
        """
        Return One Atlas Search Index

        Returns one Atlas Search index in the specified project. You identify this index using its unique ID. Atlas Search index contains the indexed fields and the analyzers used to create the index.

        Args:
            cluster_name: Name of the cluster that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_id: Unique 24-hexadecimal digit string that identifies the Application Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Application Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Application Search indexes.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/fts/indexes/{quote(str(index_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ClusterSearchIndex,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def update_group_cluster_fts_index(
        self,
        cluster_name: str,
        group_id: str,
        index_id: str,
        body: ClusterSearchIndex,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ClusterSearchIndex:
        """
        Update One Atlas Search Index

        Updates one Atlas Search index that you identified with its unique ID. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index.

        Args:
            cluster_name: Name of the cluster that contains the collection whose Atlas Search index to update.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_id: Unique 24-hexadecimal digit string that identifies the Atlas Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update on the Atlas Search index.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/fts/indexes/{quote(str(index_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ClusterSearchIndex,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )

    def delete_group_cluster_search_deployment(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Delete Search Nodes

        Deletes the Search Nodes for the specified cluster.

        Args:
            cluster_name: Label that identifies the cluster to delete.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/deployment"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def get_group_cluster_search_deployment(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiSearchDeploymentResponseView:
        """
        Return All Search Nodes

        Returns the Search Nodes for the specified cluster. Deprecated versions: v2-{2024-05-30}, v2-{2023-01-01}

        Args:
            cluster_name: Label that identifies the cluster to return the Search Nodes for.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/deployment"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ApiSearchDeploymentResponseView,
            accept="application/vnd.atlas.2025-03-12+json",
        )

    def update_group_cluster_search_deployment(
        self,
        cluster_name: str,
        group_id: str,
        body: ApiSearchDeploymentRequestView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiSearchDeploymentResponseView:
        """
        Update Search Nodes

        Updates the Search Nodes for the specified cluster. Deprecated versions: v2-{2023-01-01}

        Args:
            cluster_name: Label that identifies the cluster to update the Search Nodes for.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updates the Search Nodes for the specified cluster.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/deployment"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=ApiSearchDeploymentResponseView,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def create_group_cluster_search_deployment(
        self,
        cluster_name: str,
        group_id: str,
        body: ApiSearchDeploymentRequestView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> ApiSearchDeploymentResponseView:
        """
        Create Search Nodes

        Creates Search Nodes for the specified cluster.

        Args:
            cluster_name: Label that identifies the cluster to create Search Nodes for.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates Search Nodes for the specified cluster.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/deployment"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=ApiSearchDeploymentResponseView,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def list_group_cluster_search_indexes(
        self,
        cluster_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[SearchIndexResponse]:
        """
        Return All Atlas Search Indexes for One Cluster

        Returns all Atlas Search indexes on the specified cluster. Atlas Search indexes contain the indexed fields and the analyzers used to create the indexes.

        Args:
            cluster_name: Name of the cluster that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[SearchIndexResponse],
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def create_group_cluster_search_index(
        self,
        cluster_name: str,
        group_id: str,
        body: SearchIndexCreateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SearchIndexResponse:
        """
        Create One Atlas Search Index

        Creates one Atlas Search index on the specified collection. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index. Only clusters running MongoDB v4.2 or later can use Atlas Search.

        Args:
            cluster_name: Name of the cluster that contains the collection on which to create an Atlas Search index.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Creates one Atlas Search index on the specified collection.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=SearchIndexResponse,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def list_group_cluster_search_index(
        self,
        cluster_name: str,
        collection_name: str,
        database_name: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[SearchIndexResponse]:
        """
        Return All Atlas Search Indexes for One Collection

        Returns all Atlas Search indexes on the specified collection. Atlas Search indexes contain the indexed fields and the analyzers used to create the indexes.

        Args:
            cluster_name: Name of the cluster that contains the collection with one or more Atlas Search indexes.
            collection_name: Name of the collection that contains one or more Atlas Search indexes.
            database_name: Label that identifies the database that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[SearchIndexResponse],
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def delete_group_cluster_search_index_by_name(
        self,
        cluster_name: str,
        collection_name: str,
        database_name: str,
        group_id: str,
        index_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Atlas Search Index by Name

        Removes one Atlas Search index that you identified with its database, collection, and name. This deletion is eventually consistent.

        Args:
            cluster_name: Name of the cluster that contains the database and collection with one or more Application Search indexes.
            collection_name: Name of the collection that contains one or more Atlas Search indexes.
            database_name: Label that identifies the database that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_name: Name of the Atlas Search index to delete.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/{quote(str(index_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def get_group_cluster_search_index_by_name(
        self,
        cluster_name: str,
        collection_name: str,
        database_name: str,
        group_id: str,
        index_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SearchIndexResponse:
        """
        Return One Atlas Search Index by Name

        Returns one Atlas Search index in the specified project. You identify this index using its database, collection and name. Atlas Search index contains the indexed fields and the analyzers used to create the index.

        Args:
            cluster_name: Name of the cluster that contains the collection with one or more Atlas Search indexes.
            collection_name: Name of the collection that contains one or more Atlas Search indexes.
            database_name: Label that identifies the database that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_name: Name of the Atlas Search index to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/{quote(str(index_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=SearchIndexResponse,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def update_group_cluster_search_index_by_name(
        self,
        cluster_name: str,
        collection_name: str,
        database_name: str,
        group_id: str,
        index_name: str,
        body: SearchIndexUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SearchIndexResponse:
        """
        Update One Atlas Search Index by Name

        Updates one Atlas Search index that you identified with its database, collection name, and index name. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index.

        Args:
            cluster_name: Name of the cluster that contains the collection whose Atlas Search index you want to update.
            collection_name: Name of the collection that contains one or more Atlas Search indexes.
            database_name: Label that identifies the database that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_name: Name of the Atlas Search index to update.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update the Atlas Search index with.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(database_name), safe='')}/{quote(str(collection_name), safe='')}/{quote(str(index_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=SearchIndexResponse,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def delete_group_cluster_search_index(
        self,
        cluster_name: str,
        group_id: str,
        index_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Atlas Search Index by ID

        Removes one Atlas Search index that you identified with its unique ID. This deletion is eventually consistent.

        Args:
            cluster_name: Name of the cluster that contains the database and collection with one or more Application Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_id: Unique 24-hexadecimal digit string that identifies the Atlas Search index. Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(index_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def get_group_cluster_search_index(
        self,
        cluster_name: str,
        group_id: str,
        index_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SearchIndexResponse:
        """
        Return One Atlas Search Index by ID

        Returns one Atlas Search index in the specified project. You identify this index using its unique ID. Atlas Search index contains the indexed fields and the analyzers used to create the index.

        Args:
            cluster_name: Name of the cluster that contains the collection with one or more Atlas Search indexes.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_id: Unique 24-hexadecimal digit string that identifies the Application Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Application Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Application Search indexes.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(index_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=SearchIndexResponse,
            accept="application/vnd.atlas.2024-05-30+json",
        )

    def update_group_cluster_search_index(
        self,
        cluster_name: str,
        group_id: str,
        index_id: str,
        body: SearchIndexUpdateRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SearchIndexResponse:
        """
        Update One Atlas Search Index by ID

        Updates one Atlas Search index that you identified with its unique ID. Atlas Search indexes define the fields on which to create the index and the analyzers to use when creating the index.

        Args:
            cluster_name: Name of the cluster that contains the collection whose Atlas Search index you want to update.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            index_id: Unique 24-hexadecimal digit string that identifies the Atlas Search [index](https://dochub.mongodb.org/core/index-definitions-fts). Use the [Get All Atlas Search Indexes for a Collection API](https://docs.atlas.mongodb.com/reference/api/fts-indexes-get-all/) endpoint to find the IDs of all Atlas Search indexes.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Details to update on the Atlas Search index.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/clusters/{quote(str(cluster_name), safe='')}/search/indexes/{quote(str(index_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=SearchIndexResponse,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )
