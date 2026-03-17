from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack_power <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")
        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        board = game_state.setdefault("battlefield", [])
        board.append(self.card_id)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament combatant enters the arena",
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "tournament_melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.attack_power // 3, incoming_damage)
        damage_taken = max(0, incoming_damage - blocked)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
            "combat_ready": self.health > 0,
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 10) - (self.losses * 10)

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            raise ValueError("Wins update must be non-negative")
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            raise ValueError("Losses update must be non-negative")
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "card_id": self.card_id,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "card_id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
            "power": self.attack_power,
        }
