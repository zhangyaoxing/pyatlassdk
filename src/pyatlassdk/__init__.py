"""MongoDB Atlas SDKs."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from pyatlassdk.admin.client import AtlasAdminClient
from pyatlassdk.admin.client import AtlasApiError as AtlasAdminApiError
from pyatlassdk.app.client import AtlasApiError as AtlasAppApiError
from pyatlassdk.app.client import AtlasAppAdminClient
from pyatlassdk.status.client import AtlasApiError as AtlasStatusApiError
from pyatlassdk.status.client import AtlasStatusClient

try:
    __version__ = version("pyatlassdk")
except PackageNotFoundError:  # pragma: no cover - running from a source checkout
    __version__ = "0.0.0"

# Backwards-compatible aliases for the Atlas Administration API client.
AtlasClient = AtlasAdminClient
AtlasApiError = AtlasAdminApiError

__all__ = [
    "AtlasAdminApiError",
    "AtlasAdminClient",
    "AtlasApiError",
    "AtlasAppAdminClient",
    "AtlasAppApiError",
    "AtlasClient",
    "AtlasStatusApiError",
    "AtlasStatusClient",
    "__version__",
]
