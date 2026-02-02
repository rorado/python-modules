
class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> str:
        return f"{self.name} ({self.height}cm, {self.age} days)"


class Flower(Plant):

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> str:
        return f"{self.name} is blooming beautifully!"

    def display_info(self) -> str:
        return (
                f"{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color"
                )


class Tree(Plant):

    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        shade_area = self.trunk_diameter * 1.56
        return f"{self.name} provides {shade_area} square meters of shade"

    def display_info(self) -> str:
        return (
                f"{self.name} (Tree): {self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter"
                )


class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def display_info(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
            f"{self.harvest_season} harvest, "
            f"{self.name} is {self.nutritional_value}"
            )


if __name__ == "__main__":

    print("=== Garden Plant Types ===")
    print()

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")

    for plant in [rose, sunflower]:
        print(plant.display_info())
        print(plant.bloom())
    print()

    oak = Tree("Oak", 500, 1825, 50)
    maple = Tree("Maple", 300, 1500, 40)
    for plant in [oak, maple]:
        print(plant.display_info())
        print(plant.produce_shade())
    print()

    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    carrot = Vegetable("Carrot", 30, 70, "autumn", "rich in vitamin A")
    for plant in [tomato, carrot]:
        print(plant.display_info())
