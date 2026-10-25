"""Generated model for StreamsPrivateLinkConnection. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsPrivateLinkConnection(BaseModel):
    """Container for metadata needed to create a Private Link connection."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The ID of the Private Link connection.")
    arn: str | None = Field(default=None, description="Amazon Resource Name (ARN). Required for AWS Provider and MSK vendor.")
    authentication_scheme: Annotated[Literal["TLS", "SASL_SCRAM", "IAM"], BeforeValidator(upper_case)] | None = Field(default=None, alias="authenticationScheme", description="Authentication mechanism to use with this private networking connection.")
    azure_resource_ids: list[str] | None = Field(default=None, alias="azureResourceIds", description="Azure Resource IDs of each availability zone for the Azure Confluent cluster.")
    dns_domain: str | None = Field(default=None, alias="dnsDomain", description="The domain hostname. Required for the following provider and vendor combinations:\n- AWS provider with CONFLUENT vendor.\n- AZURE provider with EVENTHUB or CONFLUENT vendor.")
    dns_sub_domain: list[str] | None = Field(default=None, alias="dnsSubDomain", description="Sub-Domain name of Confluent cluster. These are typically your availability zones. Required for AWS Provider and CONFLUENT vendor, if your AWS CONFLUENT cluster doesn't use subdomains, you must set this to the empty array [].")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message if the state is FAILED.")
    gcp_connection_ids: list[str] | None = Field(default=None, alias="gcpConnectionIds", description="List of GCP Private Service Connect connection IDs.")
    gcp_service_attachment_uris: list[str] | None = Field(default=None, alias="gcpServiceAttachmentUris", description="Service Attachment URIs of each availability zone for the GCP Confluent cluster.")
    interface_endpoint_id: str | None = Field(default=None, alias="interfaceEndpointId", description="Interface endpoint ID that is created from the service endpoint ID provided.")
    interface_endpoint_name: str | None = Field(default=None, alias="interfaceEndpointName", description="Interface endpoint name that is created from the service endpoint ID provided.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    provider: str = Field(description="Cloud provider where the private endpoint's target resource is deployed. Valid values are AWS, AZURE, and GCP.")
    provider_account_id: str | None = Field(default=None, alias="providerAccountId", description="Account ID from the cloud provider.")
    region: str | None = Field(default=None, description="The region of the Provider\u2019s cluster. See [AWS](https://www.mongodb.com/docs/atlas/reference/amazon-aws/#stream-processing-workspaces), [AZURE](https://www.mongodb.com/docs/atlas/reference/microsoft-azure/#stream-processing-workspaces), and [GCP](https://www.mongodb.com/docs/atlas/reference/google-gcp/#stream-processing-workspaces) supported regions.")
    service_endpoint_id: str | None = Field(default=None, alias="serviceEndpointId", description="For AZURE EVENTHUB, this is the [namespace endpoint ID](https://learn.microsoft.com/en-us/rest/api/eventhub/namespaces/get). For AWS CONFLUENT cluster, this is the [VPC Endpoint service name](https://docs.confluent.io/cloud/current/networking/private-links/aws-privatelink.html).")
    state: str | None = Field(default=None, description="State the connection is in.")
    vendor: str | None = Field(default=None, description="Vendor that manages the cloud service. The list of supported vendor values is:\n- AWS\n-- `MSK` for AWS MSK Kafka clusters\n-- `CONFLUENT` for Confluent Kafka clusters on AWS\n-- `KINESIS` for AWS Kinesis Data Streams\n-- `S3` for AWS S3\n-- `LAMBDA` for AWS Lambda\n\n- Azure\n-- `EVENTHUB` for Azure EventHub.\n-- `CONFLUENT` for Confluent Kafka clusters on Azure\n-- `AZURE_BLOB_STORAGE` for Azure Blob Storage\n\n- GCP\n-- `CONFLUENT` for Confluent Kafka clusters on GCP\n-- `PUBSUB` for Google Cloud Pub/Sub\n\n**NOTE** Omitting the vendor field will default to using the GENERIC vendor.")
