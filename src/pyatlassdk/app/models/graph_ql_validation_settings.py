"""Generated model for GraphQLValidationSettings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.graph_ql_validation_action import GraphQLValidationAction
from pyatlassdk.app.models.graph_ql_validation_level import GraphQLValidationLevel

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GraphQLValidationSettings(BaseModel):
    """Generated model for GraphQLValidationSettings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    read_validation_action: GraphQLValidationAction | None = None
    read_validation_level: GraphQLValidationLevel | None = None
    write_validation_action: GraphQLValidationAction | None = None
    write_validation_level: GraphQLValidationLevel | None = None
