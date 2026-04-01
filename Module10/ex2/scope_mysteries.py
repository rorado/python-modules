from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulates(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulates


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        if key in memory:
            return memory[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter())
    print()
    print("\nTesting enchantment factory...")
    flaming_enchant = enchantment_factory("Flaming")
    frozen_enchant = enchantment_factory("Frozen")
    print(flaming_enchant("Sword"))
    print(frozen_enchant("Shield"))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
