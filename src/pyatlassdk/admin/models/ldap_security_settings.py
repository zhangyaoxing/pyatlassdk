"""Generated model for LDAPSecuritySettings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link
from pyatlassdk.admin.models.user_to_dn_mapping import UserToDNMapping

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LDAPSecuritySettings(BaseModel):
    """Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration details that apply to the specified project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    authentication_enabled: bool | None = Field(default=None, alias="authenticationEnabled", description="Flag that indicates whether users can authenticate using an Lightweight Directory Access Protocol (LDAP) host.")
    authorization_enabled: bool | None = Field(default=None, alias="authorizationEnabled", description="Flag that indicates whether users can authorize access to MongoDB Cloud resources using an Lightweight Directory Access Protocol (LDAP) host.")
    authz_query_template: str | None = Field(default=None, alias="authzQueryTemplate", description="Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud runs to obtain the LDAP groups associated with the authenticated user. MongoDB Cloud uses this parameter only for user authorization. Use the `{USER}` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query according to [RFC 4515](https://datatracker.ietf.org/doc/html/rfc4515) and [RFC 4516](https://datatracker.ietf.org/doc/html/rfc4516).")
    bind_password: str | None = Field(default=None, alias="bindPassword", description="Password that MongoDB Cloud uses to authenticate the `bindUsername`.")
    bind_username: str | None = Field(default=None, alias="bindUsername", description="Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host. LDAP distinguished names must be formatted according to RFC 2253.")
    ca_certificate: str | None = Field(default=None, alias="caCertificate", description="Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host. MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: `\"caCertificate\": \"\"`.")
    hostname: str | None = Field(default=None, description="Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host. This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    port: int | None = Field(default=None, description="Port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.")
    user_to_dn_mapping: list[UserToDNMapping] | None = Field(default=None, alias="userToDNMapping", description="User-to-Distinguished Name (DN) map that MongoDB Cloud uses to transform a Lightweight Directory Access Protocol (LDAP) username into an LDAP DN.")
