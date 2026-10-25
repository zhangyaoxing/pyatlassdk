"""Generated model for UserToDNMapping. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UserToDNMapping(BaseModel):
    """User-to-Distinguished Name (DN) map that MongoDB Cloud uses to transform a Lightweight Directory Access Protocol (LDAP) username into an LDAP DN."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ldap_query: str | None = Field(default=None, alias="ldapQuery", description="Lightweight Directory Access Protocol (LDAP) query template that inserts the LDAP name that the regular expression matches into an LDAP query Uniform Resource Identifier (URI). The formatting for the query must conform to [RFC 4515](https://datatracker.ietf.org/doc/html/rfc4515) and [RFC 4516](https://datatracker.ietf.org/doc/html/rfc4516).")
    match: str = Field(description="Regular expression that MongoDB Cloud uses to match against the provided Lightweight Directory Access Protocol (LDAP) username. Each parenthesis-enclosed section represents a regular expression capture group that the substitution or `ldapQuery` template uses.")
    substitution: str | None = Field(default=None, description="Lightweight Directory Access Protocol (LDAP) Distinguished Name (DN) template that converts the LDAP username that matches regular expression in the *match* parameter into an LDAP Distinguished Name (DN).")
