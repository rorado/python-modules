from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    hand_view = [
        f"{card.name} ({card.cost})" for card in engine.hand
    ]
    print(f"Hand: {hand_view}")

    turn_result = engine.simulate_turn()
    print("Turn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}")

    print("Game Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern:"
          " Maximum flexibility achieved!")


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)
