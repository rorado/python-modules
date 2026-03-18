"""Exercise 0 - Detect and explain Python virtual environments."""

from __future__ import annotations

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

	user_site = site.getusersitepackages()
	return user_site if user_site else "Unavailable"


def print_outside_matrix() -> None:
	"""Print guidance when no virtual environment is active."""
	print("MATRIX STATUS: You're still plugged in")
	print(f"Current Python: {sys.executable}")
	print("Virtual Environment: None detected")
	print("WARNING: You're in the global environment!")
	print("The machines can see everything you install.")
	print("Global package installation path:")
	print(get_site_packages_path())
	print("To enter the construct, run:")
	print("python -m venv matrix_env")
	print("source matrix_env/bin/activate  # On Unix")
	print("matrix_env\\Scripts\\activate  # On Windows")
	print("Then run this program again.")


def print_inside_construct() -> None:
	"""Print environment details when a virtual environment is active."""
	env_name = get_environment_name()
	print("MATRIX STATUS: Welcome to the construct")
	print(f"Current Python: {sys.executable}")
	print(f"Virtual Environment: {env_name}")
	print(f"Environment Path: {sys.prefix}")
	print("SUCCESS: You're in an isolated environment!")
	print("Safe to install packages without affecting the global system.")
	print("Package installation path:")
	print(get_site_packages_path())


def main() -> None:
	"""Entrypoint for environment status report."""
	if is_virtual_environment():
		print_inside_construct()
		return
	print_outside_matrix()


if __name__ == "__main__":
	main()
