
class Plant:
    def __init__(self, name: str, height: int, age_days: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.age_days += 1

    def display_info(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.age_days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 30, 20)
    starting_height = rose.height
    print("=== Day 1 ===")
    print(rose.display_info())

    print("=== Day 7 ===")
    for day in range(7):
        rose.grow()
        rose.age()
    print(rose.display_info())
    growth = rose.height - starting_height
    print(f"Growth this week: +{growth}cm")
