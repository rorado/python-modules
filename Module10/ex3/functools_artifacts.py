from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable, Dict, List, Union, Any
import operator


def spell_reducer(spells: List[int], operation: str) -> int:
    operations: Dict[str, Callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    func = operations[operation]
    return reduce(func, spells)


def partial_enchanter(
    base_enchantment: Callable
) -> Dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(
            base_enchantment, power=50, element="lightning"
        ),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell: Any) -> str:
        return f"Unknown spell type: {type(spell)}"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell deals {spell} points!"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment spell: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return ", ".join(cast(s) for s in spell)

    return cast


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    print("\nTesting partial enchanter...")

    def enchant(target: str, power: int, element: str) -> str:
        return f"{element.title()} enchant of power {power} cast on {target}!"

    enchantments = partial_enchanter(enchant)
    print(enchantments["fire_enchant"]("dragon"))
    print(enchantments["ice_enchant"]("goblin"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(100))
    print(dispatcher("freeze"))
    print(dispatcher([10, "burn", 5]))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)