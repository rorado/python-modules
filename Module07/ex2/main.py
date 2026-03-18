from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Epic",
        attack_power=5,
        health=8,
        mana_pool=8,
    )

    print("\nPlaying Arcane Warrior (Elite Card):")
    play_result = arcane_warrior.play({"battlefield": []})
    print(f"Play result: {play_result}")

    print("\nCombat phase:")
    attack_result = arcane_warrior.attack("Enemy")
    defense_result = arcane_warrior.defend(5)
    print(f"Attack result: {attack_result}")
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    mana_result = arcane_warrior.channel_mana(3)
    print(f"Spell cast: {spell_result}")
    print(f"Mana channel: {mana_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
