
class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def display_info(self) -> str:
        return (f"{self.name} ({self.height}cm, {self.age_days} days)")


if __name__ == "__main__":
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    plants = []
    plant_len = 0
    for name, height, age in plants_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.display_info()}")
        plant_len += 1

    print(f"Total plants created: {plant_len}")
