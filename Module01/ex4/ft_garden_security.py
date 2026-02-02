
class SecurePlant:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def display_info(self) -> str:
        return f"{self.name} ({self.__height}cm, {self.__age} days)"


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = SecurePlant("Rose")
    print("Plant created:", plant.name)

    plant.set_height(20)
    plant.set_age(30)

    print()
    plant.set_height(-5)

    print()
    print("Current plant:", plant.display_info())
