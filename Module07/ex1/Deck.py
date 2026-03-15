from typing import List
from ex0.Card import Card
import random

class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = sum(1 for c in self.cards if getattr(c, "attack", None) is not None)
        spells = sum(1 for c in self.cards if getattr(c, "effect_type", None) is not None)
        artifacts = sum(1 for c in self.cards if getattr(c, "durability", None) is not None)
        avg_cost = sum(c.cost for c in self.cards) / total if total else 0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }