"""Generated model for NDSServerlessInstanceAuditView. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.link import Link
from pyatlassdk.models.nds_serverless_instance_audit_type_view import NDSServerlessInstanceAuditTypeView
from pyatlassdk.models.principal import Principal
from pyatlassdk.models.raw import Raw

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NDSServerlessInstanceAuditView(BaseModel):
    """Serverless instance audit identifies any activities around serverless instance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key_id: str | None = Field(default=None, alias="apiKeyId", description="Unique 24-hexadecimal digit string that identifies the API Key that triggered the event. If this resource returns this parameter, it doesn't return the `userId` parameter.")
    created: datetime = Field(description="Date and time when this event occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    delegate_principal: Principal | None = Field(default=None, alias="delegatePrincipal")
    event_type_name: NDSServerlessInstanceAuditTypeView = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The `eventId` identifies the specific event.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the event.")
    is_global_admin: bool | None = Field(default=None, alias="isGlobalAdmin", description="Flag that indicates whether a MongoDB employee triggered the specified event.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    public_key: str | None = Field(default=None, alias="publicKey", description="Public part of the API key that triggered the event. If this resource returns this parameter, it doesn't return the **username** parameter.")
    raw: Raw | None = None
    remote_address: str | None = Field(default=None, alias="remoteAddress", description="IPv4 or IPv6 address from which the user triggered this event.")
    user_id: str | None = Field(default=None, alias="userId", description="Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn't return the `apiKeyId` parameter.")
    username: str | None = Field(default=None, description="Email address for the user who triggered this event. If this resource returns this parameter, it doesn't return the `publicApiKey` parameter.")
