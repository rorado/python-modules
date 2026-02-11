
def garden_operations() -> None:
    """Demonstrates catching common Python errors with try-except."""

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        file = open("file.txt")
        file.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'file.txt'")

    print("Testing KeyError...")
    try:
        plants = {"tomato": 5}
        print(plants["banana"])
    except KeyError:
        print("Caught KeyError: banana")

    print("Testing multiple errors together...")
    try:
        int("abc") / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types() -> None:
    """Runs garden_operations to show error handling in action."""
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")
