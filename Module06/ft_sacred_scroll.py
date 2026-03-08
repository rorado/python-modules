import alchemy
import alchemy.elements


def main() -> None:
    print("=== Sacred Scroll Mastery ===")

    print("Testing direct module access:")
    print(
        "alchemy.elements.create_fire(): "
        f"{alchemy.elements.create_fire()}"
    )
    print(
        "alchemy.elements.create_water(): "
        f"{alchemy.elements.create_water()}"
    )
    print(
        "alchemy.elements.create_earth(): "
        f"{alchemy.elements.create_earth()}"
    )
    print(
        "alchemy.elements.create_air(): "
        f"{alchemy.elements.create_air()}"
    )

    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
