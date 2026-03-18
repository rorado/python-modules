from ex0.CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())

    available_mana = 6
    print(f"\nPlaying Fire Dragon with {available_mana} mana available:")
    print("Playable:", dragon.is_playable(available_mana))
    print("Play result:", dragon.play({}))

    print("\nFire Dragon attacks Goblin Warrior:")
    print("Attack result:", dragon.attack_target("Goblin Warrior"))

    available_mana = 3
    print(f"\nTesting insufficient mana ({available_mana} available):")
    print("Playable:", dragon.is_playable(available_mana))

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
