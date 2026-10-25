"""Generated model for ApiAtlasRestoreCollectionNamespaceView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasRestoreCollectionNamespaceView(BaseModel):
    """Source and optional target collection for a restore."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    source_namespace: str = Field(alias="sourceNamespace", description="Collection requested to restore, as `database.collection`.")
    target_namespace: str | None = Field(default=None, alias="targetNamespace", description="Requested target collection as `database.collection`; if empty, source namespace is used.")
