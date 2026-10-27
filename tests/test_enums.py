"""Case-insensitive enum helpers and enum fields on models."""

from __future__ import annotations

import pytest

from pyatlassdk.admin import _enums as admin_enums
from pyatlassdk.app import _enums as app_enums
from pyatlassdk.status import _enums as status_enums

ENUM_MODULES = [admin_enums, app_enums, status_enums]


@pytest.mark.parametrize("module", ENUM_MODULES)
def test_upper_case_uppercases_strings_only(module) -> None:
    assert module.upper_case("secondary") == "SECONDARY"
    assert module.upper_case("MiXeD") == "MIXED"
    assert module.upper_case(None) is None
    assert module.upper_case(5) == 5
    assert module.upper_case(["a"]) == ["a"]


@pytest.mark.parametrize("module", ENUM_MODULES)
def test_case_insensitive_enum_accepts_any_casing(module) -> None:
    class Color(module.CaseInsensitiveEnum):
        RED = "RED"
        BLUE = "BLUE"

    assert Color("red") is Color.RED
    assert Color("Blue") is Color.BLUE
    assert Color("RED") is Color.RED
    assert Color.RED == "RED"


@pytest.mark.parametrize("module", ENUM_MODULES)
def test_case_insensitive_enum_rejects_unknown_and_non_strings(module) -> None:
    class Color(module.CaseInsensitiveEnum):
        RED = "RED"

    with pytest.raises(ValueError):
        Color("green")
    with pytest.raises(ValueError):
        Color(1)
    with pytest.raises(ValueError):
        Color(None)
