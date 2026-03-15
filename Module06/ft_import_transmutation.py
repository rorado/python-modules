import alchemy.elements
from alchemy.elements import create_fire, create_water, create_earth
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion


def main() -> None:
    print("\n=== Import Transmutation Mastery ===")

    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")

    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")

    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")

    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
