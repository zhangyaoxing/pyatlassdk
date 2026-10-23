"""Generated resource for DataFederation. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.data_federation_tenant_query_limit import DataFederationTenantQueryLimit
from pyatlassdk.models.data_lake_tenant import DataLakeTenant
from pyatlassdk.models.paginated_private_network_endpoint_id_entry_view import PaginatedPrivateNetworkEndpointIdEntryView
from pyatlassdk.models.private_network_endpoint_id_entry import PrivateNetworkEndpointIdEntry

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class DataFederation:
    """Returns, adds, edits, and removes Federated Database Instances. This resource requires your project ID. Changes to federated database instance configurations can affect costs."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_group_data_federation(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        type: Literal["USER", "ONLINE_ARCHIVE"] | None = None,
    ) -> list[DataLakeTenant]:
        """
        Return All Federated Database Instances in One Project

        Returns the details of all federated database instances in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            type: Type of Federated Database Instances to return.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "type": type,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[DataLakeTenant],
        )

    def create_group_data_federation(
        self,
        group_id: str,
        body: DataLakeTenant,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        skip_role_validation: bool | None = None,
    ) -> DataLakeTenant:
        """
        Create One Federated Database Instance in One Project

        Creates one federated database instance in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            skip_role_validation: Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket. AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.
            body: Details to create one federated database instance in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "skipRoleValidation": skip_role_validation,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=DataLakeTenant,
        )

    def delete_group_data_federation(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Federated Database Instance from One Project

        Removes one federated database instance from the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Human-readable label that identifies the federated database instance to remove.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}"
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

    def get_group_data_federation(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
    ) -> DataLakeTenant:
        """
        Return One Federated Database Instance in One Project

        Returns the details of one federated database instance within the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Human-readable label that identifies the Federated Database to return.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DataLakeTenant,
        )

    def update_group_data_federation(
        self,
        group_id: str,
        tenant_name: str,
        body: DataLakeTenant,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
        skip_role_validation: bool,
    ) -> DataLakeTenant:
        """
        Update One Federated Database Instance in One Project

        Updates the details of one federated database instance in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Human-readable label that identifies the federated database instance to update.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            skip_role_validation: Flag that indicates whether this request should check if the requesting IAM role can read from the S3 bucket. AWS checks if the role can list the objects in the bucket before writing to it. Some IAM roles only need write permissions. This flag allows you to skip that check.
            body: Details of one Federated Database to update in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
            "skipRoleValidation": skip_role_validation,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=DataLakeTenant,
        )

    def list_group_data_federation_limits(
        self,
        group_id: str,
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[DataFederationTenantQueryLimit]:
        """
        Return All Query Limits for One Federated Database Instance

        Returns query limits for a federated databases instance in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Human-readable label that identifies the federated database instance for which you want to retrieve query limits.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}/limits"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[DataFederationTenantQueryLimit],
        )

    def delete_group_data_federation_limit(
        self,
        group_id: str,
        limit_name: Literal["bytesProcessed.query", "bytesProcessed.daily", "bytesProcessed.weekly", "bytesProcessed.monthly"],
        tenant_name: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Delete One Query Limit for One Federated Database Instance

        Deletes one query limit for one federated database instance.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            limit_name: Human-readable label that identifies this data federation instance limit. | Limit Name | Description | Default | | --- | --- | --- | | `bytesProcessed.query` | Limit on the number of bytes processed during a single data federation query | N/A | | `bytesProcessed.daily` | Limit on the number of bytes processed for the data federation instance for the current day | N/A | | `bytesProcessed.weekly` | Limit on the number of bytes processed for the data federation instance for the current week | N/A | | `bytesProcessed.monthly` | Limit on the number of bytes processed for the data federation instance for the current month | N/A |
            tenant_name: Human-readable label that identifies the federated database instance to which the query limit applies.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}/limits/{quote(str(limit_name), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
        )

    def get_group_data_federation_limit(
        self,
        group_id: str,
        limit_name: Literal["bytesProcessed.query", "bytesProcessed.daily", "bytesProcessed.weekly", "bytesProcessed.monthly"],
        tenant_name: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> DataFederationTenantQueryLimit:
        """
        Return One Federated Database Instance Query Limit for One Project

        Returns the details of one query limit for the specified federated database instance in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            limit_name: Human-readable label that identifies this data federation instance limit. | Limit Name | Description | Default | | --- | --- | --- | | `bytesProcessed.query` | Limit on the number of bytes processed during a single data federation query | N/A | | `bytesProcessed.daily` | Limit on the number of bytes processed for the data federation instance for the current day | N/A | | `bytesProcessed.weekly` | Limit on the number of bytes processed for the data federation instance for the current week | N/A | | `bytesProcessed.monthly` | Limit on the number of bytes processed for the data federation instance for the current month | N/A |
            tenant_name: Human-readable label that identifies the federated database instance to which the query limit applies.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}/limits/{quote(str(limit_name), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=DataFederationTenantQueryLimit,
        )

    def set_group_data_federation_limit(
        self,
        group_id: str,
        limit_name: Literal["bytesProcessed.query", "bytesProcessed.daily", "bytesProcessed.weekly", "bytesProcessed.monthly"],
        tenant_name: str,
        body: DataFederationTenantQueryLimit,
        *,
        envelope: bool | None = None,
    ) -> DataFederationTenantQueryLimit:
        """
        Configure One Query Limit for One Federated Database Instance

        Creates or updates one query limit for one federated database instance.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            limit_name: Human-readable label that identifies this data federation instance limit. | Limit Name | Description | Default | | --- | --- | --- | | `bytesProcessed.query` | Limit on the number of bytes processed during a single data federation query | N/A | | `bytesProcessed.daily` | Limit on the number of bytes processed for the data federation instance for the current day | N/A | | `bytesProcessed.weekly` | Limit on the number of bytes processed for the data federation instance for the current week | N/A | | `bytesProcessed.monthly` | Limit on the number of bytes processed for the data federation instance for the current month | N/A |
            tenant_name: Human-readable label that identifies the federated database instance to which the query limit applies.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            body: Creates or updates one query limit for one federated database instance.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}/limits/{quote(str(limit_name), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=DataFederationTenantQueryLimit,
        )

    def download_group_data_federation_query_logs(
        self,
        group_id: str,
        tenant_name: str,
        *,
        end_date: int | None = None,
        start_date: int | None = None,
    ) -> str:
        """
        Download Query Logs for One Federated Database Instance

        Downloads the query logs for the specified federated database instance. The API does not support direct calls with the json response schema. You must request a gzip response schema using an accept header of the format: `Accept: application/vnd.atlas.YYYY-MM-DD+gzip`.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            tenant_name: Human-readable label that identifies the federated database instance for which you want to download query logs.
            end_date: Timestamp that specifies the end point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
            start_date: Timestamp that specifies the starting point for the range of log messages to download. MongoDB Cloud expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/dataFederation/{quote(str(tenant_name), safe='')}/queryLogs.gz"
        params = {
            "endDate": end_date,
            "startDate": start_date,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=str,
        )

    def list_group_private_network_setting_endpoint_ids(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedPrivateNetworkEndpointIdEntryView:
        """
        Return All Federated Database Instance and Online Archive Private Endpoints in One Project

        Returns all private endpoints for Federated Database Instances and Online Archives in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateNetworkSettings/endpointIds"
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
            response_model=PaginatedPrivateNetworkEndpointIdEntryView,
        )

    def create_group_private_network_setting_endpoint_id(
        self,
        group_id: str,
        body: PrivateNetworkEndpointIdEntry,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PaginatedPrivateNetworkEndpointIdEntryView:
        """
        Create One Federated Database Instance and Online Archive Private Endpoint for One Project

        Adds one private endpoint for Federated Database Instances and Online Archives to the specified projects. If the endpoint ID already exists and the associated comment is unchanged, Atlas Data Federation makes no change to the endpoint ID list. If the endpoint ID already exists and the associated comment is changed, Atlas Data Federation updates the comment value only in the endpoint ID list. If the endpoint ID doesn't exist, Atlas Data Federation appends the new endpoint to the list of endpoints in the endpoint ID list. Each region has an associated service name for the various endpoints. For the latest list of supported regions and their service names, see the external documentation.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Private endpoint for Federated Database Instances and Online Archives to add to the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateNetworkSettings/endpointIds"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=PaginatedPrivateNetworkEndpointIdEntryView,
        )

    def delete_group_private_network_setting_endpoint_id(
        self,
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Remove One Federated Database Instance and Online Archive Private Endpoint from One Project

        Removes one private endpoint for Federated Database Instances and Online Archives in the specified project.

        Args:
            endpoint_id: Unique 22-character alphanumeric string that identifies the private endpoint to remove. Atlas Data Federation supports AWS private endpoints using the AWS PrivateLink feature.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateNetworkSettings/endpointIds/{quote(str(endpoint_id), safe='')}"
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

    def get_group_private_network_setting_endpoint_id(
        self,
        endpoint_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> PrivateNetworkEndpointIdEntry:
        """
        Return One Federated Database Instance and Online Archive Private Endpoint in One Project

        Returns the specified private endpoint for Federated Database Instances or Online Archives in the specified project.

        Args:
            endpoint_id: Unique 22-character alphanumeric string that identifies the private endpoint to return. Atlas Data Federation supports AWS private endpoints using the AWS PrivateLink feature.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/privateNetworkSettings/endpointIds/{quote(str(endpoint_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PrivateNetworkEndpointIdEntry,
        )
