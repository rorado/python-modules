from typing import List
import random

from ex0.Card import Card


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

    def draw_card(self) -> Card | None:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = 0
        for c in self.cards:
            if getattr(c, "attack", None) is not None:
                creatures += 1

        spells = 0
        for c in self.cards:
            if getattr(c, "effect_type", None) is not None:
                spells += 1

        artifacts = 0
        for c in self.cards:
            if getattr(c, "durability", None) is not None:
                artifacts += 1
        avg_cost = sum(c.cost for c in self.cards) / total if total else 0
        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": f"{avg_cost:.2f}",
        }
