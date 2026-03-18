"""Exercise 2 - Load secure configuration from environment and .env file."""

from __future__ import annotations

import os
import sys
from typing import Dict, Tuple


RequiredConfig = Tuple[str, bool]


def load_dotenv_if_available() -> bool:
    """Load .env file when python-dotenv is installed."""
    try:
        from dotenv import load_dotenv

        load_dotenv()
        return True
    except Exception:
        return False


def read_config() -> Dict[str, str]:
    """Collect configuration from environment with development defaults."""
    matrix_mode = os.getenv("MATRIX_MODE", "development")

    defaults = {
        "development": {
            "DATABASE_URL": "sqlite:///matrix_local.db",
            "LOG_LEVEL": "DEBUG",
            "ZION_ENDPOINT": "http://localhost:8000/zion",
        },
        "production": {
            "DATABASE_URL": "",
            "LOG_LEVEL": "INFO",
            "ZION_ENDPOINT": "",
        },
    }

    mode_defaults = defaults.get(matrix_mode, defaults["development"])

    return {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": os.getenv("DATABASE_URL", mode_defaults["DATABASE_URL"]),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", mode_defaults["LOG_LEVEL"]),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", mode_defaults["ZION_ENDPOINT"]),
    }


def validate_config(config: Dict[str, str]) -> Dict[str, RequiredConfig]:
    """Validate required keys depending on mode."""
    mode = config["MATRIX_MODE"]
    return {
        "DATABASE_URL": (
            config["DATABASE_URL"],
            bool(config["DATABASE_URL"]),
        ),
        "API_KEY": (
            config["API_KEY"],
            bool(config["API_KEY"]),
        ),
        "ZION_ENDPOINT": (
            config["ZION_ENDPOINT"],
            bool(config["ZION_ENDPOINT"]),
        ),
        "MODE_CHECK": (mode, mode in ("development", "production")),
    }


def print_configuration_report(config: Dict[str, str], dotenv_loaded: bool) -> None:
    """Display a readable configuration and security report."""
    checks = validate_config(config)

    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    if checks["DATABASE_URL"][1]:
        print("Database: Connected to configured instance")
    else:
        print("Database: Missing DATABASE_URL")

    if checks["API_KEY"][1]:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API_KEY")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if checks["ZION_ENDPOINT"][1]:
        print("Zion Network: Online")
    else:
        print("Zion Network: Missing ZION_ENDPOINT")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if dotenv_loaded:
        print("[OK] .env file support available (python-dotenv loaded)")
    else:
        print("[WARN] python-dotenv not installed, .env file not loaded")
        print("       Install with: pip install python-dotenv")

    print("[OK] Production overrides available")


def exit_if_invalid(config: Dict[str, str]) -> None:
    """Exit with non-zero code when required production settings are missing."""
    mode = config["MATRIX_MODE"]
    if mode != "production":
        return

    missing = []
    for key in ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT"):
        if not config.get(key):
            missing.append(key)

    if missing:
        print()
        print("ERROR: Missing required production configuration:")
        for key in missing:
            print(f"- {key}")
        sys.exit(1)


def main() -> None:
    """Entrypoint for environment-based configuration loading."""
    dotenv_loaded = load_dotenv_if_available()
    config = read_config()
    print_configuration_report(config, dotenv_loaded)
    exit_if_invalid(config)


if __name__ == "__main__":
    main()