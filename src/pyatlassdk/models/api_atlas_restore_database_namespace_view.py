"""Generated model for ApiAtlasRestoreDatabaseNamespaceView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasRestoreDatabaseNamespaceView(BaseModel):
    """Source and optional target database for a restore."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    source_namespace: str = Field(alias="sourceNamespace", description="Database name requested to restore.")
    target_namespace: str | None = Field(default=None, alias="targetNamespace", description="Requested target database name; if empty, source database name is used.")
