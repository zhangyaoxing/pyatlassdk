"""Load environment variables from a nearby .env file."""

from __future__ import annotations

from dotenv import find_dotenv, load_dotenv


def load_env() -> bool:
    """Load the nearest .env file from the current directory upward.

    Existing environment variables are not overridden. Returns ``True`` when a
    file was found and loaded.
    """
    path = find_dotenv(usecwd=True)
    if not path:
        return False
    return load_dotenv(path, override=False)
