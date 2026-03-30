from typing import Callable, Any, Tuple, List


def spell_combiner(
    spell1: Callable,
    spell2: Callable,
) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both arguments must be callable")

    def combined(*args: Any) -> Tuple[Any, Any]:
        return spell1(*args), spell2(*args)

    return combined


def power_amplifier(
    base_spell: Callable,
    multiplier: int
) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be callable")

    def amplified(*args: Any) -> int:
        return base_spell(*args) * multiplier

    return amplified


def conditional_caster(
    condition: Callable,
    spell: Callable
) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("Both arguments must be callable")

    def conditional(*args: Any) -> Any:
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: List[Callable]
) -> Callable:
    if not all(callable(spell) for spell in spells):
        raise TypeError("spells must be callable")

    def sequence(*args: Any, **kwargs: Any) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]

    return sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def spark(base_power: int) -> int:
        return base_power

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    hit_result, heal_result = combined("Dragon")
    print(f"Combined spell result: {hit_result}, {heal_result}")

    print("\nTesting power amplifier...")
    mega_spark = power_amplifier(spark, 3)
    print(f"Original: {spark(10)}, Amplified: {mega_spark(10)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"An error occurred: {err}")
