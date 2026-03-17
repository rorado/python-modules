from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:

    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.hand: list = []
        self.battlefield: list = []
        self.turns_simulated = 0
        self.total_damage = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature("Fire Dragon"),
            factory.create_creature("Goblin Warrior"),
            factory.create_spell("Lightning Bolt"),
        ]

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine is not configured")

        result = self.strategy.execute_turn(self.hand, self.battlefield)
        cards_played = result["actions"]["cards_played"]
        self.hand = [
            card for card in self.hand if card.name not in cards_played
        ]

        self.turns_simulated += 1
        self.total_damage += result["actions"]["damage_dealt"]
        return result

    def get_engine_status(self) -> dict:
        strategy_name = "unconfigured"
        if self.strategy is not None:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": len(self.hand) + len(self.battlefield),
        }
