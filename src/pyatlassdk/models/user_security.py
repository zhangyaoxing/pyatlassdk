"""Generated model for UserSecurity. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.db_user_tlsx509_settings import DBUserTLSX509Settings
from pyatlassdk.models.ldap_security_settings import LDAPSecuritySettings
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class UserSecurity(BaseModel):
    """Generated model for UserSecurity."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    customer_x509: DBUserTLSX509Settings | None = Field(default=None, alias="customerX509")
    ldap: LDAPSecuritySettings | None = None
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
