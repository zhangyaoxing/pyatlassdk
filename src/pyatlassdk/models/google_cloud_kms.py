"""Generated model for GoogleCloudKMS. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class GoogleCloudKMS(BaseModel):
    """Details that define the configuration of Encryption at Rest using Google Cloud Key Management Service (KMS)."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled encryption at rest for the specified  project. To disable encryption at rest using customer key management and remove the configuration details, pass only this parameter with a value of `false`.")
    key_version_resource_id: str | None = Field(default=None, alias="keyVersionResourceID", description="Resource path that displays the key version resource ID for your Google Cloud KMS.")
    role_id: str | None = Field(default=None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies the Google Cloud Provider Access Role that MongoDB Cloud uses to access the Google Cloud KMS.")
    service_account_key: str | None = Field(default=None, alias="serviceAccountKey", description="JavaScript Object Notation (JSON) object that contains the Google Cloud Key Management Service (KMS). Format the JSON as a string and not as an object.")
    valid: bool | None = Field(default=None, description="Flag that indicates whether the Google Cloud Key Management Service (KMS) encryption key can encrypt and decrypt data.")
