from functools import partial

def enchant(power, element, target):
    return f"{element.title()} spell of power {power} cast on {target}"

def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
        'lightning_enchant': partial(base_enchantment, power=50, element='lightning')
    }

enchantments = partial_enchanter(enchant)

print(enchantments['fire_enchant']("dragon")) 
print(enchantments['ice_enchant']("goblin"))
print(enchantments['lightning_enchant']("orc")) 