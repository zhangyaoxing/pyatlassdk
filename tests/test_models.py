"""Structural checks across every generated pydantic model and enum."""

from __future__ import annotations

import enum
import importlib
import inspect
import pkgutil
from typing import Any

import pytest
from pydantic import BaseModel, ValidationError

PACKAGES = ["pyatlassdk.admin.models", "pyatlassdk.app.models", "pyatlassdk.status.models"]


def module_names(package: str) -> list[str]:
    pkg = importlib.import_module(package)
    return sorted(m.name for m in pkgutil.iter_modules(pkg.__path__) if not m.ispkg)


def classes_in(module_name: str) -> list[type]:
    module = importlib.import_module(module_name)
    return [
        obj
        for _, obj in inspect.getmembers(module, inspect.isclass)
        if obj.__module__ == module_name
    ]


ALL_MODULES = [f"{p}.{m}" for p in PACKAGES for m in module_names(p)]

# Models whose generated annotation is ``Literal[true]`` (lowercase), which pydantic cannot resolve.
# They are asserted broken in test_known_issues.py and excluded from the generic checks below.
UNRESOLVABLE = {
    "EmailPasswordAuthProvider",
    *(f"EmailPasswordAuthProviderConfigVariant{i}" for i in range(1, 7)),
    "PushPullAppConfig",
}


def exported_names(module_name: str) -> list[str]:
    """Public names a generated model module must expose (classes or type aliases)."""
    package, _, leaf = module_name.rpartition(".")
    lazy = getattr(importlib.import_module(package), "_MODULES", None)
    if lazy is not None:
        return [name for name, module in lazy.items() if module == leaf]
    return [cls.__name__ for cls in classes_in(module_name)]


def model_classes(module_name: str) -> list[type[BaseModel]]:
    return [
        cls
        for cls in classes_in(module_name)
        if issubclass(cls, BaseModel) and cls.__name__ not in UNRESOLVABLE
    ]


@pytest.fixture(params=ALL_MODULES)
def model_module(request: pytest.FixtureRequest) -> str:
    return request.param


def test_corpus_size_is_plausible() -> None:
    sizes = {p: len(module_names(p)) for p in PACKAGES}

    assert sizes["pyatlassdk.admin.models"] > 900
    assert sizes["pyatlassdk.app.models"] > 200
    assert sizes["pyatlassdk.status.models"] == 12


def test_module_exposes_its_declared_name(model_module: str) -> None:
    module = importlib.import_module(model_module)
    names = exported_names(model_module)

    assert names, f"{model_module} is not registered in its package"
    for name in names:
        assert hasattr(module, name), f"{model_module} does not define {name}"


def test_models_are_pydantic_or_enums(model_module: str) -> None:
    for cls in classes_in(model_module):
        assert issubclass(cls, (BaseModel, enum.Enum)), cls


def test_models_are_fully_resolved(model_module: str) -> None:
    for cls in model_classes(model_module):
        if True:
            assert cls.__pydantic_complete__, f"{cls.__name__} has unresolved forward references"


def test_models_accept_field_names_and_aliases(model_module: str) -> None:
    for cls in model_classes(model_module):
        assert cls.model_config.get("populate_by_name") is True, cls.__name__


def test_aliases_do_not_collide_with_other_fields(model_module: str) -> None:
    for cls in model_classes(model_module):
        names = set(cls.model_fields)
        aliases = [f.alias for f in cls.model_fields.values() if f.alias]
        assert len(aliases) == len(set(aliases)), f"duplicate alias in {cls.__name__}"
        for name, field in cls.model_fields.items():
            if field.alias and field.alias != name:
                assert field.alias not in names, f"{cls.__name__}.{name} alias shadows a field"


def test_models_without_required_fields_dump_to_empty(model_module: str) -> None:
    for cls in model_classes(model_module):
        if any(f.is_required() for f in cls.model_fields.values()):
            continue
        assert cls().model_dump(by_alias=True, exclude_none=True) == {}, cls.__name__


