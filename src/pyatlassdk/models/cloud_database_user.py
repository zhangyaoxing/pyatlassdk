"""Generated model for CloudDatabaseUser. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.component_label import ComponentLabel
from pyatlassdk.models.database_user_role import DatabaseUserRole
from pyatlassdk.models.link import Link
from pyatlassdk.models.user_scope import UserScope

from pydantic import BaseModel, ConfigDict, Field

class CloudDatabaseUser(BaseModel):
    """Generated model for CloudDatabaseUser."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws_iam_type: Literal["NONE", "USER", "ROLE"] | None = Field(default=None, alias="awsIAMType", description="Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role.")
    database_name: Literal["admin", "$external"] = Field(alias="databaseName", description="The database against which the database user authenticates. Database users must provide both a username and authentication database to log into MongoDB. If the user authenticates with AWS IAM, x.509, LDAP, or OIDC Workload this value should be `$external`. If the user authenticates with SCRAM-SHA or OIDC Workforce, this value should be `admin`.")
    delete_after_date: datetime | None = Field(default=None, alias="deleteAfterDate", description="Date and time when MongoDB Cloud deletes the user. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. You must specify a future date that falls within one week of making the Application Programming Interface (API) request.")
    description: str | None = Field(default=None, description="Description of this database user.")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project.")
    labels: list[ComponentLabel] | None = Field(default=None, description="List that contains the key-value pairs for tagging and categorizing the MongoDB database user. The labels that you define do not appear in the console.")
    ldap_auth_type: Literal["NONE", "GROUP", "USER"] | None = Field(default=None, alias="ldapAuthType", description="Part of the Lightweight Directory Access Protocol (LDAP) record that the database uses to authenticate this database user on the LDAP host.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    oidc_auth_type: Literal["NONE", "IDP_GROUP", "USER"] | None = Field(default=None, alias="oidcAuthType", description="Human-readable label that indicates whether the new database user or group authenticates with OIDC federated authentication. To create a federated authentication user, specify the value of USER in this field. To create a federated authentication group, specify the value of `IDP_GROUP` in this field.")
    password: str | None = Field(default=None, description="Alphanumeric string that authenticates this database user against the database specified in `databaseName`. To authenticate with SCRAM-SHA, you must specify this parameter. This parameter doesn't appear in this response.")
    roles: list[DatabaseUserRole] = Field(description="List that provides the pairings of one role with one applicable database.")
    scopes: list[UserScope] | None = Field(default=None, description="List that contains clusters, MongoDB Atlas Data Lakes, and MongoDB Atlas Streams Workspaces that this database user can access. If omitted, MongoDB Cloud grants the database user access to all the clusters, MongoDB Atlas Data Lakes, and MongoDB Atlas Streams Workspaces in the project.")
    username: str = Field(description="Human-readable label that represents the user that authenticates to MongoDB. The format of this label depends on the method of authentication:\n\n| Authentication Method | Parameter Needed | Parameter Value | username Format |\n|---|---|---|---|\n| AWS IAM | `awsIAMType` | `ROLE` | <abbr title=\"Amazon Resource Name\">ARN</abbr> |\n| AWS IAM | `awsIAMType` | `USER` | <abbr title=\"Amazon Resource Name\">ARN</abbr> |\n| x.509 | `x509Type` | `CUSTOMER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |\n| x.509 | `x509Type` | `MANAGED` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |\n| LDAP | `ldapAuthType` | `USER` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |\n| LDAP | `ldapAuthType` | `GROUP` | [RFC 2253](https://tools.ietf.org/html/2253) Distinguished Name |\n| OIDC Workforce | `oidcAuthType` | `IDP_GROUP` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP group name |\n| OIDC Workload | `oidcAuthType` | `USER` | Atlas OIDC IdP ID (found in federation settings), followed by a '/', followed by the IdP user name |\n| SCRAM-SHA | `awsIAMType`, `x509Type`, `ldapAuthType`, `oidcAuthType` | `NONE` | Alphanumeric string |\n")
    x509_type: Literal["NONE", "CUSTOMER", "MANAGED"] | None = Field(default=None, alias="x509Type", description="X.509 method that MongoDB Cloud uses to authenticate the database user.\n\n- For application-managed X.509, specify `MANAGED`.\n- For self-managed X.509, specify `CUSTOMER`.\n\nUsers created with the `CUSTOMER` method require a Common Name (CN) in the **username** parameter. You must create externally authenticated users on the `$external` database.")
