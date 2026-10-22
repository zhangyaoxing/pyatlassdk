"""Generated model for ApiAtlasClusterAdvancedConfigurationView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasClusterAdvancedConfigurationView(BaseModel):
    """Group of settings that configures a subset of the advanced configuration details."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    custom_openssl_cipher_config_tls12: list[Literal["TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"]] | None = Field(default=None, alias="customOpensslCipherConfigTls12", description="The custom OpenSSL cipher suite list for TLS 1.2. Requires `tlsCipherConfigMode` = `CUSTOM`; when `tlsCipherConfigMode` is omitted, supplying a non-empty list infers `CUSTOM`.")
    custom_openssl_cipher_config_tls13: list[Literal["TLS_AES_256_GCM_SHA384", "TLS_CHACHA20_POLY1305_SHA256", "TLS_AES_128_GCM_SHA256", "TLS_AES_128_CCM_SHA256"]] | None = Field(default=None, alias="customOpensslCipherConfigTls13", description="The custom OpenSSL cipher suite list for TLS 1.3. Requires `tlsCipherConfigMode` = `CUSTOM`; when `tlsCipherConfigMode` is omitted, supplying a non-empty list infers `CUSTOM`.")
    minimum_enabled_tls_protocol: Literal["TLS1_0", "TLS1_1", "TLS1_2", "TLS1_3"] | None = Field(default=None, alias="minimumEnabledTlsProtocol", description="Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections. Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version.")
    tls_cipher_config_mode: Literal["CUSTOM", "DEFAULT"] | None = Field(default=None, alias="tlsCipherConfigMode", description="The TLS cipher suite configuration mode. The default mode uses the default cipher suites. The custom mode allows you to specify custom cipher suites for both TLS 1.2 and TLS 1.3.")
