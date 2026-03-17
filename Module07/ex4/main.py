from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


print("=== DataDeck Tournament Platform ===")
print("Registering Tournament Cards...")

platform = TournamentPlatform()

fire_dragon = TournamentCard(
    card_id="dragon_001",
    name="Fire Dragon",
    cost=5,
    rarity="Legendary",
    attack_power=7,
    health=10,
    rating=1200,
)
ice_wizard = TournamentCard(
    card_id="wizard_001",
    name="Ice Wizard",
    cost=4,
    rarity="Epic",
    attack_power=6,
    health=9,
    rating=1150,
)

first_id = platform.register_card(fire_dragon)
second_id = platform.register_card(ice_wizard)

print(f"{fire_dragon.name} (ID: {first_id}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {fire_dragon.rating}")
print(f"- Record: {fire_dragon.wins}-{fire_dragon.losses}")

print(f"{ice_wizard.name} (ID: {second_id}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print(f"- Rating: {ice_wizard.rating}")
print(f"- Record: {ice_wizard.wins}-{ice_wizard.losses}")

print("\nCreating tournament match...")
match = platform.create_match(first_id, second_id)
print(f"Match result: {match}")

print("\nTournament Leaderboard:")
leaderboard = platform.get_leaderboard()
for index, entry in enumerate(leaderboard, start=1):
    print(
        f"{index}. {entry['name']} - "
        f"Rating: {entry['rating']} ({entry['record']})"
    )

print("\nPlatform Report:")
print(platform.generate_tournament_report())
print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
