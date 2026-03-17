from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        mana_budget = 6
        cards_played: list[str] = []
        targets_attacked: list[str] = []
        damage_dealt = 0

        playable_cards = sorted(hand, key=lambda card: card.cost)
        for card in playable_cards:
            if card.cost > mana_budget:
                continue
            mana_budget -= card.cost
            cards_played.append(card.name)

            if hasattr(card, "attack"):
                damage_dealt += card.attack
            elif hasattr(card, "effect_type") and card.effect_type == "damage":
                damage_dealt += 3

            if card not in battlefield:
                battlefield.append(card)

        if cards_played:
            targets_attacked = self.prioritize_targets(
                ["Enemy Creature", "Enemy Player"]
            )

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": 6 - mana_budget,
                "targets_attacked": targets_attacked,
                "damage_dealt": damage_dealt,
            },
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            ordered = ["Enemy Player"]
            ordered.extend(
                target
                for target in available_targets
                if target != "Enemy Player"
            )
            return ordered
        return available_targets
