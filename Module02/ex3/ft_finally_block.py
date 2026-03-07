def water_plants(plant_list: list) -> None:
    """Waters each plant in the list and handles invalid plants gracefully."""

    print("Opening watering system")
    try:
        for plant in plant_list:
            if not plant:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests the watering system with valid and invalid plant lists."""

    print("=== Garden Watering System ===")

    print("Testing normal watering...")
    good_plants = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_plants = ["tomato", None, "carrots"]
    water_plants(bad_plants)
    print()
    print("Cleanup always happens, even with errors!")
