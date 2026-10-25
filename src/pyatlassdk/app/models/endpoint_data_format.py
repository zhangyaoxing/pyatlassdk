"""Generated model for EndpointDataFormat. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app._enums import CaseInsensitiveEnum

class EndpointDataFormat(CaseInsensitiveEnum):
    """A [data format](https://mongodb.com/docs/atlas/app-services/data-api/#data-formats) supported by the Data API & custom endpoints."""
    JSON = "JSON"
    EJSON = "EJSON"
