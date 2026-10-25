"""Generated resource for Schemas. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.full_schema import FullSchema
from pyatlassdk.app.models.null_type_schema_validation_setting import NullTypeSchemaValidationSetting
from pyatlassdk.app.models.schema_metadata_instance import SchemaMetadataInstance

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Schemas:
    """View and manage your application's [schemas](https://www.mongodb.com/docs/atlas/app-services/schemas/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_schemas(
        self,
        app_id: str,
        group_id: str,
    ) -> list[SchemaMetadataInstance]:
        """
        List schemas

        List all defined [schemas](https://www.mongodb.com/docs/atlas/app-services/schemas).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/schemas"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[SchemaMetadataInstance],
        )

    def admin_create_schema(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> SchemaMetadataInstance:
        """
        Create a schema

        Define a new [schema](https://www.mongodb.com/docs/atlas/app-services/schemas) 
        for a linked collection. When creating a schema with this endpoint, 
        ensure that the JSON payload is completely unescaped. Incorrectly 
        escaped JSON formats can lead to errors.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/schemas"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=SchemaMetadataInstance,
            content_type="application/json",
        )

    def admin_delete_schema(
        self,
        app_id: str,
        group_id: str,
        schema_id: str,
    ) -> None:
        """
        Delete a schema

        Delete a specific [schema](https://www.mongodb.com/docs/atlas/app-services/schemas) by its `_id` value.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            schema_id: The unique `_id` value of a schema.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/schemas/{quote(str(schema_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_schema(
        self,
        app_id: str,
        group_id: str,
        schema_id: str,
    ) -> FullSchema:
        """
        Get a schema

        Get a specific [schema](https://www.mongodb.com/docs/atlas/app-services/schemas) by its `_id` value.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            schema_id: The unique `_id` value of a schema.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/schemas/{quote(str(schema_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=FullSchema,
        )

    def admin_update_schema(
        self,
        app_id: str,
        group_id: str,
        schema_id: str,
        body: FullSchema,
    ) -> None:
        """
        Update a schema

        Replace an existing [schema](https://www.mongodb.com/docs/atlas/app-services/schemas) with a new one.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            schema_id: The unique `_id` value of a schema.
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/schemas/{quote(str(schema_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_validate_documents(
        self,
        app_id: str,
        datasource_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Sample & Validate Documents

        Query a subset of documents in a collection and validate each match against a schema.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            datasource_id: The unique `_id` value of a MongoDB data source.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(datasource_id), safe='')}/commands/validate_documents"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_get_null_type_schema_validation_setting(
        self,
        app_id: str,
        group_id: str,
    ) -> NullTypeSchemaValidationSetting:
        """
        Get Null Type Schema Validation Setting

        Check if [null type schema validation](https://www.mongodb.com/docs/atlas/app-services/schemas/enforce-a-schema/#validate-null-types) is enabled.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/validation_settings/null_type_schema_validation"
        return self._client.request(
            method="GET",
            path=path,
            response_model=NullTypeSchemaValidationSetting,
        )

    def admin_set_null_type_schema_validation_setting(
        self,
        app_id: str,
        group_id: str,
        body: NullTypeSchemaValidationSetting,
    ) -> None:
        """
        Set Null Type Schema Validation Setting

        Enable or disable [null type schema validation](https://www.mongodb.com/docs/atlas/app-services/schemas/enforce-a-schema/#validate-null-types).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/validation_settings/null_type_schema_validation"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
