
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("type of Rose:", type(Plant))
    Rose = Plant("Rose", 30, 20)
    Sunflower = Plant("Sunflower", 150, 45)
    Cactus = Plant("Cactus", 40, 100)

    for plant in (Rose, Sunflower, Cactus):
        print(plant.display_info())
