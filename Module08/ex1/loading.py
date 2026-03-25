
import importlib
import sys
from typing import Any, Dict, Optional, Tuple

DependencyResult = Tuple[bool, Optional[str], Optional[str], Optional[Any]]


def check_dependency(module_name: str, package_name: str) -> DependencyResult:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        return True, package_name, str(version), module
    except Exception:
        return False, package_name, None, None


def print_dependency_status(results: Dict[str, DependencyResult]) -> None:
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

    if not all_ok:
        print()
        print("Missing dependencies detected."
              " Install them, then rerun loading.py")
        return

    print()


def run_analysis(results: Dict[str, DependencyResult]) -> None:
    pd = results["pandas"][3]
    np = results["numpy"][3]

    if pd is None or np is None:
        print("Cannot run analysis: pandas or numpy is missing.")
        return

    try:
        plt = importlib.import_module("matplotlib.pyplot")
    except Exception:
        print("Cannot draw plot: matplotlib.pyplot is missing.")
        return
    print("Analyzing Matrix data...")

    points_count = 100
    values = np.random.randint(1, 100, points_count)
    data_frame = pd.DataFrame({
            "index": np.arange(points_count),
            "value": values
        })

    print(f"Processing {points_count} data points...")

    plt.figure(figsize=(19, 4))
    plt.plot(
            data_frame["index"],
            data_frame["value"],
            marker="o",
            color="blue"
        )
    plt.title("Matrix Data Analysis")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.tight_layout()

    print("Generating visualization...\n")
    output_file = "matrix_analysis.png"
    print("Analysis complete!")
    try:
        plt.savefig(output_file)
        print(f"Results saved to: {output_file}")
    finally:
        plt.close()


def main() -> None:
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

    essentials_ok = all(results[name][0]
                        for name in ("pandas", "numpy", "matplotlib"))
    if not essentials_ok:
        sys.exit(1)

    run_analysis(results)


if __name__ == "__main__":
    main()
