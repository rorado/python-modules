
class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}"
                         f" is too high (max 12)")
    return (
            f"{plant_name}: healthy"
            f"(water: {water_level}, sun: {sunlight_hours})"
            )


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name: str, water_level: int, sunlight_hours: int):
        try:
            if not name:
                raise PlantError("Plant name cannot be empty!")
            self.plants[name] = (water_level, sunlight_hours)
            print(f"Added {name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error watering plants: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self):
        print("Checking plant health...")
        for plant, (water, sun) in self.plants.items():
            try:
                result = check_plant_health(plant, water, sun)
                print(result)
            except ValueError as e:
                print(f"Error checking {plant}: {e}")


def test_garden_management():
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato", 5, 8)
    manager.add_plant("lettuce", 15, 8)
    manager.add_plant("", 5, 8)

    print("Watering plants...")
    manager.water_plants()

    manager.check_health()

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")
