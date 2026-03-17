from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack_power <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")
        if mana_pool < 0:
            raise ValueError("Mana pool cannot be negative")
        self.attack_power = attack_power
        self.health = health
        self.mana_pool = mana_pool

    def play(self, game_state: dict) -> dict:
        battlefield = game_state.setdefault("battlefield", [])
        battlefield.append(self.name)
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed with combat and magic abilities",
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.attack_power // 2, incoming_damage)
        taken = max(incoming_damage - blocked, 0)
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
            "combat_role": "elite_frontline",
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        costs = {
            "fireball": 4,
            "frost_nova": 3,
            "arcane_blast": 2,
        }
        mana_cost = costs.get(spell_name.lower(), 2)
        if mana_cost > self.mana_pool:
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "error": "Not enough mana",
            }
        self.mana_pool -= mana_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            raise ValueError("Channel amount must be non-negative")
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool,
            "school": "arcane",
            "spell_slots": 3,
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update(
            {
                "type": "Elite",
                "attack": self.attack_power,
                "health": self.health,
                "mana_pool": self.mana_pool,
            }
        )
        return info