def test_model_json_schema_builds(model_module: str) -> None:
    for cls in model_classes(model_module):
        assert cls.model_json_schema(by_alias=True)


# --------------------------------------------------------------------------- lazy admin/app packages


@pytest.mark.parametrize("package", ["pyatlassdk.admin.models", "pyatlassdk.app.models"])
def test_lazy_exports_resolve_to_classes(package: str) -> None:
    models = importlib.import_module(package)
    modules = models._MODULES

    assert len(modules) == len(module_names(package))
    for name, module in modules.items():
        resolved = getattr(models, name)
        # Most exports are classes; the rest are TypeAlias unions, maps, or aliases of another
        # model (e.g. OrgLogIntegrationRequest -> OrgOtelLogIntegrationRequest, AnyValue -> Any).
        assert resolved is not None, name
        assert getattr(importlib.import_module(f"{package}.{module}"), name) is resolved


@pytest.mark.parametrize("package", ["pyatlassdk.admin.models", "pyatlassdk.app.models"])
def test_lazy_exports_cover_every_module(package: str) -> None:
    models = importlib.import_module(package)

    assert set(models._MODULES.values()) == set(module_names(package))
    assert dir(models) == sorted(models._MODULES)


@pytest.mark.parametrize("package", ["pyatlassdk.admin.models", "pyatlassdk.app.models"])
def test_lazy_unknown_attribute_raises_attribute_error(package: str) -> None:
    models = importlib.import_module(package)

    with pytest.raises(AttributeError):
        models.DoesNotExist  # noqa: B018


@pytest.mark.parametrize("package", ["pyatlassdk.admin.models", "pyatlassdk.app.models"])
def test_lazy_resolution_is_cached_in_module_globals(package: str) -> None:
    models = importlib.import_module(package)
    name = next(iter(models._MODULES))

    first = getattr(models, name)

    assert models.__dict__[name] is first


# --------------------------------------------------------------------------- behavior of specific shapes


def test_required_field_missing_raises() -> None:
    from pyatlassdk.admin.models.team_role import TeamRole

    with pytest.raises(ValidationError):
        TeamRole()


def test_alias_and_name_are_interchangeable_on_input() -> None:
    from pyatlassdk.admin.models.team_role import TeamRole

    by_alias = TeamRole(roleNames=["GROUP_OWNER"], teamId="t")
    by_name = TeamRole(role_names=["GROUP_OWNER"], team_id="t")

    assert by_alias == by_name
    assert by_name.model_dump(by_alias=True) == {
        "links": None,
        "roleNames": ["GROUP_OWNER"],
        "teamId": "t",
    }


def test_unknown_fields_are_kept_not_rejected() -> None:
    from pyatlassdk.admin.models.team_role import TeamRole

    role = TeamRole(roleNames=[], teamId="t", brandNew="x")

    assert role.model_extra == {"brandNew": "x"}
    assert role.model_dump(by_alias=True, exclude_none=True)["brandNew"] == "x"


def test_response_dicts_round_trip_through_a_model() -> None:
    from pyatlassdk.admin.models.team_role import TeamRole

    payload = {"roleNames": ["A"], "teamId": "t", "links": [{"href": "h", "rel": "self"}]}

    assert TeamRole.model_validate(payload).model_dump(by_alias=True, exclude_none=True) == payload


def test_map_fields_are_typed_as_string_dicts() -> None:
    from pyatlassdk.admin.models.cluster_connection_strings import ClusterConnectionStrings

    field = ClusterConnectionStrings.model_fields["aws_private_link"]

    assert "dict[str, str]" in str(field.annotation)


@pytest.mark.parametrize("value", ["secondary", "Secondary", "SECONDARY"])
def test_upper_case_enum_fields_normalize(value: Any) -> None:
    from pyatlassdk.admin.models.bi_connector import BiConnector

    assert BiConnector(read_preference=value).read_preference == "SECONDARY"
