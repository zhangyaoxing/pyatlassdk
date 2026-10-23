"""Generated model for OrganizationSettings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.custom_session_timeouts import CustomSessionTimeouts

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrganizationSettings(BaseModel):
    """Collection of settings that configures the organization."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_access_list_required: bool | None = Field(default=None, alias="apiAccessListRequired", description="Flag that indicates whether to require API operations to originate from an IP Address added to the API access list for the specified organization.")
    custom_session_timeouts: CustomSessionTimeouts | None = Field(default=None, alias="customSessionTimeouts")
    gen_ai_features_enabled: bool | None = Field(default=None, alias="genAIFeaturesEnabled", description="Flag that indicates whether this organization has access to generative AI features. This setting only applies to Atlas Commercial and is enabled by default. Once this setting is turned on, Project Owners may be able to enable or disable individual AI features at the project level.")
    max_service_account_secret_validity_in_hours: int | None = Field(default=None, alias="maxServiceAccountSecretValidityInHours", description="Number that represents the maximum period before expiry in hours for new Atlas Admin API Service Account secrets within the specified organization.")
    multi_factor_auth_required: bool | None = Field(default=None, alias="multiFactorAuthRequired", description="Flag that indicates whether to require users to set up Multi-Factor Authentication (MFA) before accessing the specified organization. To learn more, see: https://www.mongodb.com/docs/atlas/security-multi-factor-authentication/.")
    operations_contact: str | None = Field(default=None, alias="operationsContact", description="String that specifies a distribution list email address for the specified organization to receive proactive notifications about its infrastructure. The operations contact is used for notifications only and is not authorized to make decisions or approvals. Passing an explicit null clears the existing operations contact (if any). An empty string is invalid and is rejected with a validation error.")
    restrict_employee_access: bool | None = Field(default=None, alias="restrictEmployeeAccess", description="Flag that indicates whether to block MongoDB Support from accessing Atlas infrastructure and cluster logs for any deployment in the specified organization without explicit permission. Once this setting is turned on, you can grant MongoDB Support a 24-hour bypass access to the Atlas deployment to resolve support issues. To learn more, see: https://www.mongodb.com/docs/atlas/security-restrict-support-access/.")
    security_contact: str | None = Field(default=None, alias="securityContact", description="String that specifies a single email address for the specified organization to receive security-related notifications. Specifying a security contact does not grant them authorization or access to Atlas for security decisions or approvals. An empty string is valid and clears the existing security contact (if any).")
    streams_cross_group_enabled: bool | None = Field(default=None, alias="streamsCrossGroupEnabled", description="Flag that indicates whether a group's Atlas Stream Processing workspaces in this organization can create connections to other group's clusters in the same organization.")
