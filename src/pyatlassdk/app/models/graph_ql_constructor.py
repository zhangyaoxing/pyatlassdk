"""Generated model for GraphQLConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.custom_resolver_constructor import CustomResolverConstructor
from pyatlassdk.app.models.graph_ql_config import GraphQLConfig
from pyatlassdk.app.models.graph_ql_validation_settings import GraphQLValidationSettings

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GraphQLConstructor(BaseModel):
    """Generated model for GraphQLConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    config: GraphQLConfig
    validation_settings: GraphQLValidationSettings
    custom_resolvers: list[CustomResolverConstructor]
