from __future__ import annotations

import os

from pyatlassdk import AtlasAdminClient, AtlasAppAdminClient
from pyatlassdk._env import load_env


def test_admin_client_reads_credentials_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("MONGO_ATLAS_PUBLIC_KEY", "public")
    monkeypatch.setenv("MONGO_ATLAS_PRIVATE_KEY", "private")

    with AtlasAdminClient() as client:
        assert client.auth_mode == "digest"


def test_app_client_reads_access_token_from_environment(monkeypatch) -> None:
    monkeypatch.setenv("MONGO_ATLAS_ACCESS_TOKEN", "token")

    with AtlasAppAdminClient() as client:
        assert client.auth_mode == "bearer"


def test_load_env_reads_dotenv(tmp_path, monkeypatch) -> None:
    monkeypatch.delenv("MONGO_ATLAS_TEST_VALUE", raising=False)
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text("MONGO_ATLAS_TEST_VALUE=from-dotenv\n", encoding="utf-8")

    assert load_env() is True
    assert os.environ["MONGO_ATLAS_TEST_VALUE"] == "from-dotenv"


def test_dotenv_credentials_are_used_by_admin_client(tmp_path, monkeypatch) -> None:
    for name in ("MONGO_ATLAS_PUBLIC_KEY", "MONGO_ATLAS_PRIVATE_KEY"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.chdir(tmp_path)
    (tmp_path / ".env").write_text(
        "MONGO_ATLAS_PUBLIC_KEY=dotenv-public\nMONGO_ATLAS_PRIVATE_KEY=dotenv-private\n",
        encoding="utf-8",
    )

    assert load_env() is True
    with AtlasAdminClient() as client:
        assert client.auth_mode == "digest"
