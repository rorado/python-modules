import sys
from typing import Dict


def parse_inventory(args: list[str]) -> Dict[str, int]:
    inventory: Dict[str, int] = {}

    for arg in args:
        try:
            name, qty = arg.split(":")
            inventory[name] = inventory.get(name, 0) + int(qty)
        except ValueError:
            print(f"Invalid item format: {arg}")

    return inventory


def main() -> None:
    if len(sys.argv) == 1:
        print("No inventory items provided.")
        return

    inventory = parse_inventory(sys.argv[1:])

    total_items = sum(inventory.values())
    unique_items = len(inventory)

    most_item = max(inventory.items(), key=lambda x: x[1])
    least_item = min(inventory.items(), key=lambda x: x[1])

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")

    print()
    print("=== Current Inventory ===")
    total = sum(inventory.values())
    for name, qty in inventory.items():
        percent = (qty / total) * 100
        print(f"{name}: {qty} units ({percent:.1f}%)")

    print()
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {most_item[0]} ({most_item[1]} units)")
    print(f"Least abundant: {least_item[0]} ({least_item[1]} units)")

    categories = {
        "Scarce": {},
        "Moderate": {}
    }

    for item, qty in inventory.items():
        if qty <= 3:
            categories["Scarce"][item] = qty
        else:
            categories["Moderate"][item] = qty


    print()
    print("=== Item Categories ===")
    print(f"Moderate: {categories['Moderate']}")
    print(f"Scarce: {categories['Scarce']}")

    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()
