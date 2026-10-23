"""Generated model for ApiUserEventViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.api_user_event_type_view_for_nds_group import ApiUserEventTypeViewForNdsGroup
from pyatlassdk.models.link import Link
from pyatlassdk.models.principal import Principal
from pyatlassdk.models.raw import Raw

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiUserEventViewForNdsGroup(BaseModel):
    """API User event identifies different activities around user API keys."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key_id: str | None = Field(default=None, alias="apiKeyId", description="Unique 24-hexadecimal digit string that identifies the API Key that triggered the event. If this resource returns this parameter, it doesn't return the `userId` parameter.")
    created: datetime = Field(description="Date and time when this event occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    delegate_principal: Principal | None = Field(default=None, alias="delegatePrincipal")
    event_type_name: ApiUserEventTypeViewForNdsGroup = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The `eventId` identifies the specific event.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the event.")
    is_global_admin: bool | None = Field(default=None, alias="isGlobalAdmin", description="Flag that indicates whether a MongoDB employee triggered the specified event.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    public_key: str | None = Field(default=None, alias="publicKey", description="Public part of the API key that triggered the event. If this resource returns this parameter, it doesn't return the **username** parameter.")
    raw: Raw | None = None
    remote_address: str | None = Field(default=None, alias="remoteAddress", description="IPv4 or IPv6 address from which the user triggered this event.")
    target_public_key: str | None = Field(default=None, alias="targetPublicKey", description="Public part of the API key that this event targets.")
    user_id: str | None = Field(default=None, alias="userId", description="Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn't return the `apiKeyId` parameter.")
    username: str | None = Field(default=None, description="Email address for the user who triggered this event. If this resource returns this parameter, it doesn't return the `publicApiKey` parameter.")
    whitelist_entry: str | None = Field(default=None, alias="whitelistEntry", description="Entry in the list of source host addresses that the API key accepts and this event targets.")
