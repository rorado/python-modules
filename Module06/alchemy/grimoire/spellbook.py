def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)

    if validation_result.endswith("VALID") and not validation_result.endswith("INVALID"):
        return f"Spell recorded: {spell_name} ({validation_result})"

    return f"Spell rejected: {spell_name} ({validation_result})"
