"""Top-level package surface: exports, aliases, version and typing marker."""

from __future__ import annotations

from pathlib import Path

import pyatlassdk
from pyatlassdk.admin import AtlasAdminClient, AtlasApiError
from pyatlassdk.admin import _errors as admin_errors
from pyatlassdk.app import _errors as app_errors
from pyatlassdk.status import _errors as status_errors

PACKAGE_DIR = Path(pyatlassdk.__file__).parent


def test_all_exports_resolve() -> None:
    for name in pyatlassdk.__all__:
        assert hasattr(pyatlassdk, name), name


def test_backwards_compatible_aliases() -> None:
    assert pyatlassdk.AtlasClient is pyatlassdk.AtlasAdminClient
    assert pyatlassdk.AtlasApiError is pyatlassdk.AtlasAdminApiError


def test_each_package_has_its_own_error_type() -> None:
    errors = {
        pyatlassdk.AtlasAdminApiError,
        pyatlassdk.AtlasAppApiError,
        pyatlassdk.AtlasStatusApiError,
    }
    assert len(errors) == 3
    assert pyatlassdk.AtlasAdminApiError is admin_errors.AtlasApiError
    assert pyatlassdk.AtlasAppApiError is app_errors.AtlasApiError
    assert pyatlassdk.AtlasStatusApiError is status_errors.AtlasApiError


def test_subpackages_reexport_client_and_error() -> None:
    assert AtlasAdminClient is pyatlassdk.AtlasAdminClient
    assert AtlasApiError is pyatlassdk.AtlasAdminApiError

    from pyatlassdk import app, status

    assert app.AtlasAppAdminClient is pyatlassdk.AtlasAppAdminClient
    assert app.AtlasApiError is pyatlassdk.AtlasAppApiError
    assert status.AtlasStatusClient is pyatlassdk.AtlasStatusClient
    assert status.AtlasApiError is pyatlassdk.AtlasStatusApiError


def test_version_is_a_string() -> None:
    assert isinstance(pyatlassdk.__version__, str)
    assert pyatlassdk.__version__.count(".") >= 2


def test_py_typed_markers_ship_with_every_package() -> None:
    for relative in ("py.typed", "admin/py.typed", "app/py.typed", "status/py.typed"):
        assert (PACKAGE_DIR / relative).exists(), relative
