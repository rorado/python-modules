
def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """
        Checks plant health and raises ValueError if something is wrong.
        Returns a success message if all values are valid.
    """

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours "
                         f"{sunlight_hours} is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    try:
        msg = check_plant_health("tomato", 5, 8)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing empty plant name...")
    try:
        msg = check_plant_health("", 5, 8)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad water level...")
    try:
        msg = check_plant_health("lettuce", 15, 8)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("Testing bad sunlight hours...")
    try:
        msg = check_plant_health("carrots", 5, 0)
        print(msg)
    except ValueError as e:
        print(f"Error: {e}")
    print()

    print("All error raising tests completed!")
