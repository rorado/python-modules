"""Exercise 1 - Dependency loading and sample Matrix data analysis."""

from __future__ import annotations

import importlib
import sys
from typing import Any, Dict, Optional, Tuple


DependencyResult = Tuple[bool, Optional[str], Optional[str], Optional[Any]]


def check_dependency(module_name: str, package_name: str) -> DependencyResult:
    """Try to import a module and return (ok, display_name, version, module)."""
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        return True, package_name, str(version), module
    except Exception:
        return False, package_name, None, None


def print_dependency_status(results: Dict[str, DependencyResult]) -> None:
    """Display dependency checks with clear install guidance."""
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    all_ok = True
    for key in ("pandas", "numpy", "matplotlib", "requests"):
        ok, package_name, version, _module = results[key]
        if ok:
            print(f"[OK] {package_name} ({version}) - Ready")
        else:
            all_ok = False
            print(f"[MISSING] {package_name} - Not installed")

    print()
    print("Dependency management options:")
    print("- pip: use requirements.txt")
    print("  pip install -r requirements.txt")
    print("- Poetry: use pyproject.toml (+ poetry.lock)")
    print("  poetry install")

    if not all_ok:
        print()
        print("Missing dependencies detected. Install them, then rerun loading.py")
        return

    print()
    print("All essential programs loaded successfully.")


def run_analysis(results: Dict[str, DependencyResult]) -> None:
    """Run a tiny data pipeline and generate a visualization."""
    pandas_module = results["pandas"][3]
    numpy_module = results["numpy"][3]
    matplotlib_module = results["matplotlib"][3]

    if pandas_module is None or numpy_module is None or matplotlib_module is None:
        return

    try:
        pyplot = importlib.import_module("matplotlib.pyplot")
    except Exception:
        print("Unable to load matplotlib.pyplot, visualization skipped.")
        return

    print("Analyzing Matrix data...")
    np = numpy_module
    pd = pandas_module
    _ = matplotlib_module

    points_count = 1000
    print(f"Processing {points_count} data points...")

    timeline = np.arange(points_count)
    signal = np.sin(timeline / 25.0)
    noise = np.random.normal(0.0, 0.15, points_count)
    values = signal + noise

    data_frame = pd.DataFrame({"tick": timeline, "signal": values})
    data_frame["moving_average"] = data_frame["signal"].rolling(window=30).mean()

    print("Generating visualization...")
    pyplot.figure(figsize=(10, 5))
    pyplot.plot(data_frame["tick"], data_frame["signal"], label="Signal", alpha=0.5)
    pyplot.plot(
        data_frame["tick"],
        data_frame["moving_average"],
        label="Moving Average (30)",
        linewidth=2,
    )
    pyplot.title("Matrix Stream Analysis")
    pyplot.xlabel("Time Tick")
    pyplot.ylabel("Signal Intensity")
    pyplot.legend()
    pyplot.tight_layout()

    output_file = "matrix_analysis.png"
    try:
        pyplot.savefig(output_file)
        print("Analysis complete!")
        print(f"Results saved to: {output_file}")
    except Exception:
        print("Analysis completed, but saving the figure failed.")
    finally:
        pyplot.close()


def main() -> None:
    """Entrypoint for dependency checks and sample analysis."""
    dependency_map = {
        "pandas": ("pandas", "pandas"),
        "numpy": ("numpy", "numpy"),
        "matplotlib": ("matplotlib", "matplotlib"),
        "requests": ("requests", "requests"),
    }

    results: Dict[str, DependencyResult] = {}
    for key, (module_name, package_name) in dependency_map.items():
        results[key] = check_dependency(module_name, package_name)

    print_dependency_status(results)

    essentials_ok = all(results[name][0] for name in ("pandas", "numpy", "matplotlib"))
    if not essentials_ok:
        sys.exit(1)

    run_analysis(results)


if __name__ == "__main__":
    main()