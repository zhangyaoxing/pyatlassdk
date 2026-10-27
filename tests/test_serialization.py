"""``_serialize`` and ``_payload`` helpers, identical in all three generated clients."""

from __future__ import annotations

import datetime as dt
import importlib

import httpx
import pytest
from pydantic import BaseModel, ConfigDict, Field

MODULES = ["pyatlassdk.admin.client", "pyatlassdk.app.client", "pyatlassdk.status.client"]


@pytest.fixture(params=MODULES)
def client_module(request: pytest.FixtureRequest):
    return importlib.import_module(request.param)


class Inner(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    first_name: str | None = Field(default=None, alias="firstName")


class Outer(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    created_at: dt.datetime | None = Field(default=None, alias="createdAt")
    inner_items: list[Inner] | None = Field(default=None, alias="innerItems")
    note: str | None = None


def test_model_uses_aliases_and_drops_none(client_module) -> None:
    result = client_module._serialize(Outer(note="n"))

    assert result == {"note": "n"}


def test_nested_models_and_datetimes_become_json_values(client_module) -> None:
    outer = Outer(
        created_at=dt.datetime(2026, 1, 2, 3, 4, 5, tzinfo=dt.timezone.utc),
        inner_items=[Inner(first_name="a"), Inner()],
    )

    assert client_module._serialize(outer) == {
        "createdAt": "2026-01-02T03:04:05Z",
        "innerItems": [{"firstName": "a"}, {}],
    }


def test_lists_and_dicts_are_walked_recursively(client_module) -> None:
    value = {"models": [Inner(first_name="x")], "when": dt.date(2026, 5, 6), "n": 1}

    assert client_module._serialize(value) == {
        "models": [{"firstName": "x"}],
        "when": "2026-05-06",
        "n": 1,
    }


def test_datetime_and_date_are_isoformatted(client_module) -> None:
    moment = dt.datetime(2026, 1, 1, 12, 30)

    assert client_module._serialize(moment) == "2026-01-01T12:30:00"
    assert client_module._serialize(dt.date(2026, 1, 1)) == "2026-01-01"


@pytest.mark.parametrize("scalar", [None, 0, 1.5, True, "text"])
def test_scalars_pass_through(client_module, scalar) -> None:
    assert client_module._serialize(scalar) is scalar


def test_payload_prefers_json(client_module) -> None:
    assert client_module._payload(httpx.Response(200, json={"a": 1})) == {"a": 1}


def test_payload_falls_back_to_text(client_module) -> None:
    assert client_module._payload(httpx.Response(500, text="plain failure")) == "plain failure"


def test_payload_of_empty_body_is_empty_string(client_module) -> None:
    assert client_module._payload(httpx.Response(500)) == ""
