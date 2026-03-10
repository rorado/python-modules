try:
    from alchemy.grimoire import record_spell, validate_ingredients
except Exception as err:
    print(err)


def main() -> None:
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print(
        'validate_ingredients("fire air"): '
        f'{validate_ingredients("fire air")}'
    )
    print(
        'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}'
    )

    print("\nTesting spell recording with validation:")
    print(
        'record_spell("Fireball", "fire air"): '
        f'{record_spell("Fireball", "fire air")}'
    )
    print(
        'record_spell("Dark Magic", "shadow"): '
        f'{record_spell("Dark Magic", "shadow")}'
    )

    print("\nTesting late import technique:")
    print(
        'record_spell("Lightning", "air"): '
        f'{record_spell("Lightning", "air")}'
    )
    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
