"""Generated resource for Deploy. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.app_deployment_settings import AppDeploymentSettings
from pyatlassdk.app.models.cloud_provider_region import CloudProviderRegion
from pyatlassdk.app.models.deployment import Deployment
from pyatlassdk.app.models.deployment_config import DeploymentConfig
from pyatlassdk.app.models.deployment_draft import DeploymentDraft
from pyatlassdk.app.models.deployment_migration import DeploymentMigration
from pyatlassdk.app.models.diff import Diff

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Deploy:
    """
    ## Draft and Deploy a Group of Changes

    You can [deploy](https://www.mongodb.com/docs/atlas/app-services/apps/deploy/) a
    group of application changes together by creating and deploying a draft.
    To create and deploy a set of draft changes:

    ### 1. Create a New Draft

    A draft represents a group of application changes that you can deploy or
    discard as a single unit. To create a draft, send a `POST` request to
    the drafts endpoint:

    ```shell
    curl --request POST \\
      --header 'Content-Type: application/json' \\
      --header 'Authorization: Bearer <access_token>' \\
      'https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/drafts'
    ```


    #### One Draft Per User

    Each user can only create a single draft at a time, either through the
    UI or the Admin API. If you already have an existing draft, you can
    discard the changes associated with it by sending a `DELETE` request to
    the draft's endpoint:

    ```shell
    curl --request DELETE \\
      --header 'Authorization: Bearer <access_token>' \\
      'https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/drafts/{draftId}'
    ```

    ### 2. Make Changes to Your Application

    Once you've created a draft, make all of the changes that you want to
    include in the draft. App Services adds any application changes that you make
    to the draft so that you can deploy them together.

    ### 3. Deploy the Draft

    After you've made all the changes that you want to include in the
    deployment, deploy the draft by sending a `POST` request to that draft's
    deployment endpoint:

    ```shell
    curl --request POST \\
      --header 'Content-Type: application/json' \\
      --header 'Authorization: Bearer <access_token>' \\
      'https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/drafts/{draftId}/deployment'
    ```

    #### Draft Conflicts

    If you deploy changes through the API but have conflicting changes in a
    draft in the UI, your UI draft will become invalid and you will not be
    able to deploy it. You can download your UI draft by reviewing the draft
    in the `Deployment` page. You can use the download to deploy your
    changes in the `appservices` CLI or as a reference as you reapply changes in
    the UI.
    """

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_deployment_config(
        self,
        app_id: str,
        group_id: str,
    ) -> DeploymentConfig:
        """
        Get the Deployment Configuration

        See information about how your App deploys changes.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deploy/config"
        return self._client.request(
            method="GET",
            path=path,
            response_model=DeploymentConfig,
        )

    def admin_configure_deployment(
        self,
        app_id: str,
        group_id: str,
        *,
        body: DeploymentConfig | None = None,
    ) -> None:
        """
        Configure Deployment

        Modify an App's deployment configuration to customize how the App deploys changes.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deploy/config"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_get_deployment_migration(
        self,
        app_id: str,
        group_id: str,
    ) -> DeploymentMigration:
        """
        Get a Deployment Migration

        Get metadata and status for the current deployment migration, if one exists.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deployment_migration"
        return self._client.request(
            method="GET",
            path=path,
            response_model=DeploymentMigration,
        )

    def admin_create_deployment_migration(
        self,
        app_id: str,
        group_id: str,
        body: AppDeploymentSettings,
    ) -> None:
        """
        Create a Deployment Migration

        Start a new deployment migration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The deployment model and cloud provider region that the App should migrate to.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deployment_migration"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_list_deployments(
        self,
        app_id: str,
        group_id: str,
    ) -> list[Deployment]:
        """
        List recent deployments

        Return the 25 most recent application deployments.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deployments"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[Deployment],
        )

    def admin_get_deployment(
        self,
        app_id: str,
        deployment_id: str,
        group_id: str,
    ) -> Deployment:
        """
        Get a deployment

        Get information about a recent deployment of the application.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            deployment_id: The `_id` value of an application deployment.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deployments/{quote(str(deployment_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Deployment,
        )

    def admin_redeploy_deployment(
        self,
        app_id: str,
        deployment_id: str,
        group_id: str,
    ) -> None:
        """
        Redeploy a Deployment

        Redeploy a previously-deployed version of an App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            deployment_id: The `_id` value of an application deployment.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/deployments/{quote(str(deployment_id), safe='')}/redeploy"
        return self._client.request(
            method="POST",
            path=path,
            response_model=None,
        )

    def admin_list_deployment_drafts(
        self,
        app_id: str,
        group_id: str,
    ) -> DeploymentDraft:
        """
        Get Current Deployment Draft

        Return the current application deployment draft, if applicable.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/drafts"
        return self._client.request(
            method="GET",
            path=path,
            response_model=DeploymentDraft,
        )

    def admin_create_deployment_draft(
        self,
        app_id: str,
        group_id: str,
    ) -> DeploymentDraft:
        """
        Create a Deployment Draft

        Create a new application deployment draft, if none exists.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/drafts"
        return self._client.request(
            method="POST",
            path=path,
            response_model=DeploymentDraft,
        )

    def admin_discard_draft(
        self,
        app_id: str,
        draft_id: str,
        group_id: str,
    ) -> None:
        """
        Discard the specified deployment draft

        Discard the specified application deployment draft.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            draft_id: The unique `_id` value of a draft.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/drafts/{quote(str(draft_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_deploy_draft(
        self,
        app_id: str,
        draft_id: str,
        group_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> Deployment:
        """
        Deploy a deployment draft

        Deploy the specified application deployment draft.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            draft_id: The unique `_id` value of a draft.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/drafts/{quote(str(draft_id), safe='')}/deployment"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=Deployment,
            content_type="application/json",
        )

    def admin_deploy_draft_diff(
        self,
        app_id: str,
        draft_id: str,
        group_id: str,
    ) -> Diff:
        """
        Diff a draft with the current deployment

        Return a diff between the currently deployed application and the
        specified draft.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            draft_id: The unique `_id` value of a draft.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/drafts/{quote(str(draft_id), safe='')}/diff"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Diff,
        )

    def admin_list_app_regions(
        self,
    ) -> list[CloudProviderRegion]:
        """
        List all available Atlas App cloud regions

        Return a list of all supported cloud regions in which you can
        deploy an Atlas App.
        """
        path = "/provider_regions"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[CloudProviderRegion],
        )
