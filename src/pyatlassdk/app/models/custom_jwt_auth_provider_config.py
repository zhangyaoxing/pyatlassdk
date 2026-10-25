"""Generated model for CustomJwtAuthProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomJwtAuthProviderConfig(BaseModel):
    """Generated model for CustomJwtAuthProviderConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    audience: list[str] | None = Field(default=None, description="Defines the expected values of the `aud` claim in the\nexternal JWT. By default, the Custom JWT provider\nexpects `aud` to be your App ID.")
    require_any_audience: str | None = Field(default=None, alias="requireAnyAudience", description="If `false`, the external JWT must include *all* of\nthe values defined in `audience` in its `aud` claim.\n\nIf `true`, a JWT is valid if *any* of the values\ndefined in `audience` are in its `aud` claim.")
    signing_algorithm: str | None = Field(default=None, alias="signingAlgorithm", description="The cryptographic method that the external system\nuses to sign the JWT. Custom JWT authentication supports\nJWTs signed using any of the following algorithms:\n\n- HS256\n- RS256")
    use_jwkuri: bool | None = Field(default=None, alias="useJWKURI", description="If `true`, the Custom JWT provider uses a signing\nalgorithm and signing keys defined in a [JSON Web\nKey](https://www.rfc-editor.org/rfc/rfc7517) (JWK)\nor JSON Web Key Set (JWKS). The JWK(S) must be\naccessible at the URL specified in `jwkURI`.")
    jwk_uri: str | None = Field(default=None, alias="jwkURI", description="A URL that hosts a JWK or JWKS that describes the\nsigning method and signing keys the Custom JWT provider\nshould use. The JWK(S) may specify up to three signing\nkeys and must use the RS256 algorithm.")
