"""Generated model for CustomResolverConstructor. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomResolverConstructor(BaseModel):
    """Generated model for CustomResolverConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    on_type: str = Field(description="The name of the resolver's parent type. This can be\n`\"Query\"`, `\"Mutation\"`, or the name of a generated type if\nthis is a computed property.")
    field_name: str = Field(description="The name of the custom resolver field that appears in the GraphQL schema.")
    input_type: str | dict[str, Any] | None = Field(default=None, description="The type of the custom resolver's `input` parameter. This\ncan be a scalar, the name of an existing generated type, or\na custom JSON schema object. If undefined, the resolver does\nnot accept an input.")
    input_type_format: Literal["scalar", "scalar-list", "generated", "generated-list", "custom"] | None = Field(default=None, description="The kind of input type the custom resolver uses. This value\nmust agree with the value of `input_type`:\n\n- A scalar input type must use `\"scalar\"` or `\"scalar-list\"`\n- A generated input type must use `\"generated\"` or `\"generated-list\"`\n- A custom input type must use `\"custom\"`\n\nIf undefined, the resolver does not accept an input.")
    payload_type: str | dict[str, Any] | None = Field(default=None, description="The type of the value returned by the custom resolver. This\ncan be a scalar, the name of an existing generated type, or\na custom JSON schema object.\n\nIf undefined, the resolver returns a `DefaultPayload`\nobject:\n\n```graphql\ntype DefaultPayload {\n  status: String!\n}\n```")
    payload_type_format: Literal["scalar", "scalar-list", "generated", "generated-list", "custom"] | None = Field(default=None, description="The kind of payload type the custom resolver uses. This value\nmust agree with the value of `payload_type`:\n\n- A scalar payload type must use `\"scalar\"` or `\"scalar-list\"`\n- A generated payload type must use `\"generated\"` or `\"generated-list\"`\n- A custom payload type must use `\"custom\"`\n\nIf undefined, the resolver returns a `DefaultPayload` object.")
    function_name: str = Field(description="The resolver function's name.")
