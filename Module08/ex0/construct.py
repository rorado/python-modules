
import os
import site
import sys


def is_virtual_environment() -> bool:
    return bool(
        (hasattr(sys, "base_prefix") and sys.prefix != sys.base_prefix)
    )


def get_environment_name() -> str:
    return os.path.basename(sys.prefix) or "unknown_env"


def get_site_packages_path() -> str:
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
    except Exception:
        pass


def print_outside_matrix() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")

    print()
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\nScripts\nactivate\t# On Windows")
    print()
    print("Then run this program again.")


def print_inside_construct() -> None:
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

    if is_virtual_environment():
        print_inside_construct()
        return
    print_outside_matrix()


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
