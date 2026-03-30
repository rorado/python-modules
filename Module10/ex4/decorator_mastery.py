from typing import Callable, Any
import functools
import time

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"Spell completed in {duration:.4f} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not args:
                return "Insufficient power for this spell"
            power = args[0]
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 2):
                try:
                    return func(*args, **kwargs) 
                except Exception:
                    if attempt <= max_attempts:
                        print(f"Spell failed, retrying... ({attempt}/{max_attempts})")
                    else:
                        return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Name must be:
        - at least 3 characters
        - only letters and spaces
        """
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"
    
def main() -> None:
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    print(MageGuild.validate_mage_name("Mage123"))
    print(guild.cast_spell("Fireball", 15)) 
    print(guild.cast_spell("Ice", 5))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(err)