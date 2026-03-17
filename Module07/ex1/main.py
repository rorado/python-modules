from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

print("\n=== DataDeck Deck Builder ===")
print("Building deck with different card types...")

fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
lightning_bolt = SpellCard("Lightning Bolt", 3, "Rare", "damage")
mana_crystal = ArtifactCard(
    "Mana Crystal", 2, "Uncommon", 5, "+1 mana per turn"
)

deck = Deck()
deck.add_card(fire_dragon)
deck.add_card(lightning_bolt)
deck.add_card(mana_crystal)

deck.shuffle()

stats = deck.get_deck_stats()
print(f"\nDeck stats: {stats}\n")

print("Drawing and playing cards:\n")
game_state = {}
while card := deck.draw_card():
    print(f"Drew: {card.name} ({type(card).__name__})")
    result = card.play(game_state)
    print(f"Play result: {result}\n")

print("Polymorphism in action: Same interface, different card behaviors!")
