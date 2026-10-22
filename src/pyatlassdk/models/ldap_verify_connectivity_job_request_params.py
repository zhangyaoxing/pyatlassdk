"""Generated model for LDAPVerifyConnectivityJobRequestParams. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class LDAPVerifyConnectivityJobRequestParams(BaseModel):
    """Request information needed to verify an Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration. The response does not return the `bindPassword`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    authz_query_template: str | None = Field(default=None, alias="authzQueryTemplate", description="Lightweight Directory Access Protocol (LDAP) query template that MongoDB Cloud applies to create an LDAP query to return the LDAP groups associated with the authenticated MongoDB user. MongoDB Cloud uses this parameter only for user authorization.\n\nUse the `{USER}` placeholder in the Uniform Resource Locator (URL) to substitute the authenticated username. The query relates to the host specified with the hostname. Format this query per [RFC 4515](https://datatracker.ietf.org/doc/html/rfc4515) and [RFC 4516](https://datatracker.ietf.org/doc/html/rfc4516).")
    bind_password: str = Field(alias="bindPassword", description="Password that MongoDB Cloud uses to authenticate the `bindUsername`.")
    bind_username: str = Field(alias="bindUsername", description="Full Distinguished Name (DN) of the Lightweight Directory Access Protocol (LDAP) user that MongoDB Cloud uses to connect to the LDAP host. LDAP distinguished names must be formatted according to RFC 2253.")
    ca_certificate: str | None = Field(default=None, alias="caCertificate", description="Certificate Authority (CA) certificate that MongoDB Cloud uses to verify the identity of the Lightweight Directory Access Protocol (LDAP) host. MongoDB Cloud allows self-signed certificates. To delete an assigned value, pass an empty string: `\"caCertificate\": \"\"`.")
    hostname: str = Field(description="Human-readable label that identifies the hostname or Internet Protocol (IP) address of the Lightweight Directory Access Protocol (LDAP) host. This host must have access to the internet or have a Virtual Private Cloud (VPC) peering connection to your cluster.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    port: int = Field(description="IANA port to which the Lightweight Directory Access Protocol (LDAP) host listens for client connections.")
