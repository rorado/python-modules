from typing import Generator


def game_event_stream(count: int) -> Generator[str, None, None]:
    players = ("alice", "bob", "charlie")
    actions = ("killed monster", "found treasure", "leveled up", "found secret room", )

    for i in range(count):
        player = players[i % len(players)]
        level = (i % 15) + 1
        action = actions[(i - 1) % len(actions)]
        yield f"Player {player} (level {level}) {action}"


def fibonacci_stream(count: int) -> Generator[int, None, None]:
    a = 0
    b = 1
    for _ in range(count):
        yield a
        temp = a + b
        a = b
        b = temp


def prime_stream(count: int) -> Generator[int, None, None]:
    found = 0
    number = 2

    while found < count:
        is_prime = True
        i = 2
        while i * i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            yield number
            found += 1
        number += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")

    stream = game_event_stream(total_events)

    total = 0
    high_level = 0
    treasure = 0
    level_up = 0
    secret_room = 0

    try:
        while True:
            event = next(stream)
            total += 1

            if total <= 3:
                print(f"Event {total}: {event}")
            elif total == 4:
                print("...")

            if "(level 10)" in event or "(level 11)" in event or \
               "(level 12)" in event or "(level 13)" in event or \
               "(level 14)" in event or "(level 15)" in event:
                high_level += 1

            if "found treasure" in event:
                treasure += 1

            if "leveled up" in event:
                level_up += 1
            
            if "found secret room" in event:
                secret_room += 1

    except StopIteration:
        pass

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")
    print(f"Secret room events: {secret_room}")
    print("Memory usage: Constant (streaming)")

    print("\n=== Generator Demonstration ===")

    print("Fibonacci sequence (first 10): ", end="")
    fib = fibonacci_stream(10)
    fib_iter = iter(fib)

    try:
        first = True
        while True:
            number = next(fib_iter)
            if not first:
                print(", ", end="")
            print(number, end="")
            first = False
    except StopIteration:
        pass

    print()

    print("Prime numbers (first 5): ", end="")
    primes = prime_stream(5)
    prime_iter = iter(primes)

    try:
        first = True
        while True:
            number = next(prime_iter)
            if not first:
                print(", ", end="")
            print(number, end="")
            first = False
    except StopIteration:
        pass

    print()


if __name__ == "__main__":
    main()


