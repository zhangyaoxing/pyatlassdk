"""Generated model for GraphQLConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GraphQLConfig(BaseModel):
    """Generated model for GraphQLConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    use_natural_pluralization: bool | None = Field(default=None, description="If `true`, generated schema type names use common English\npluralization whenever possible.\n\nIf `false`, or if a natural pluralization cannot be\ndetermined, then plural types use the singular type\nname with an `\"s\"` appended to the end.\n\n**You cannot change this value after you create your App.\nThis value is `true` for all new Apps.**")
    disable_schema_introspection: bool | None = Field(default=None, description="If `true`, the GraphQL API blocks [introspection queries](https://graphql.org/learn/introspection/) from clients.")
