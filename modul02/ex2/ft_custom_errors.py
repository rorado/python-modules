
class GardenError(Exception):
    """Base class for all garden-related errors"""
    pass


class PlantError(GardenError):
    """Error related to plants"""
    pass


class WaterError(GardenError):
    """Error related to watering"""
    pass


def raise_plant_error() -> None:
    """Raises a PlantError for demonstration purposes."""
    raise PlantError("The tomato plant is wilting!")


def raise_water_error() -> None:
    """Raises a WaterError for demonstration purposes."""
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Demonstrates handling of custom garden-related errors."""
    print("=== Custom Garden Errors Demo ===")

    print()
    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()
    print("All custom error types work correctly!")
