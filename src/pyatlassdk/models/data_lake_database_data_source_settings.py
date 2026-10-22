"""Generated model for DataLakeDatabaseDataSourceSettings. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DataLakeDatabaseDataSourceSettings(BaseModel):
    """Data store that maps to a collection for this data lake."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    allow_insecure: bool | None = Field(default=None, alias="allowInsecure", description="Flag that validates the scheme in the specified URLs. If `true`, allows insecure `HTTP` scheme, doesn't verify the server's certificate chain and hostname, and accepts any certificate with any hostname presented by the server. If `false`, allows secure `HTTPS` scheme only.")
    collection: str | None = Field(default=None, description="Human-readable label that identifies the collection in the database. For creating a wildcard (`*`) collection, you must omit this parameter.")
    collection_regex: str | None = Field(default=None, alias="collectionRegex", description="Regex pattern to use for creating the wildcard (*) collection. To learn more about the regex syntax, see [Go programming language](https://pkg.go.dev/regexp).")
    database: str | None = Field(default=None, description="Human-readable label that identifies the database, which contains the collection in the cluster. You must omit this parameter to generate wildcard (`*`) collections for dynamically generated databases.")
    database_regex: str | None = Field(default=None, alias="databaseRegex", description="Regex pattern to use for creating the wildcard (*) database. To learn more about the regex syntax, see [Go programming language](https://pkg.go.dev/regexp).")
    dataset_name: str | None = Field(default=None, alias="datasetName", description="Human-readable label that identifies the dataset that Atlas generates for an ingestion pipeline run or Online Archive.")
    dataset_prefix: str | None = Field(default=None, alias="datasetPrefix", description="Human-readable label that matches against the dataset names for ingestion pipeline runs or Online Archives.")
    default_format: Literal[".avro", ".avro.bz2", ".avro.gz", ".bson", ".bson.bz2", ".bson.gz", ".bsonx", ".csv", ".csv.bz2", ".csv.gz", ".json", ".json.bz2", ".json.gz", ".orc", ".parquet", ".tsv", ".tsv.bz2", ".tsv.gz"] | None = Field(default=None, alias="defaultFormat", description="File format that MongoDB Cloud uses if it encounters a file without a file extension while searching **storeName**.")
    path: str | None = Field(default=None, description="File path that controls how MongoDB Cloud searches for and parses files in the **storeName** before mapping them to a collection.Specify ``/`` to capture all files and folders from the ``prefix`` path.")
    provenance_field_name: str | None = Field(default=None, alias="provenanceFieldName", description="Name for the field that includes the provenance of the documents in the results. MongoDB Cloud returns different fields in the results for each supported provider.")
    store_name: str | None = Field(default=None, alias="storeName", description="Human-readable label that identifies the data store that MongoDB Cloud maps to the collection.")
    trim_level: int | None = Field(default=None, alias="trimLevel", description="Unsigned integer that specifies how many fields of the dataset name to trim from the left of the dataset name before mapping the remaining fields to a wildcard collection name.")
    urls: list[str] | None = Field(default=None, description="URLs of the publicly accessible data files. You can't specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter.")
