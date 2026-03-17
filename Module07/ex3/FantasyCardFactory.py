import random

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def __init__(self) -> None:
        self._creatures = [
            ("Fire Dragon", 5, "Legendary", 7, 5),
            ("Goblin Warrior", 2, "Common", 2, 2),
        ]
        self._spells = [
            ("Fireball", 3, "Rare", "damage"),
            ("Ice Shard", 2, "Uncommon", "debuff"),
            ("Lightning Bolt", 3, "Rare", "damage"),
        ]
        self._artifacts = [
            ("Mana Ring", 2, "Uncommon", 4, "+1 mana per turn"),
            ("Ancient Staff", 4, "Epic", 5, "+2 spell power"),
        ]

    def create_creature(self, name_or_power: str | int | None = None):
        card_data = self._creatures[0]
        if isinstance(name_or_power, str):
            for creature in self._creatures:
                if creature[0].lower() == name_or_power.lower():
                    card_data = creature
                    break
        elif isinstance(name_or_power, int):
            card_data = (
                "Forged Beast",
                max(1, name_or_power // 2),
                "Rare",
                name_or_power,
                max(1, name_or_power - 1),
            )
        return CreatureCard(*card_data)

    def create_spell(self, name_or_power: str | int | None = None):
        card_data = random.choice(self._spells)
        if isinstance(name_or_power, str):
            for spell in self._spells:
                if spell[0].lower() == name_or_power.lower():
                    card_data = spell
                    break
        elif isinstance(name_or_power, int):
            card_data = (
                "Arcane Burst",
                max(1, name_or_power // 2),
                "Rare",
                "damage",
            )
        return SpellCard(*card_data)

    def create_artifact(self, name_or_power: str | int | None = None):
        card_data = self._artifacts[0]
        if isinstance(name_or_power, str):
            for artifact in self._artifacts:
                if artifact[0].lower() == name_or_power.lower():
                    card_data = artifact
                    break
        elif isinstance(name_or_power, int):
            card_data = (
                "Runed Totem",
                max(1, name_or_power // 3),
                "Uncommon",
                max(1, name_or_power),
                "+1 all stats",
            )
        return ArtifactCard(*card_data)

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        for _ in range(size):
            picker = random.choice(["creature", "spell", "artifact"])
            if picker == "creature":
                cards.append(self.create_creature())
            elif picker == "spell":
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {
            "theme": "fantasy",
            "size": size,
            "cards": cards,
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball", "ice_shard", "lightning_bolt"],
            "artifacts": ["mana_ring", "ancient_staff"],
        }
