"""Generated model for ClusterDescriptionProcessArgs20240805. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterDescriptionProcessArgs20240805(BaseModel):
    """Advanced MongoDB process configuration options applied to the cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    change_stream_options_pre_and_post_images_expire_after_seconds: int | None = Field(default=None, alias="changeStreamOptionsPreAndPostImagesExpireAfterSeconds", description="The minimum pre- and post-image retention time in seconds.")
    chunk_migration_concurrency: int | None = Field(default=None, alias="chunkMigrationConcurrency", description="Number of threads on the source shard and the receiving shard for chunk migration. The number of threads should not exceed the half the total number of CPU cores in the sharded cluster.")
    custom_openssl_cipher_config_tls12: list[Annotated[Literal["TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"], BeforeValidator(upper_case)]] | None = Field(default=None, alias="customOpensslCipherConfigTls12", description="The custom OpenSSL cipher suite list for TLS 1.2. Requires `tlsCipherConfigMode` = `CUSTOM`; when `tlsCipherConfigMode` is omitted, supplying a non-empty list infers `CUSTOM`.")
    custom_openssl_cipher_config_tls13: list[Annotated[Literal["TLS_AES_256_GCM_SHA384", "TLS_CHACHA20_POLY1305_SHA256", "TLS_AES_128_GCM_SHA256", "TLS_AES_128_CCM_SHA256"], BeforeValidator(upper_case)]] | None = Field(default=None, alias="customOpensslCipherConfigTls13", description="The custom OpenSSL cipher suite list for TLS 1.3. Requires `tlsCipherConfigMode` = `CUSTOM`; when `tlsCipherConfigMode` is omitted, supplying a non-empty list infers `CUSTOM`.")
    default_max_time_ms: int | None = Field(default=None, alias="defaultMaxTimeMS", description="Default time limit in milliseconds for individual read operations to complete.")
    default_write_concern: str | None = Field(default=None, alias="defaultWriteConcern", description="Default level of acknowledgment requested from MongoDB for write operations when none is specified by the driver.")
    javascript_enabled: bool | None = Field(default=None, alias="javascriptEnabled", description="Flag that indicates whether the cluster allows execution of operations that perform server-side executions of JavaScript. When using 8.0+, we recommend disabling server-side JavaScript and using operators of aggregation pipeline as more performant alternative.")
    minimum_enabled_tls_protocol: Annotated[Literal["TLS1_0", "TLS1_1", "TLS1_2", "TLS1_3"], BeforeValidator(upper_case)] | None = Field(default=None, alias="minimumEnabledTlsProtocol", description="Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections. Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version.")
    no_table_scan: bool | None = Field(default=None, alias="noTableScan", description="Flag that indicates whether the cluster disables executing any query that requires a collection scan to return results.")
    oplog_min_retention_hours: float | None = Field(default=None, alias="oplogMinRetentionHours", description="Minimum retention window for cluster's oplog expressed in hours. A value of null indicates that the cluster uses the default minimum oplog window that MongoDB Cloud calculates.")
    oplog_size_mb: int | None = Field(default=None, alias="oplogSizeMB", description="Storage limit of cluster's oplog expressed in megabytes. A value of null indicates that the cluster uses the default oplog size that MongoDB Cloud calculates.")
    query_stats_log_verbosity: int | None = Field(default=None, alias="queryStatsLogVerbosity", description="May be set to 1 (disabled) or 3 (enabled). When set to 3, Atlas will include redacted and anonymized `$queryStats` output in MongoDB logs. `$queryStats` output does not contain literals or field values. Enabling this setting might impact the performance of your cluster.")
    sample_refresh_interval_bi_connector: int | None = Field(default=None, alias="sampleRefreshIntervalBIConnector", description="Interval in seconds at which the mongosqld process re-samples data to create its relational schema.")
    sample_size_bi_connector: int | None = Field(default=None, alias="sampleSizeBIConnector", description="Number of documents per database to sample when gathering schema information.")
    tls_cipher_config_mode: Annotated[Literal["CUSTOM", "DEFAULT"], BeforeValidator(upper_case)] | None = Field(default=None, alias="tlsCipherConfigMode", description="The TLS cipher suite configuration mode. The default mode uses the default cipher suites. The custom mode allows you to specify custom cipher suites for both TLS 1.2 and TLS 1.3.")
    transaction_lifetime_limit_seconds: int | None = Field(default=None, alias="transactionLifetimeLimitSeconds", description="Lifetime, in seconds, of multi-document transactions. Atlas considers the transactions that exceed this limit as expired and so aborts them through a periodic clean-up process.")
