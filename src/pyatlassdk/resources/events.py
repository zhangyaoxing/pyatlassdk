"""Generated resource for Events. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime
from urllib.parse import quote
from pyatlassdk.models.event_type_for_nds_group import EventTypeForNdsGroup
from pyatlassdk.models.event_type_for_org import EventTypeForOrg
from pyatlassdk.models.event_view_for_nds_group import EventViewForNdsGroup
from pyatlassdk.models.event_view_for_org import EventViewForOrg
from pyatlassdk.models.group_paginated_event_view import GroupPaginatedEventView
from pyatlassdk.models.org_paginated_event_view import OrgPaginatedEventView
from pyatlassdk.models.paginated_event_type_details_response import PaginatedEventTypeDetailsResponse

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class Events:
    """Returns events. This collection remains under revision and may change."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def list_event_types(
        self,
        *,
        envelope: bool | None = None,
        include_count: bool | None = None,
        items_per_page: int | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> PaginatedEventTypeDetailsResponse:
        """
        Return All Event Types

        Returns a list of all event types, along with a description and additional metadata about each event.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            items_per_page: Number of items that the response returns per page.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/eventTypes"
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
            response_model=PaginatedEventTypeDetailsResponse,
        )

    def list_group_events(
        self,
        group_id: str,
        *,
        cluster_names: list[str] | None = None,
        envelope: bool | None = None,
        event_type: list[EventTypeForNdsGroup] | None = None,
        excluded_event_type: list[EventTypeForNdsGroup] | None = None,
        include_count: bool | None = None,
        include_raw: bool | None = None,
        items_per_page: int | None = None,
        max_date: datetime | None = None,
        min_date: datetime | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> GroupPaginatedEventView:
        """
        Return Events from One Project

        Returns events for the specified project. Events identify significant database, billing, or security activities or status changes.

        This resource remains under revision and may change.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            cluster_names: Human-readable label that identifies the cluster.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            event_type: Category of incident recorded at this moment in time. **IMPORTANT**: The complete list of event type values changes frequently.
            excluded_event_type: Category of event that you would like to exclude from query results, such as `CLUSTER_CREATED`. **IMPORTANT**: Event type names change frequently. Verify that you specify the event type correctly by checking the complete list of event types.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            include_raw: Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
            items_per_page: Number of items that the response returns per page.
            max_date: Date and time from when MongoDB Cloud stops returning events. This parameter uses the ISO 8601 timestamp format in UTC.
            min_date: Date and time from when MongoDB Cloud starts returning events. This parameter uses the ISO 8601 timestamp format in UTC.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/events"
        params = {
            "clusterNames": cluster_names,
            "envelope": envelope,
            "eventType": event_type,
            "excludedEventType": excluded_event_type,
            "includeCount": include_count,
            "includeRaw": include_raw,
            "itemsPerPage": items_per_page,
            "maxDate": max_date,
            "minDate": min_date,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=GroupPaginatedEventView,
        )

    def get_group_event(
        self,
        event_id: str,
        group_id: str,
        *,
        envelope: bool | None = None,
        include_raw: bool | None = None,
        pretty: bool | None = None,
    ) -> EventViewForNdsGroup:
        """
        Return One Event from One Project

        Returns one event for the specified project. Events identify significant database, billing, or security activities or status changes. Use the Return Events from One Project endpoint to retrieve all events to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            event_id: Unique 24-hexadecimal digit string that identifies the event that you want to return.
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_raw: Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/events/{quote(str(event_id), safe='')}"
        params = {
            "envelope": envelope,
            "includeRaw": include_raw,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EventViewForNdsGroup,
        )

    def list_org_events(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        event_type: list[EventTypeForOrg] | None = None,
        include_count: bool | None = None,
        include_raw: bool | None = None,
        items_per_page: int | None = None,
        max_date: datetime | None = None,
        min_date: datetime | None = None,
        page_num: int | None = None,
        pretty: bool | None = None,
    ) -> OrgPaginatedEventView:
        """
        Return Events from One Organization

        Returns events for the specified organization. Events identify significant database, billing, or security activities or status changes. 

        This resource remains under revision and may change.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            event_type: Category of incident recorded at this moment in time. **IMPORTANT**: The complete list of event type values changes frequently.
            include_count: Flag that indicates whether MongoDB Cloud calculates the total number of items for the response. When set to `false`, MongoDB Cloud may skip an additional count operation. The response may still include `totalCount` when the count is available without additional calculation.
            include_raw: Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
            items_per_page: Number of items that the response returns per page.
            max_date: Date and time from when MongoDB Cloud stops returning events. This parameter uses the ISO 8601 timestamp format in UTC.
            min_date: Date and time from when MongoDB Cloud starts returning events. This parameter uses the ISO 8601 timestamp format in UTC.
            page_num: Number of the page that displays the current set of the total objects that the response returns.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/events"
        params = {
            "envelope": envelope,
            "eventType": event_type,
            "includeCount": include_count,
            "includeRaw": include_raw,
            "itemsPerPage": items_per_page,
            "maxDate": max_date,
            "minDate": min_date,
            "pageNum": page_num,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=OrgPaginatedEventView,
        )

    def get_org_event(
        self,
        event_id: str,
        org_id: str,
        *,
        envelope: bool | None = None,
        include_raw: bool | None = None,
        pretty: bool | None = None,
    ) -> EventViewForOrg:
        """
        Return One Event from One Organization

        Returns one event for the specified organization. Events identify significant database, billing, or security activities or status changes. Use the Return Events from One Organization endpoint to retrieve all events to which the authenticated user has access.

        This resource remains under revision and may change.

        Args:
            event_id: Unique 24-hexadecimal digit string that identifies the event that you want to return.
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            include_raw: Flag that indicates whether to include the raw document in the output. The raw document contains additional meta information about the event.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/events/{quote(str(event_id), safe='')}"
        params = {
            "envelope": envelope,
            "includeRaw": include_raw,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=EventViewForOrg,
        )
