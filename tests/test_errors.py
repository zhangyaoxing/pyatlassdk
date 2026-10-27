"""AtlasApiError behavior for each generated package."""

from __future__ import annotations

import pytest

from pyatlassdk import AtlasAdminApiError, AtlasAppApiError, AtlasStatusApiError

ERROR_TYPES = [AtlasAdminApiError, AtlasAppApiError, AtlasStatusApiError]


@pytest.mark.parametrize("error_type", ERROR_TYPES)
def test_error_carries_status_message_and_payload(error_type: type[Exception]) -> None:
    error = error_type(404, "not found", {"detail": "missing"})

    assert str(error) == "HTTP 404: not found"
    assert error.status_code == 404  # type: ignore[attr-defined]
    assert error.payload == {"detail": "missing"}  # type: ignore[attr-defined]


@pytest.mark.parametrize("error_type", ERROR_TYPES)
def test_error_payload_defaults_to_none(error_type: type[Exception]) -> None:
    assert error_type(500, "boom").payload is None  # type: ignore[attr-defined]


@pytest.mark.parametrize("error_type", ERROR_TYPES)
def test_error_is_a_plain_exception(error_type: type[Exception]) -> None:
    with pytest.raises(Exception, match="HTTP 418: teapot"):
        raise error_type(418, "teapot")


def test_error_types_are_not_interchangeable() -> None:
    with pytest.raises(AtlasAdminApiError):
        try:
            raise AtlasAdminApiError(400, "x")
        except AtlasAppApiError:  # pragma: no cover - must not match
            pytest.fail("admin error caught as app error")
