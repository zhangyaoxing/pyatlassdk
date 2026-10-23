"""Generated resource for AWSClustersDNS. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.aws_custom_dns_enabled_view import AWSCustomDNSEnabledView

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class AWSClustersDNS:
    """Returns and edits custom DNS configurations for MongoDB Cloud database deployments on AWS. The resource requires your Project ID. If you use the VPC peering on AWS and you use your own DNS servers instead of Amazon Route 53, enable custom DNS. Before 31 March 2020, applications deployed within AWS using custom DNS services and VPC-peered with MongoDB Cloud couldn't connect over private IP addresses. Custom DNS resolved to public IP addresses. AWS internal DNS resolved to private IP addresses. Applications deployed with custom DNS services in AWS should use Private IP for Peering connection strings."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_group_aws_custom_dns(
        self,
        group_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AWSCustomDNSEnabledView:
        """
        Return One Custom DNS Configuration for Atlas Clusters on AWS

        Returns the custom DNS configuration for AWS clusters in the specified project.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/awsCustomDNS"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=AWSCustomDNSEnabledView,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def toggle_group_aws_custom_dns(
        self,
        group_id: str,
        body: AWSCustomDNSEnabledView,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> AWSCustomDNSEnabledView:
        """
        Update State of One Custom DNS Configuration for Atlas Clusters on AWS

        Enables or disables the custom DNS configuration for AWS clusters in the specified project. Enable custom DNS if you use AWS VPC peering and use your own DNS servers.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: Enables or disables the custom DNS configuration for AWS clusters in the specified project.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/awsCustomDNS"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=AWSCustomDNSEnabledView,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )
