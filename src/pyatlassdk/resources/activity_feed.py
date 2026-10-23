"""Generated resource for ActivityFeed. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from datetime import datetime
from urllib.parse import quote
from pyatlassdk.models.activity_feed_link_response import ActivityFeedLinkResponse
from pyatlassdk.models.event_type_for_nds_group import EventTypeForNdsGroup
from pyatlassdk.models.event_type_for_org import EventTypeForOrg

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class ActivityFeed:
    """Returns pre-filtered activity feed links for projects and organizations. The returned links can be shared and opened to view the activity feed with the specified filters applied."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_activity_feed(
        self,
        group_id: str,
        *,
        cluster_name: list[str] | None = None,
        event_type: list[EventTypeForNdsGroup] | None = None,
        max_date: datetime | None = None,
        min_date: datetime | None = None,
        pretty: bool | None = None,
    ) -> ActivityFeedLinkResponse:
        """
        Return Pre-Filtered Activity Feed Link for One Project

        Returns a pre-filtered activity feed link for the specified project based on the provided date range and event types. The returned link can be shared and opened to view the activity feed with the same filters applied.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            cluster_name: Human-readable label that identifies the cluster.
            event_type: Category of incident recorded at this moment in time. **IMPORTANT**: The complete list of event type values changes frequently.
            max_date: End date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
            min_date: Start date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/activityFeed"
        params = {
            "clusterName": cluster_name,
            "eventType": event_type,
            "maxDate": max_date,
            "minDate": min_date,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ActivityFeedLinkResponse,
        )

    def get_org_activity_feed(
        self,
        org_id: str,
        *,
        event_type: list[EventTypeForOrg] | None = None,
        max_date: datetime | None = None,
        min_date: datetime | None = None,
        pretty: bool | None = None,
    ) -> ActivityFeedLinkResponse:
        """
        Return Pre-Filtered Activity Feed Link for One Organization

        Returns a pre-filtered activity feed link for the specified organization based on the provided date range and event types. The returned link can be shared and opened to view the activity feed with the same filters applied.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            event_type: Category of incident recorded at this moment in time. **IMPORTANT**: The complete list of event type values changes frequently.
            max_date: End date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
            min_date: Start date and time for events to include in the activity feed link. ISO 8601 timestamp format in UTC.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/activityFeed"
        params = {
            "eventType": event_type,
            "maxDate": max_date,
            "minDate": min_date,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ActivityFeedLinkResponse,
        )
