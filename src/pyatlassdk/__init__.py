"""Generated MongoDB Atlas SDK. Do not edit manually."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from pyatlassdk.client import AtlasApiError, AtlasClient

try:
    __version__ = version("pyatlassdk")
except PackageNotFoundError:  # pragma: no cover - running from a source checkout
    __version__ = "0.0.0"

__all__ = ["AtlasApiError", "AtlasClient", "__version__"]
