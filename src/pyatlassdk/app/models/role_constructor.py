"""Generated model for RoleConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.expression import Expression
from pyatlassdk.app.models.field_level_permissions import FieldLevelPermissions
from pyatlassdk.app.models.nestable_field_level_permissions import NestableFieldLevelPermissions
from pyatlassdk.app.models.role_constructor_document_filters import RoleConstructorDocumentFilters

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RoleConstructor(BaseModel):
    """Document-level read and write permissions for Device Sync."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    document_filters: RoleConstructorDocumentFilters | None = None
    name: str | None = Field(default=None, description="The role's name.")
    apply_when: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` when this role applies to a user for a specific document.")
    read: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` if the role has permission to read all fields in the document. If Device Sync is enabled, use `document_filters.read` instead.")
    write: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` if the role has permission to add, modify, or remove all fields in the document. If Device Sync is enabled, use `document_filters.write` instead.")
    insert: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` if the role has permission to insert a new document into the collection.")
    delete: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` if the role has permission to delete a document from the collection.")
    search: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` if the role has permission to search the collection using [Atlas Search](https://www.mongodb.com/docs/atlas/atlas-search/).")
    fields: NestableFieldLevelPermissions | None = Field(default=None, description="Field-level rules for any fields that are not explicitly configured in the role's `properties`.")
    additional_fields: FieldLevelPermissions | None = Field(default=None, description="Field-level rules for any fields that are not explicitly configured in the role's `properties`.")
