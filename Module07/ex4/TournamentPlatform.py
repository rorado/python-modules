import random

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:

    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("Both card IDs must be registered")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        score1 = card1.attack_power + random.randint(0, 3)
        score2 = card2.attack_power + random.randint(0, 3)

        if score1 >= score2:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self._update_ratings(winner, loser)

        self.matches_played += 1
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> list:
        ranked = sorted(
            self.cards.values(),
            key=lambda card: card.rating,
            reverse=True,
        )
        return [
            {
                "name": card.name,
                "card_id": card.card_id,
                "rating": card.rating,
                "record": f"{card.wins}-{card.losses}",
            }
            for card in ranked
        ]

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        avg_rating = 0
        if total_cards:
            avg_rating = (
                sum(card.rating for card in self.cards.values()) // total_cards
            )
        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }

    def _update_ratings(
        self, winner: TournamentCard, loser: TournamentCard
    ) -> None:
        winner.rating += 10
        loser.rating = max(0, loser.rating - 10)
