"""Exercise 0 - Detect and explain Python virtual environments."""

import os
import site
import sys


def is_virtual_environment() -> bool:
    """Return True when Python runs inside a virtual environment."""
    return bool(
        getattr(sys, "real_prefix", None)
        or (hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix)
    )


def get_environment_name() -> str:
    """Return the current virtual environment directory name."""
    return os.path.basename(sys.prefix.rstrip(os.sep)) or "unknown_env"


def get_site_packages_path() -> str:
    """Get the preferred site-packages path for the active interpreter."""
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
    except Exception:
        pass


def print_outside_matrix() -> None:
    """Print guidance when no virtual environment is active."""
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    # print("Global package installation path:")
    # print(get_site_packages_path())
    # print("All installed packages affect the entire system.")q

    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\nScripts\nactivate\t# On Windows")
    print()
    print("Then run this program again.")


def print_inside_construct() -> None:
    """Print environment details when a virtual environment is active."""
    env_name = get_environment_name()
    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    print(get_site_packages_path())
    print("Packages here are isolated from the global system.")


def main() -> None:

    # """Entrypoint for environment status report."""
    if is_virtual_environment():
        print_inside_construct()
        return
    print_outside_matrix()


if __name__ == "__main__":
    main()