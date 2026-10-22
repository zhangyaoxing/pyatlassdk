"""Generated model for DatabasePermittedNamespaceResource. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class DatabasePermittedNamespaceResource(BaseModel):
    """Namespace to which this database user has access."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster: bool = Field(description="Flag that indicates whether to grant the action on the cluster resource. If `true`, MongoDB Cloud ignores the `actions.resources.collection` and `actions.resources.db` parameters.")
    collection: str = Field(description="Human-readable label that identifies the collection on which you grant the action to one MongoDB user. If you don't set this parameter, you grant the action to all collections in the database specified in the `actions.resources.db` parameter. If you set `\"actions.resources.cluster\" : true`, MongoDB Cloud ignores this parameter.")
    db: str = Field(description="Human-readable label that identifies the database on which you grant the action to one MongoDB user. If you set `\"actions.resources.cluster\" : true`, MongoDB Cloud ignores this parameter.")
