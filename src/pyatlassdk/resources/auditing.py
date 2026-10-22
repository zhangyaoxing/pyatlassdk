"""Generated resource for Auditing. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.audit_log import AuditLog

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class Auditing:
    """Returns and edits database auditing settings for MongoDB Cloud projects."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_audit_log(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AuditLog:
        """
        Return Auditing Configuration for One Project

        Returns the auditing configuration for the specified project. The auditing configuration defines the events that MongoDB Cloud records in the audit log. This feature isn't available for `M0`, `M2`, `M5`, or serverless clusters.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/auditLog"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AuditLog,
        )

    def update_group_audit_log(
        self,
        group_id: str,
        body: AuditLog,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AuditLog:
        """
        Update Auditing Configuration for One Project

        Updates the auditing configuration for the specified project. The auditing configuration defines the events that MongoDB Cloud records in the audit log. This feature isn't available for `M0`, `M2`, `M5`, or serverless clusters.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Updated auditing configuration for the specified project.
        """
        path = f"/api/atlas/v2/groups/{quote(str(group_id), safe='')}/auditLog"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AuditLog,
        )
