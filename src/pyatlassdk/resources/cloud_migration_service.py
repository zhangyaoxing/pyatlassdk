"""Generated resource for CloudMigrationService. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.models.live_import_available_project import LiveImportAvailableProject
from pyatlassdk.models.live_import_validation import LiveImportValidation
from pyatlassdk.models.live_migration_request20240530 import LiveMigrationRequest20240530
from pyatlassdk.models.live_migration_response import LiveMigrationResponse
from pyatlassdk.models.target_org import TargetOrg
from pyatlassdk.models.target_org_request import TargetOrgRequest

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class CloudMigrationService:
    """Manages the Cloud Migration Service. Source organizations, projects, and MongoDB clusters reside on Cloud Manager or Ops Manager. Destination organizations, projects, and MongoDB clusters reside on MongoDB Cloud. Source databases can't use any authentication except SCRAM-SHA."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def create_group_live_migration(
        self,
        group_id: str,
        body: LiveMigrationRequest20240530,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LiveMigrationResponse:
        """
        Create One Migration for One Local Managed Cluster to MongoDB Atlas

        Migrate one cluster that Cloud or Ops Manager manages to MongoDB Atlas.

         Please make sure to validate your migration before initiating it.

         You can use this API endpoint for push live migrations only. Your API Key must have the Organization Owner role to successfully call this resource.

         **NOTE**: Migrating time-series collections is not yet supported on MongoDB 6.0 or higher. Migrations on MongoDB 6.0 or higher will skip any time-series collections on the source cluster. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: One migration to be created.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/liveMigrations"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=LiveMigrationResponse,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def validate_group_live_migrations(
        self,
        group_id: str,
        body: LiveMigrationRequest20240530,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LiveImportValidation:
        """
        Validate One Migration Request

        Verifies whether the provided credentials, available disk space, MongoDB versions, and so on meet the requirements of the migration request. If the check passes, the migration can proceed. Your API Key must have the Organization Owner role to successfully call this resource. Deprecated versions: v2-{2023-01-01}

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: One migration to be validated.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/liveMigrations/validate"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=LiveImportValidation,
            accept="application/vnd.atlas.2024-05-30+json",
            content_type="application/vnd.atlas.2024-05-30+json",
        )

    def get_group_live_migration_validate_status(
        self,
        group_id: str,
        validation_id: str,
        *,
        envelope: bool | None = None,
    ) -> LiveImportValidation:
        """
        Return One Migration Validation Job

        Return the status of one migration validation job. Your API Key must have the Organization Owner role to successfully call this resource.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            validation_id: Unique 24-hexadecimal digit string that identifies the validation job.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/liveMigrations/validate/{quote(str(validation_id), safe='')}"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=LiveImportValidation,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def get_group_live_migration(
        self,
        group_id: str,
        live_migration_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> LiveMigrationResponse:
        """
        Return One Migration Job

        Return details of one cluster migration job. Each push live migration job uses one migration host. Your API Key must have the Organization Member role to successfully call this resource.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            live_migration_id: Unique 24-hexadecimal digit string that identifies the migration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/liveMigrations/{quote(str(live_migration_id), safe='')}"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=LiveMigrationResponse,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def cutover_group_live_migration(
        self,
        group_id: str,
        live_migration_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> Any:
        """
        Cut Over One Migrated Cluster

        Cut over the migrated cluster to MongoDB Atlas. Confirm when the cut over completes. When the cut over completes, MongoDB Atlas completes the live migration process and stops synchronizing with the source cluster. Your API Key must have the Organization Owner role to successfully call this resource.

        Args:
            group_id: Unique 24-hexadecimal digit string that identifies your project. Use the [/groups](#tag/Projects/operation/listProjects) endpoint to retrieve all projects to which the authenticated user has access. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.
            live_migration_id: Unique 24-hexadecimal digit string that identifies the migration.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/liveMigrations/{quote(str(live_migration_id), safe='')}/cutover"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_org_live_migration_available_projects(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> list[LiveImportAvailableProject]:
        """
        Return All Projects Available for Migration

        Return all projects that you can migrate to the specified organization.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/liveMigrations/availableProjects"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[LiveImportAvailableProject],
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def delete_org_live_migration_link_tokens(
        self,
        org_id: str,
        *,
        envelope: bool | None = None,
    ) -> Any:
        """
        Remove One Link-Token

        Remove one organization link and its associated public API key. MongoDB Atlas uses the link-token for push live migrations only. Live migrations (push) let you securely push data from Cloud Manager or Ops Manager into MongoDB Atlas. Your API Key must have the Organization Owner role to successfully call this resource.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/liveMigrations/linkTokens"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="DELETE",
            path=path,
            params=params,
            response_model=Any,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def create_org_live_migration_link_token(
        self,
        org_id: str,
        body: TargetOrgRequest,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> TargetOrg:
        """
        Create One Link-Token

        Create one link-token that contains all the information required to complete the link. MongoDB Atlas uses the link-token for push live migrations only. Live migration (push) allows you to securely push data from Cloud Manager or Ops Manager into MongoDB Atlas. Your API Key must have the Organization Owner role to successfully call this resource.

        Args:
            org_id: Unique 24-hexadecimal digit string that identifies the organization that contains your projects. Use the [`/orgs`](#tag/Organizations/operation/listOrganizations) endpoint to retrieve all organizations to which the authenticated user has access.
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
            body: IP address access list entries associated with the migration.
        """
        path = f"/orgs/{quote(str(org_id), safe='')}/liveMigrations/linkTokens"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=TargetOrg,
            accept="application/vnd.atlas.2023-01-01+json",
            content_type="application/vnd.atlas.2023-01-01+json",
        )
