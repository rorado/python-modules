class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height
        self.grow_val = 0
        self.kind = "regular"

    def grow(self, amount: int = 1) -> None:
        self.height += amount
        self.grow_val += amount
        print(f"{self.name} grew {amount}cm")

    def display_info(self) -> str:
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, color: str, is_blooming: bool = True) -> None:
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming
        self.kind = "flowering"

    def display_info(self) -> str:
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height}cm, {self.color} flowers ({status})"


class PrizeFlower(FloweringPlant):

    def __init__(self, name: str, height: int, color: str, prize_points: int) -> None:
        super().__init__(name, height, color)
        self.prize_points = prize_points
        self.kind = "prize"

    def display_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.prize_points}"


class GardenManager:
    total_gardens = 0

    def __init__(self) -> None:
        self.gardens = {}
        GardenManager.total_gardens += 1

    def add_plant(self, garden_name: str, plant: Plant) -> None:
        if garden_name not in self.gardens:
            self.gardens[garden_name] = []
        self.gardens[garden_name].append(plant)
        print(f"Added {plant.name} to {garden_name}'s garden")

    def grow_plants(self, garden_name: str) -> None:
        if garden_name in self.gardens:
            print(f"{garden_name} is helping all plants grow...")
            for plant in self.gardens[garden_name]:
                plant.grow(2)

    def report(self, garden_name: str) -> None:
        if garden_name in self.gardens:
            stats = self.GardenStats(self.gardens[garden_name])

            print(f"=== {garden_name}'s Garden Report ===")
            for plant in self.gardens[garden_name]:
                print(f"- {plant.display_info()}")

            print()
            print(f"Plants added: {stats.total_plants()}, Total growth: {stats.total_growth()}cm")
            print(f"Plant types: {stats.display_count_types()}")
            print()
            print(f"Height validation test: {stats.validate_heights()}")

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    class GardenStats:

        def __init__(self, plants) -> None:
            self.plants = plants

        def total_plants(self) -> int:
            count = 0
            for _ in self.plants:
                count += 1
            return count

        def total_growth(self) -> int:
            total = 0
            for plant in self.plants:
                total += plant.grow_val
            return total

        def display_count_types(self) -> str:
            regular = 0
            flowering = 0
            prize = 0
            for plant in self.plants:
                if plant.kind == "prize":
                    prize += 1
                elif plant.kind == "flowering":
                    flowering += 1
                else:
                    regular += 1
            return f"{regular} regular, {flowering} flowering, {prize} prize"

        def validate_heights(self) -> bool:
            for plant in self.plants:
                if not GardenManager.validate_height(plant.height):
                    return False
            return True


if __name__ == "__main__":

    print("=== Garden Management System Demo ===")
    print()

    manager = GardenManager()

    manager.add_plant("Alice", Plant("Oak Tree", 100))
    manager.add_plant("Alice", FloweringPlant("Rose", 25, "red", True))
    manager.add_plant("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))

    print()
    manager.grow_plants("Alice")
    print()
    manager.report("Alice")

    print()
    manager.add_plant("Bob", Plant("Maple", 90))
    print()
    manager.report("Bob")

    GardenManager.create_garden_network()
