def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice_achievements = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }

    bob_achievements = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }

    charlie_achievements = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print()

    print("=== Achievement Analytics ===")

    # Union: all unique achievements
    all_achievements = (
        alice_achievements
        .union(bob_achievements)
        .union(charlie_achievements)
    )

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    # Intersection: achievements common to all players
    common_achievements = (
        alice_achievements
        .intersection(bob_achievements)
        .intersection(charlie_achievements)
    )

    print(f"Common to all players: {common_achievements}")

    # Rare achievements (owned by only one player)
    rare_achievements = (
        all_achievements
        .difference(alice_achievements.intersection(bob_achievements))
        .difference(alice_achievements.intersection(charlie_achievements))
        .difference(bob_achievements.intersection(charlie_achievements))
    )

    print(f"Rare achievements (1 player): {rare_achievements}")

    # Player comparisons
    alice_bob_common = alice_achievements.intersection(bob_achievements)
    alice_unique = alice_achievements.difference(bob_achievements)
    bob_unique = bob_achievements.difference(alice_achievements)

    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()

