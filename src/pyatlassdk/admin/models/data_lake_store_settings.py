"""Generated model for DataLakeStoreSettings. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.data_lake_atlas_store_instance import DataLakeAtlasStoreInstance
from pyatlassdk.admin.models.data_lake_azure_blob_store import DataLakeAzureBlobStore
from pyatlassdk.admin.models.data_lake_dlsaws_store import DataLakeDLSAWSStore
from pyatlassdk.admin.models.data_lake_dls_azure_store import DataLakeDLSAzureStore
from pyatlassdk.admin.models.data_lake_dlsgcp_store import DataLakeDLSGCPStore
from pyatlassdk.admin.models.data_lake_google_cloud_storage_store import DataLakeGoogleCloudStorageStore
from pyatlassdk.admin.models.data_lake_http_store import DataLakeHTTPStore
from pyatlassdk.admin.models.data_lake_s3_store_settings import DataLakeS3StoreSettings

DataLakeStoreSettings: TypeAlias = DataLakeS3StoreSettings | DataLakeDLSAWSStore | DataLakeDLSAzureStore | DataLakeDLSGCPStore | DataLakeAtlasStoreInstance | DataLakeHTTPStore | DataLakeAzureBlobStore | DataLakeGoogleCloudStorageStore
