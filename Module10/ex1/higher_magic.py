def spell_combiner(spell1: callable, spell2: callable) -> callable:
	if not callable(spell1) or not callable(spell2):
		raise TypeError("Both arguments must be callable")
	def combined(*args, **kwargs):
		return spell1(*args, **kwargs), spell2(*args, **kwargs)

	return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
	if not callable(base_spell):
		raise TypeError("base_spell must be callable")
	def amplified(*args, **kwargs):
		return base_spell(*args, **kwargs) * multiplier

	return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
	if not callable(condition) or not callable(spell):
		raise TypeError("Both arguments must be callable")
	def conditional(*args, **kwargs):
		if condition(*args, **kwargs):
			return spell(*args, **kwargs)
		return "Spell fizzled"

	return conditional


def spell_sequence(spells: list[callable]) -> callable:
	if not all(callable(spell) for spell in spells):
		raise TypeError("spells must be callable")
	def sequence(*args, **kwargs):
		return [spell(*args, **kwargs) for spell in spells]

	return sequence


def main():
	def fireball(target: str) -> str:
		return f"Fireball hits {target}"

	def heal(target: str) -> str:
		return f"Heals {target}"

	def spark(base_power: int) -> int:
		return base_power

	print("Testing spell combiner...")
	combined = spell_combiner(fireball, heal)
	hit_result, heal_result = combined("Dragon")
	print(f"Combined spell result: {hit_result}, {heal_result}")

	print("\nTesting power amplifier...")
	mega_spark = power_amplifier(spark, 3)
	print(f"Original: {spark(10)}, Amplified: {mega_spark(10)}")
	
if __name__ == "__main__":
	try:
		main()
	except Exception as err:
		print(f"An error occurred: {err}")
